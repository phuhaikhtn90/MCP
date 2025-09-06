# Context Engineering Framework

Hệ thống tài liệu để xây dựng "bộ não tập thể" cho AI, giúp AI hoạt động hiệu quả như một AI Orchestrator thay vì Vibe Coder.

## Cấu trúc Framework

```
docs/
├── 00_context/                  # AI's Long-term Memory
│   ├── requirements.md          # Business goals, success criteria
│   ├── implementation-guide.md  # Technical architecture, patterns
│   └── reference.md             # Additional references
├── 01_plan/                     # Project Management  
│   └── project-roadmap.md       # Timeline, current status, sprints
├── 02_implement/                # Sprint Execution
│   ├── sprint-1.md              # Detailed task breakdown
│   ├── sprint-template.md       # Template for future sprints
│   └── ...                      # Additional sprint files
└── README.md                    # This file

CLAUDE.md                        # AI Rules file (root level)
```

## Cách sử dụng

### Bước 1: Setup Framework (Đã hoàn thành)
Framework này đã được setup sẵn với:
- ✅ Cấu trúc thư mục hoàn chỉnh
- ✅ AI's Long-term Memory documents
- ✅ Project management templates
- ✅ Sprint execution templates
- ✅ AI Rules file (CLAUDE.md)

### Bước 2: Customize cho dự án của bạn
1. **Cập nhật `requirements.md`**: Thay đổi business goals và success criteria
2. **Điều chỉnh `implementation-guide.md`**: Cập nhật technical architecture
3. **Modify `project-roadmap.md`**: Set timeline và milestones cho dự án
4. **Tạo sprint mới**: Copy `sprint-template.md` thành `sprint-X.md`

### Bước 3: Bắt đầu làm việc với AI
Nói với AI: **"Bạn biết phải làm gì rồi đấy."**

AI sẽ tự động:
1. Đọc `project-roadmap.md` để hiểu current status
2. Reference context documents khi cần
3. Thực hiện tasks theo quy trình đã định
4. Update documentation khi có progress

## Nguyên tắc hoạt động

### AI's Long-term Memory (`00_context/`)
- **KHÔNG ĐƯỢC SỬA** mà không có approval rõ ràng
- Chứa foundation knowledge của dự án
- AI sẽ reference những file này để hiểu context

### Project Management (`01_plan/`)
- Update khi có major progress
- Maintain current status và next actions
- Single source of truth cho project timeline

### Sprint Execution (`02_implement/`)
- Update hàng ngày với progress
- Detailed task breakdown và acceptance criteria
- Track actual time vs estimates

## Quy trình làm việc

### Mỗi session với AI:
1. AI đọc roadmap để hiểu current focus
2. Identify task từ current sprint
3. Focus mode: một task tại một thời điểm
4. Implement → Test → Document → Commit
5. Update progress trong sprint document

### Quality Gates:
- Code compiles successfully
- All tests PASS
- No regressions
- Documentation updated
- Clean commit messages

## Lợi ích của Framework

### Cho Developer:
- Giảm thời gian "nhắc bài" cho AI
- Tăng chất lượng code
- Có thể track progress rõ ràng
- Framework có thể reuse

### Cho AI:
- Luôn có context đầy đủ
- Biết phải làm gì tiếp theo
- Follow consistent workflow
- Maintain quality standards

## Best Practices

### Documentation:
- Keep concise và actionable
- Avoid duplication, use links
- Single source of truth
- Clear status indicators

### Task Management:
- One task at a time
- Test-first approach
- Quality gates before completion
- Regular progress updates

### Communication:
- Be direct và technical
- Reference documentation
- Provide clear status updates
- Ask for clarification when needed

## Troubleshooting

### AI "quên" context:
→ Check documentation completeness trong `00_context/`

### Code quality issues:
→ Review quality gates trong `CLAUDE.md`

### Timeline delays:
→ Reassess sprint planning trong `01_plan/`

### Test failures:
→ Implement proper TDD workflow

## Framework Philosophy

**Vibe Coder**: Prompt và hy vọng  
**AI Orchestrator**: Tạo ra hệ sinh thái để AI hoạt động hiệu quả

Framework này biến AI từ một "thực tập sinh ngơ ngác" thành một "kỹ sư có kỷ luật".

---

## Nguồn tham khảo
- [Context Engineering Article](https://phucnt.substack.com/p/context-engineering-tu-vibe-coder)
- [AI Coding Best Practices](https://phucnt.substack.com/p/ai-coding-tu-vibe-coding-en-chuyen)

*Framework được tạo dựa trên bài viết "Context Engineering: Từ Vibe Coder Đến AI Orchestrator" của Phúc NT*
