# Hermes Delivery Gates

Local-first, read-only delivery-gate validation for [Hermes Agent](https://github.com/NousResearch/hermes-agent).

## Status

Pre-alpha. The initial release will validate a repository change against an explicit policy and evidence receipts. It will not commit, push, merge, deploy, read credentials, access the network, execute arbitrary commands, or dispatch agents.

## Planned v0.1 tools

- `delivery_preflight` — inspect repository and declared policy readiness.
- `delivery_diff_scope` — compare changed files against an allowlist and denylist.
- `delivery_receipt_validate` — validate structured evidence receipts.

## Development

```bash
uv sync --group dev
uv run pytest
hermes plugins doctor . --ci
hermes plugins compat .
```

## License

MIT. See [LICENSE](LICENSE).
