---

description: "Task list for CLI Todo Application implementation"
---

# Tasks: CLI Todo Application

**Input**: Design documents from `/specs/001-cli-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/
- [X] T002 Create src/__main__.py as entry point for the CLI application
- [X] T003 [P] Create src/models/__init__.py
- [X] T004 [P] Create src/services/__init__.py
- [X] T005 [P] Create src/cli/__init__.py
- [X] T006 [P] Create src/utils/__init__.py
- [X] T007 [P] Create tests/unit/__init__.py
- [X] T008 [P] Create tests/integration/__init__.py
- [X] T009 [P] Create tests/fixtures/__init__.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T010 Create Task class in src/models/task.py based on data-model.md
- [X] T011 [P] Create TaskManager service in src/services/task_manager.py
- [X] T012 [P] Create validators utility in src/utils/validators.py
- [X] T013 Create authentication placeholder in src/utils/auth.py
- [X] T014 Create custom exceptions hierarchy in src/utils/exceptions.py
- [X] T015 [P] Create unit test for Task model in tests/unit/test_task.py
- [X] T016 [P] Create unit test for TaskManager in tests/unit/test_task_manager.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Allow users to add a new task with a title and optional description via CLI command

**Independent Test**: Can be fully tested by running the add command with a title and verifying that a new task appears in the list with a unique ID and the correct title/description.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T017 [P] [US1] Create unit test for add task functionality in tests/unit/test_task_manager.py
- [X] T018 [P] [US1] Create integration test for add command in tests/integration/test_cli.py

### Implementation for User Story 1

- [X] T019 [P] [US1] Implement add_task method in src/services/task_manager.py
- [X] T020 [US1] Implement add command in src/cli/cli_app.py using argparse
- [X] T021 [US1] Add validation for empty titles in src/utils/validators.py
- [X] T022 [US1] Ensure unique sequential ID assignment in src/services/task_manager.py
- [X] T023 [US1] Add error handling for empty titles in src/services/task_manager.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Allow users to view all tasks with their ID, title, description, and completion status

**Independent Test**: Can be fully tested by adding several tasks and then running the view command to verify all tasks are displayed with correct IDs, titles, descriptions, and completion status.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T024 [P] [US2] Create unit test for view all tasks functionality in tests/unit/test_task_manager.py
- [X] T025 [P] [US2] Create integration test for list/view command in tests/integration/test_cli.py

### Implementation for User Story 2

- [X] T026 [P] [US2] Implement get_all_tasks method in src/services/task_manager.py
- [X] T027 [US2] Implement list/view command in src/cli/cli_app.py
- [X] T028 [US2] Format task display with ID, title, description, and completion status in src/models/task.py
- [X] T029 [US2] Handle empty task list case in src/services/task_manager.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Allow users to mark a task as complete or incomplete using its ID

**Independent Test**: Can be tested by adding a task, marking it complete, and then viewing the task list to confirm the status has changed.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T030 [P] [US3] Create unit test for mark complete/incomplete functionality in tests/unit/test_task_manager.py
- [X] T031 [P] [US3] Create integration test for complete/incomplete commands in tests/integration/test_cli.py

### Implementation for User Story 3

- [X] T032 [P] [US3] Implement mark_complete and mark_incomplete methods in src/services/task_manager.py
- [X] T033 [US3] Implement complete command in src/cli/cli_app.py
- [X] T034 [US3] Implement incomplete command in src/cli/cli_app.py
- [X] T035 [US3] Add validation for valid task IDs in src/services/task_manager.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Details (Priority: P3)

**Goal**: Allow users to update the title and/or description of an existing task using its ID

**Independent Test**: Can be tested by adding a task, updating its details, and then viewing the task to confirm the changes were applied.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T036 [P] [US4] Create unit test for update task functionality in tests/unit/test_task_manager.py
- [X] T037 [P] [US4] Create integration test for update command in tests/integration/test_cli.py

### Implementation for User Story 4

- [X] T038 [P] [US4] Implement update_task method in src/services/task_manager.py
- [X] T039 [US4] Implement update command in src/cli/cli_app.py
- [X] T040 [US4] Add validation for valid task IDs in src/services/task_manager.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Allow users to delete a task using its ID

**Independent Test**: Can be tested by adding a task, deleting it, and then viewing the task list to confirm it's no longer present.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T041 [P] [US5] Create unit test for delete task functionality in tests/unit/test_task_manager.py
- [X] T042 [P] [US5] Create integration test for delete command in tests/integration/test_cli.py

### Implementation for User Story 5

- [X] T043 [P] [US5] Implement delete_task method in src/services/task_manager.py
- [X] T044 [US5] Implement delete command in src/cli/cli_app.py
- [X] T045 [US5] Add validation for valid task IDs in src/services/task_manager.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T046 [P] Add comprehensive help output with examples to src/cli/cli_app.py
- [X] T047 [P] Implement generic error handling with appropriate messages in src/utils/exceptions.py
- [X] T048 [P] Add command parsing validation in src/cli/cli_app.py
- [X] T049 [P] Add performance validation for handling 100+ tasks in src/services/task_manager.py
- [X] T050 [P] Create README.md with setup and usage instructions
- [X] T051 [P] Create CLAUDE.md with Claude Code instructions
- [X] T052 [P] Run quickstart validation from quickstart.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Create unit test for add task functionality in tests/unit/test_task_manager.py"
Task: "Create integration test for add command in tests/integration/test_cli.py"

# Launch all implementation tasks for User Story 1 together:
Task: "Implement add_task method in src/services/task_manager.py"
Task: "Implement add command in src/cli/cli_app.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence