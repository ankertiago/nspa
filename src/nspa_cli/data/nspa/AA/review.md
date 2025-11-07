# /review · 代码评审提示词

## 适用场景
当需要对最近一次提交/合并请求做快速而系统的代码评审，并将评审结果写入 `.nspa/Output/review.md` 时使用。

## 输入
- `change_scope`：本次评审的分支、PR 链接或提交范围。
- `diff`：关键文件的改动片段（带行号）。
- `context`：需求背景、验收标准、相关设计文档或测试说明。

## Claude 指令
1. **理解背景**：根据 `change_scope` 和 `context` 提炼目标与约束，确认要关注的模块/接口。
2. **审查代码**：
   - 正确性：边界条件、异常处理、空指针/None、并发等；
   - 安全性：输入校验、权限、敏感信息；
   - 性能 & 可维护性：复杂度、重复逻辑、日志质量；
   - 测试：现有/缺失的单元测试、集成测试。
3. **输出结论**：
   - 明确区分「阻断问题」「建议优化」等等级；
   - 每条指出文件路径+行号+问题描述+修复建议；
   - 总结整体风险、需要补充的测试或验证步骤。
4. **写入目标文件**：生成 Markdown 片段，供用户粘贴到 `.nspa/Output/review.md`。

## 输出格式
```markdown
# Code Review Report
- Scope: <change_scope>
- Reviewer: Claude Code
- Overall Risk: <Low|Medium|High>

## Findings
| Severity | Location | Description | Recommendation |
| --- | --- | --- | --- |
| Blocking/Warning/Info | path/to/file:123 | ... | ... |

## Testing & Follow-ups
- Suggested Tests: [...]
- Action Items: [...]
```

> 生成后提示用户把以上内容保存到 `.nspa/Output/review.md`，并在处理完 action items 后可再次运行 `/review` 跟进。
