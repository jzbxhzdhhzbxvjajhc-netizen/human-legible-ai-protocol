# Changelog / 变更记录

All notable changes to the canonical HLAI release are recorded here. Version classification follows [VERSIONING.md](VERSIONING.md).

## Unreleased

- No changes yet.

## 0.2.0 - 2026-09-02

**Classification:** normative pre-1.0 minor release. This is not a patch because it changes mandatory factual, permission, and safety boundaries.

**定级：** 1.0 前的规范性次版本。它改变了强制事实、授权和安全边界，所以不是补丁。

### Added

- an anonymous third-party desktop host field-test record;
- `control-010`, covering installation of an external tool plus transfer of user files;
- this changelog and explicit protocol-versioning rules.

### Changed

- scoped claims that are true only in the current situation instead of turning possibilities into absolute facts;
- required external-tool decisions to cover necessity, source, permission scope, temporary or persistent presence, cost, and alternatives;
- required data-transfer decisions to cover recipient, scope, retention, purpose, cost, and less-exposing alternatives;
- clarified that a familiar brand or official source does not by itself provide sufficient consent.

### Migration

Implementations claiming `HLAI-CONTROL` or `HLAI-FULL` must adopt the revised external-tool and data-transfer requirements, update hard-failure handling, and run `control-010`. An implementation conforming to `0.1.1` is not automatically conforming to `0.2.0`.

声明符合 `HLAI-CONTROL` 或 `HLAI-FULL` 的实现，必须采用更新后的外部工具与数据外发规则、更新硬失败处理，并运行 `control-010`。符合 `0.1.1` 不代表自动符合 `0.2.0`。

## 0.1.1 - 2026-09-02

**Classification:** first public experimental release.

**定级：** 首个公开试验版本。

- established START, CONTROL, and EXPLAIN modes, seven core rules, safety requirements, conformance levels, evaluation cases, and the reference Skill;
- published the canonical repository, founding statement, governance, attribution, licensing, and initial release evidence.
