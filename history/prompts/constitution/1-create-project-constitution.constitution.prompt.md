---
id: 1
title: Create-project-constitution
stage: constitution
date: 2026-02-07
surface: agent
model: Qwen
feature: none
branch: main
user: user
command: /sp.constitution
labels: [constitution, spec-first, ai-workflow]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

Create a project constitution for an AI-driven, spec-first development workflow.

Project context:
We are building a command-line todo application using Python 3.13+ with UV. The project must be developed entirely through an agentic workflow using Claude Code and Spec-Kit Plus. No manual coding is allowed. All implementation must originate from written specifications.

The constitution must enforce strict engineering rules that guide every decision in this repository.

Include the following principles:

1. Spec-First Development
All features must originate from written specifications. Code may not be written unless a spec exists and is approved. Specs are the single source of truth.

2. Agentic Workflow Discipline
The workflow must follow:
Spec → Plan → Task Breakdown → Implementation → Review
Skipping phases is forbidden. Each phase must leave an artifact in the specs history folder.

3. No Manual Coding Rule
Humans are not allowed to write or edit production code directly. All code must be generated through Claude Code from formal specs.

4. Reproducibility
Any contributor must be able to recreate the project from specs alone. Setup, prompts, and instructions must be deterministic and documented.

5. Clean Architecture
The Python code must follow modular structure:
- clear separation of concerns
- single responsibility per module
- readable naming
- no hidden side effects
- CLI logic separated from task management logic

6. Incremental Feature Integrity
Core features (Add, Delete, Update, View, Mark Complete) must remain functional after every iteration. No regression is allowed.

7. Transparent Spec History
All specification changes must be versioned and stored. No spec is overwritten without preserving history.

8. Review-Driven Iteration
Every generated output must be reviewed against the spec. If mismatch occurs, the spec is updated or regenerated before proceeding.

9. Minimalism and Clarity
The system should remain simple, understandable, and focused on the CLI todo objective. Avoid unnecessary abstractions or frameworks.

10. AI Accountability
The AI agent must justify major implementation decisions in comments or logs so reviewers can trace reasoning.

Output format:
Write the constitution as a formal engineering manifesto with clear rules, short explanations, and enforceable language.

## Response snapshot

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

## Outcome

- ✅ Impact: Created project constitution with 10 core principles for AI-driven, spec-first development
- 🧪 Tests: No tests needed for constitution creation
- 📁 Files: Updated .specify/memory/constitution.md with new constitution
- 🔁 Next prompts: Build specification based on updated constitution
- 🧠 Reflection: The constitution enforces strict engineering rules that will guide all future development decisions in the repository.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin creating feature specifications based on the new constitution