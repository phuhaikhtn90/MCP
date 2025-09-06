# AI Rules for Context Engineering Framework

## Startup Workflow (Each Session)

1. Check the project setup.
2. **Read `docs/01_plan/project-roadmap.md`** - To understand the project status and current focus.
3. **Reference context documents** - `requirements.md`, `implementation-guide.md` as needed.

## Task Management Process

### Task Lifecycle:
1. **Identify task**: From the current sprint or user request.
2. **Focus mode**: Work on one task at a time, do not jump around.
3. **Implement feature**: Code implementation with proper error handling.
4. **Test Suite Update**: MANDATORY - Update the test suite for every new feature.
5. **Quality validation**: All tests must PASS before marking a task as complete.
6. **Update progress**: Update the sprint document only when ALL TESTS PASS.
7. **Commit clean**: Use a clear commit message following conventions.
8. **Update status**: Update the sprint document and `project_roadmap.md`.

### Quality Gates:
- **Code compiles**: The build must succeed.
- **Test Suite**: All automated tests (connection + functional) must PASS.
- **No regressions**: Existing functionality must not be broken.
- **No token leaks**: Do not commit sensitive data.
- **Documentation**: Update docs with test results.

### Test Requirements:
- Every new feature requires corresponding tests.
- Tests must PASS before a sprint task can be completed.
- The test suite must be maintained and updated consistently.

## Role of Document Groups

### `00_context/` - Technical Foundation (DO NOT EDIT WITHOUT EXPLICIT APPROVAL):
- `requirements.md`: Business requirements, project scope, success criteria.
- `implementation-guide.md`: Technical architecture, code patterns, API client structure.
- `reference.md`: Complete reference documentation and best practices.

### `01_plan/` - Project Management:
- `project-roadmap.md`: Project timeline, current status, sprint progress, next actions.

### `02_implement/` - Sprint Execution (UPDATED DAILY):
- `sprint-X-*.md`: Detailed task breakdown, acceptance criteria, daily progress tracking.

## Documentation Rules

### Update Rules:
- **project_roadmap.md**: Update for major progress, phase completion, current status.
- **sprint_*.md**: Update for daily progress, task completion.
- **00_context/**: Never update without explicit approval (requirements, architecture, API specs).

### Maintenance Principles:
- **AVOID DUPLICATION**: Link instead of repeating information.
- **KEEP CONCISE**: Overview docs stay short, details go in specific docs.
- **SINGLE SOURCE OF TRUTH**: Each piece of information lives in one place.
- **CROSS-REFERENCE**: Use links to connect related information.
- **STATUS FIRST**: Always show the current status clearly.

### Writing Style:
- Concise and actionable.
- Use status indicators: Not Started, In Progress, Completed, Blocked.
- Include time estimates and actual time spent.
- Link related documents instead of duplicating content.

### Document Flow: 
`project_roadmap.md` → `sprint_*.md` → specific details.
Never put detailed task lists in overview documents.

## Behavioral Guidelines

### Session Management:
- Always start by reading the roadmap to understand current context
- Focus on one task at a time until completion
- Update documentation as you progress
- Maintain clean commit history

### Communication Style:
- Be direct and technical
- Provide clear status updates
- Reference documentation when explaining decisions
- Ask for clarification only when necessary

### Problem Solving:
- Follow the established workflow
- Document issues and solutions
- Maintain quality standards
- Test thoroughly before marking complete

## Framework Philosophy

This framework transforms you from a "Vibe Coder" to an "AI Orchestrator":
- **Vibe Coder**: Prompt và hy vọng
- **AI Orchestrator**: Tạo ra hệ sinh thái để AI hoạt động hiệu quả

Remember: You are not just executing tasks, you are maintaining a systematic approach to development that ensures consistency, quality, and progress tracking.
