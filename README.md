<div align="center">

# Ai Bom MCP

**MCP server for ai bom mcp operations**

[![PyPI](https://img.shields.io/pypi/v/meok-ai-bom-mcp)](https://pypi.org/project/meok-ai-bom-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MEOK AI Labs](https://img.shields.io/badge/MEOK_AI_Labs-MCP_Server-purple)](https://meok.ai)

</div>

## Overview

Ai Bom MCP provides AI-powered tools via the Model Context Protocol (MCP).

## Tools

| Tool | Description |
|------|-------------|
| `generate_ai_bom` | Generate an AI-BOM in CycloneDX ML-BOM format (or SPDX 3.0) with all 10 required |
| `audit_ai_bom_completeness` | Audit an existing AI-BOM for completeness against the 10 required field categori |
| `map_to_regulation` | Map an AI-BOM against a specific regulatory framework's technical documentation |
| `required_fields` | List the 10 required AI-BOM field categories and their fields. |
| `sign_ai_bom_attestation` | Generate a cryptographically signed AI-BOM completeness attestation (Pro/Enterpr |

## Installation

```bash
pip install meok-ai-bom-mcp
```

## Usage with Claude Desktop

Add to your Claude Desktop MCP config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "ai-bom-mcp": {
      "command": "python",
      "args": ["-m", "meok_ai_bom_mcp.server"]
    }
  }
}
```

## Usage with FastMCP

```python
from mcp.server.fastmcp import FastMCP

# This server exposes 5 tool(s) via MCP
# See server.py for full implementation
```

## License

MIT © [MEOK AI Labs](https://meok.ai)
