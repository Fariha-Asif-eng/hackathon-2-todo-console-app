<!-- SYNC IMPACT REPORT:
Version change: N/A -> 1.0.0
Modified principles: N/A (New constitution)
Added sections: All sections
Removed sections: None
Templates requiring updates: N/A
Follow-up TODOs: None
-->
# Todo Console Application Constitution
<!-- AI-driven, spec-first development workflow -->

## Core Principles

### I. Spec-First Development
All features must originate from written specifications. Code may not be written unless a spec exists and is approved. Specs are the single source of truth.

### II. Agentic Workflow Discipline
The workflow must follow:
Spec → Plan → Task Breakdown → Implementation → Review
Skipping phases is forbidden. Each phase must leave an artifact in the specs history folder.

### III. No Manual Coding Rule
Humans are not allowed to write or edit production code directly. All code must be generated through Claude Code from formal specs.

### IV. Reproducibility
Any contributor must be able to recreate the project from specs alone. Setup, prompts, and instructions must be deterministic and documented.

### V. Clean Architecture
The Python code must follow modular structure:
- clear separation of concerns
- single responsibility per module
- readable naming
- no hidden side effects
- CLI logic separated from task management logic

### VI. Incremental Feature Integrity
Core features (Add, Delete, Update, View, Mark Complete) must remain functional after every iteration. No regression is allowed.

## Additional Constraints

### VII. Transparent Spec History
All specification changes must be versioned and stored. No spec is overwritten without preserving history.

### VIII. Review-Driven Iteration
Every generated output must be reviewed against the spec. If mismatch occurs, the spec is updated or regenerated before proceeding.

### IX. Minimalism and Clarity
The system should remain simple, understandable, and focused on the CLI todo objective. Avoid unnecessary abstractions or frameworks.

### X. AI Accountability
The AI agent must justify major implementation decisions in comments or logs so reviewers can trace reasoning.

## Development Workflow

### Specification Phase
- All features must begin with a detailed specification document
- Specifications must include acceptance criteria, edge cases, and error handling
- Specifications must be stored in the `specs/` directory with proper versioning

### Planning Phase
- Each specification must be converted into an architectural plan
- Plans must address all ten core principles
- Plans must include risk analysis and mitigation strategies

### Implementation Phase
- All code must be generated from formal specifications
- Implementation must follow clean architecture principles
- Each feature must be tested against its specification

### Review Phase
- Generated code must be reviewed against the original specification
- All ten core principles must be validated
- Any discrepancies must be resolved before proceeding

## Governance

This constitution governs all development activities in the repository. All team members must adhere to these principles. Amendments to this constitution require formal approval and must be documented with clear rationale.

All pull requests and reviews must verify compliance with these principles. Code complexity must be justified with clear benefits and trade-offs.

**Version**: 1.0.0 | **Ratified**: 2026-02-07 | **Last Amended**: 2026-02-07