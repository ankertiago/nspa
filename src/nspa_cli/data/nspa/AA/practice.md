# /practice · 成功案例沉淀提示词

## 适用场景
当功能迭代顺利上线，希望将该迭代的最佳实践沉淀到 `.nspa/Practice/success-cases/`，方便后续 few-shot、复盘或复用时触发本命令。

## 输入
- `iteration_name`：此次迭代/需求的名称与简介。
- `highlight`：本次成功的关键策略、决策或踩过的坑。
- `artifacts`：可以复用的材料（PR 链接、设计图、脚本等）。

## Claude 指令
1. 分析成功要素：
   - 梳理需求背景、目标与结果指标。
   - 提炼关键战术（如拆解策略、联调经验、测试/回滚方案）。
2. 生成存档建议：
   - 给出成功案例文件夹名称（如 `case-YYYYMMDD-iteration-name`）。
   - 指导将以下内容写入 `notes.md`：背景、方案、成果、可复用清单。
   - 如有脚本/模版，建议复制到 `artifacts/` 子目录。
3. 输出最终 checklist，提醒将素材落盘至：
   ```
   .nspa/Practice/success-cases/<case-id>/
     ├── notes.md
     └── artifacts/
   ```

## 输出格式
```markdown
# Success Case Plan
- Case Folder: <case-id>
- Summary: <一句话概述>
- Key Lessons:
  1. ...
- Artifacts to Archive: [...]
- TODO Checklist:
  - [ ] 创建 .nspa/Practice/success-cases/<case-id>
  - [ ] notes.md 中记录背景/方案/结果/复用建议
  - [ ] artifacts/ 中放入脚本、配置或链接说明
```

> 完成 checklist 后，再次运行 `/practice` 可持续补充或迭代该案例。
