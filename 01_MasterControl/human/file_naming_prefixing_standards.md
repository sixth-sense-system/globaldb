# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "2d2a89047de4067f999cbb40ba95e6b35e1cec38b46a5b0a4fb6498dc5783bb8"}, "provenance": {"build_id": "d687698a-e18b-4318-ab07-58248fcd1797", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
📄 File Naming & Prefixing Standards

This document is canonical. All other references to file naming and prefixing must point here. Any change must follow the CBR change-control workflow.

Purpose

To ensure ENERQIS’ file/folder names are clear, predictable, scalable, and enterprise-grade across all modules.

1. General Naming Rules

Consistency First: Always use lowercase with underscores (snake_case) for file names.

Descriptive, not cryptic: Names should describe content or function.

Extensions: Always include proper extensions (.md, .json, .yaml, .csv, etc.).

Versioning: Do not append version numbers in file names; instead, store version history in Git or an archival folder.

Language: English, unless the file itself requires another language.

2. Folder Naming

Module folders: XX_ModuleName/ (2-digit padded index to keep modules in order, e.g., 09_Tech/).

Subfolders: Use functional names without numbers unless grouping is needed.

3. File Prefixing for Grouping

When to use prefixes

Module contains multiple clearly distinct sub-domains (e.g., 09_Tech covering APIs, environments, tools).

Human folder has more than ~7 files or categories.

Need to force thematic grouping in alphabetical order.

Prefix format

A_, B_, C_… for major thematic groups.

Optionally A1_, A2_ for nested groups if needed.

When not to use prefixes

Module is single-domain and under ~7 files.

Prefixing adds noise without benefit.

4. Machine Files

Mirror human file structure but with machine-friendly formats.

Use clear functional names: pipeline_ingest.yaml, schema_registry.json.

Avoid prefixes unless the machine folder also spans sub-domains.

5. Example
09_Tech/
├── human/
│   ├── 09A_core_stack_overview.md
│   ├── 09B_integrations_api.md
│   ├── 09C_environment_management.md
└── machine/
    ├── manifest.json
    ├── api_configs.yaml
    ├── env_setup_scripts/

6. Decision Rule

“Modules with >X sub-domains or >7 human files must use A_, B_, C_ prefixing; others don’t.”

7. Change Control

Any deviation from these standards must be documented in file_naming_prefixing_standards.md.
