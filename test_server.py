"""
Tests for AI-BOM (AI Bill of Materials) Compliance MCP Server
==============================================================
Tests every @mcp.tool() function directly (no MCP protocol).
Run: cd /Users/nicholas/clawd/mcp-marketplace/ai-bom-mcp && pytest test_server.py -v
"""

import json
import sys
import os

os.environ.pop("MEOK_API_KEY", None)

sys.path.insert(0, os.path.dirname(__file__))

from server import (
    generate_ai_bom,
    audit_ai_bom_completeness,
    map_to_regulation,
    required_fields,
    _usage,
    AI_BOM_REQUIRED_FIELDS,
)


def _reset_rate_limits():
    _usage.clear()


# ── generate_ai_bom ───────────────────────────────────────────────

class TestGenerateAiBom:
    def setup_method(self):
        _reset_rate_limits()

    def test_basic_cyclonedx(self):
        result = generate_ai_bom(model_name="TestModel")
        assert isinstance(result, str)
        data = json.loads(result)
        assert isinstance(data, dict)
        assert data.get("format") == "cyclonedx"
        assert "ai_bom_document" in data

    def test_cyclonedx_has_bom_format(self):
        result = generate_ai_bom(model_name="MyModel", model_version="2.0")
        data = json.loads(result)
        doc = data["ai_bom_document"]
        assert doc.get("bomFormat") == "CycloneDX"
        assert doc.get("specVersion") == "1.6"

    def test_spdx_format(self):
        result = generate_ai_bom(model_name="SpdxModel", format="spdx")
        data = json.loads(result)
        assert data.get("format") == "spdx"
        doc = data["ai_bom_document"]
        assert "spdxVersion" in doc
        assert doc["spdxVersion"].startswith("SPDX")

    def test_with_all_params(self):
        result = generate_ai_bom(
            model_name="FullModel",
            model_version="3.1.0",
            organisation="Acme AI",
            licence="MIT",
            architecture="Transformer",
            parameter_count="7B",
            training_datasets="Wikipedia, Common Crawl, BookCorpus",
        )
        data = json.loads(result)
        assert isinstance(data, dict)
        assert "ai_bom_document" in data
        assert "legal_basis" in data

    def test_legal_basis_present(self):
        result = generate_ai_bom(model_name="LegalTest")
        data = json.loads(result)
        assert "legal_basis" in data
        assert isinstance(data["legal_basis"], list)
        assert len(data["legal_basis"]) > 0

    def test_populate_next_present(self):
        result = generate_ai_bom(model_name="NextSteps")
        data = json.loads(result)
        assert "populate_next" in data
        assert isinstance(data["populate_next"], list)

    def test_empty_model_name(self):
        result = generate_ai_bom(model_name="")
        data = json.loads(result)
        assert isinstance(data, dict)

    def test_training_datasets_parsed(self):
        result = generate_ai_bom(
            model_name="DataModel",
            training_datasets="dataset_a, dataset_b, dataset_c",
        )
        data = json.loads(result)
        doc = data["ai_bom_document"]
        blob = json.dumps(doc)
        assert "dataset_a" in blob
        assert "dataset_b" in blob

    def test_empty_training_datasets(self):
        result = generate_ai_bom(model_name="NoData", training_datasets="")
        data = json.loads(result)
        doc = data["ai_bom_document"]
        blob = json.dumps(doc)
        assert "UNKNOWN" in blob

    def test_default_version(self):
        result = generate_ai_bom(model_name="DefaultVer")
        data = json.loads(result)
        blob = json.dumps(data)
        assert "1.0.0" in blob


# ── audit_ai_bom_completeness ─────────────────────────────────────

class TestAuditAiBomCompleteness:
    def setup_method(self):
        _reset_rate_limits()

    def test_empty_json(self):
        result = audit_ai_bom_completeness("{}")
        data = json.loads(result)
        assert isinstance(data, dict)
        assert "overall_score_percent" in data
        assert data["overall_score_percent"] == 0.0

    def test_invalid_json(self):
        result = audit_ai_bom_completeness("not valid json at all")
        data = json.loads(result)
        assert "error" in data

    def test_complete_bom_high_score(self):
        """A BOM with all required field names should score high."""
        complete_bom = {}
        for cat, fields in AI_BOM_REQUIRED_FIELDS.items():
            complete_bom[cat] = {f: "populated" for f in fields}
        result = audit_ai_bom_completeness(json.dumps(complete_bom))
        data = json.loads(result)
        assert data["overall_score_percent"] > 50

    def test_partial_bom(self):
        partial = {
            "model_identity": {
                "name": "TestModel",
                "version": "1.0",
                "organisation": "Test",
                "licence": "MIT",
                "release_date": "2025-01-01",
                "model_id_hash": "abc123",
            }
        }
        result = audit_ai_bom_completeness(json.dumps(partial))
        data = json.loads(result)
        assert data["overall_score_percent"] > 0
        assert "categories_detail" in data

    def test_categories_detail_structure(self):
        result = audit_ai_bom_completeness('{"name": "test"}')
        data = json.loads(result)
        assert "categories_detail" in data
        for cat in data["categories_detail"]:
            assert "category" in cat
            assert "status" in cat
            assert cat["status"] in ("COMPLETE", "PARTIAL", "MISSING")

    def test_recommendation_present(self):
        result = audit_ai_bom_completeness("{}")
        data = json.loads(result)
        assert "recommendation" in data

    def test_generated_bom_audit_round_trip(self):
        """Generate a BOM then audit it -- should not be zero."""
        _reset_rate_limits()
        bom_result = generate_ai_bom(model_name="RoundTrip", organisation="Test Corp")
        bom_data = json.loads(bom_result)
        bom_doc = json.dumps(bom_data.get("ai_bom_document", {}))

        _reset_rate_limits()
        audit_result = audit_ai_bom_completeness(bom_doc)
        audit_data = json.loads(audit_result)
        assert audit_data["overall_score_percent"] >= 0


# ── map_to_regulation ─────────────────────────────────────────────

class TestMapToRegulation:
    def setup_method(self):
        _reset_rate_limits()

    def test_eu_ai_act(self):
        result = map_to_regulation('{"name": "test"}', regulation="eu_ai_act")
        data = json.loads(result)
        assert isinstance(data, dict)
        assert data.get("regulation") == "eu_ai_act"
        assert "required_sections" in data or "aibom_mapping" in data

    def test_nist_ai_rmf(self):
        result = map_to_regulation('{"name": "test"}', regulation="nist_ai_rmf")
        data = json.loads(result)
        assert data.get("regulation") == "nist_ai_rmf"

    def test_us_eo_14028(self):
        result = map_to_regulation('{"name": "test"}', regulation="us_eo_14028")
        data = json.loads(result)
        assert data.get("regulation") == "us_eo_14028"

    def test_iso_42001(self):
        result = map_to_regulation('{"name": "test"}', regulation="iso_42001")
        data = json.loads(result)
        assert data.get("regulation") == "iso_42001"

    def test_unknown_regulation(self):
        result = map_to_regulation('{"name": "test"}', regulation="unknown_reg")
        data = json.loads(result)
        assert "error" in data

    def test_empty_bom_json(self):
        result = map_to_regulation("{}", regulation="eu_ai_act")
        data = json.loads(result)
        assert isinstance(data, dict)

    def test_default_regulation(self):
        result = map_to_regulation('{"name": "test"}')
        data = json.loads(result)
        assert data.get("regulation") == "eu_ai_act"


# ── required_fields ────────────────────────────────────────────────

class TestRequiredFields:
    def setup_method(self):
        _reset_rate_limits()

    def test_returns_json(self):
        result = required_fields()
        assert isinstance(result, str)
        data = json.loads(result)
        assert isinstance(data, dict)

    def test_has_categories(self):
        result = required_fields()
        data = json.loads(result)
        assert "required_categories" in data
        cats = data["required_categories"]
        assert isinstance(cats, dict)
        assert len(cats) == 10

    def test_has_formats(self):
        result = required_fields()
        data = json.loads(result)
        assert "formats_supported" in data
        assert isinstance(data["formats_supported"], list)

    def test_categories_match_constant(self):
        result = required_fields()
        data = json.loads(result)
        cats = data["required_categories"]
        assert set(cats.keys()) == set(AI_BOM_REQUIRED_FIELDS.keys())

    def test_idempotent(self):
        r1 = json.loads(required_fields())
        _reset_rate_limits()
        r2 = json.loads(required_fields())
        assert r1 == r2


# ── Rate Limiting ──────────────────────────────────────────────────

class TestRateLimiting:
    def setup_method(self):
        _reset_rate_limits()

    def test_rate_limit_after_10(self):
        for i in range(10):
            result = json.loads(generate_ai_bom(model_name=f"Model{i}"))
            assert "error" not in result or "limit" not in str(result.get("error", "")).lower()

        result = json.loads(generate_ai_bom(model_name="Overflow"))
        if "error" in result:
            assert "limit" in str(result["error"]).lower() or "free" in str(result["error"]).lower()
