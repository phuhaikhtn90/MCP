# Reference Documentation

## Context Engineering Resources

### Core Concepts
- **Context Engineering**: Phương pháp có hệ thống để xây dựng môi trường nơi AI luôn nhận được đúng thông tin, vào đúng thời điểm
- **AI's Long-term Memory**: Hệ thống tài liệu giúp AI nhớ và hiểu context của dự án
- **AI Orchestrator vs Vibe Coder**: Sự khác biệt giữa việc "điều phối AI" và "thả trôi với AI"

### Framework Benefits
- Giảm thiểu thời gian "nhắc bài" cho AI
- Tăng chất lượng code và giảm technical debt
- Tạo ra quy trình có thể lặp lại
- AI hoạt động như một kỹ sư có kỷ luật

## Document Hierarchy & Relationships

### Information Flow
```
project-roadmap.md → sprint-*.md → specific implementation details
```

### Document Responsibilities
- **00_context/**: Technical foundation (DO NOT EDIT without approval)
- **01_plan/**: Project management và timeline
- **02_implement/**: Daily execution và progress tracking

### Cross-Reference Guidelines
- Link thay vì duplicate information
- Maintain single source of truth
- Use clear status indicators
- Keep overview docs concise

## Best Practices from Article

### Setup Process
1. **Bước 1**: Xây dựng AI's Long-term Memory
   - Sử dụng Reasoning AI để tạo requirements.md
   - Dùng Internet Search AI để hoàn thiện technical docs

2. **Bước 2**: Thiết lập AI's Rules
   - Tạo file quy tắc (CLAUDE.md hoặc clinerules.md)
   - Định nghĩa Startup Workflow, Task Lifecycle, Quality Gates

3. **Bước 3**: Execution
   - Nói với AI: "Bạn biết phải làm gì rồi đấy"
   - Quan sát AI tự động thực hiện theo quy trình

### Success Metrics
- Dự án hoàn thành trong timeline
- Code quality ổn định
- Không stress vì mất kiểm soát
- AI không "lạc đường"

## Common Patterns

### Documentation Maintenance
- Update project_roadmap.md cho major progress
- Update sprint_*.md cho daily progress
- Never update 00_context/ without approval
- Avoid duplication, use links instead

### Task Management
- Focus mode: một task tại một thời điểm
- Test-first approach
- Quality gates trước khi complete
- Clean commits với clear messages

### Communication with AI
- Provide context through documentation
- Use structured workflows
- Set clear expectations
- Maintain consistency across sessions

## Tools & Technologies

### Recommended Stack
- **Documentation**: Markdown files
- **Version Control**: Git với conventional commits
- **Testing**: Automated test suites
- **AI Agents**: Claude, GPT-4, hoặc tương tự

### File Naming Conventions
- Use descriptive names
- Include version numbers for sprints
- Maintain consistent format
- Avoid special characters

## Troubleshooting

### Common Issues
- AI "quên" context → Check documentation completeness
- Code quality issues → Review quality gates
- Timeline delays → Reassess sprint planning
- Test failures → Implement proper TDD

### Recovery Strategies
- Return to documentation
- Review current sprint status
- Validate quality gates
- Restart with clear context
