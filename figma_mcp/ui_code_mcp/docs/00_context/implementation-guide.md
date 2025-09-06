# Implementation Guide

## Technical Architecture

### Framework Structure
```
docs/
├── 00_context/                  # AI's Long-term Memory
│   ├── requirements.md          # Business goals, success criteria
│   ├── implementation-guide.md  # Technical architecture, patterns
│   └── reference.md             # Additional references
├── 01_plan/                     # Project Management  
│   └── project-roadmap.md       # Timeline, current status, sprints
└── 02_implement/                # Sprint Execution
    ├── sprint-1.md              # Detailed task breakdown
    ├── sprint-2.md              # Daily progress tracking
    └── sprint-3.md              # Acceptance criteria
```

## Coding Patterns & Best Practices

### Documentation-First Approach
- Mọi feature mới phải có documentation trước khi implement
- Documentation phải được update khi có thay đổi
- Sử dụng markdown format cho tất cả documentation

### Test-Driven Development
- Viết test trước khi implement feature
- Mọi feature mới phải có corresponding tests
- Test suite phải PASS trước khi mark task là complete
- Maintain test coverage ở mức cao

### Code Quality Standards
- Sử dụng consistent coding style
- Implement proper error handling
- Avoid code duplication
- Follow SOLID principles
- Clean commit messages theo conventional format

### File Organization
- Tách biệt concerns theo modules
- Sử dụng clear naming conventions
- Organize imports properly
- Keep files focused và cohesive

## Development Workflow

### Session Startup Process
1. Đọc `project-roadmap.md` để hiểu current status
2. Reference context documents khi cần
3. Identify task từ current sprint
4. Focus mode: làm một task tại một thời điểm

### Task Implementation Cycle
1. **Identify**: Xác định task từ sprint hoặc user request
2. **Plan**: Break down task thành smaller steps
3. **Implement**: Code implementation với proper error handling
4. **Test**: Update test suite cho feature mới
5. **Validate**: All tests phải PASS
6. **Document**: Update progress trong sprint document
7. **Commit**: Clean commit với clear message
8. **Update**: Update sprint status và roadmap

## Quality Gates

### Code Quality
- Code compiles successfully
- No syntax errors
- Follows project coding standards
- Proper error handling implemented

### Testing Requirements
- All automated tests PASS
- New features have corresponding tests
- No regressions in existing functionality
- Test coverage maintained

### Documentation Standards
- All changes documented
- API documentation updated
- README files current
- No sensitive data committed

## Technology Stack Considerations

### Language & Framework Selection
- Chọn technology stack phù hợp với project requirements
- Consider maintainability và scalability
- Ensure good community support
- Compatible với existing systems

### Development Tools
- Version control với Git
- Automated testing framework
- Code formatting tools
- Documentation generators
