# PM-Make

快速帮助产品经理把粗略产品想法定型成清晰、可严谨表述的产品构思。适用于产品构思、需求澄清、MVP 定义、用户场景梳理、JTBD 分析、信息架构和产品方案定型；可独立使用，也可作为 PRD 或原型制作前置步骤。
## 快速安装
```bash
npx skill add 996pm/PM-Make
```

## Skill 工作流程

1. 运行如下指令创建工作区：

   ```bash
   python3 {$SKILL-PATH}/PM-Make/scripts/init_workspace.py --name "<产品名或项目名>" --type "<产品类型>"
   ```

   默认会创建或复用 `{name}-workspace/`。如果终端已在某个工作区内，脚本只会在当前工作区补齐缺失文件，不会再嵌套一层。

2. 读取生成的 `shaping/00-intake.md` 和 `shaping/01-product-shaping.md`，把用户已有输入填入文档；没有信息的地方保留 `[待确认]`。
3. 按「一次只问 3-5 个关键问题」推进，不让用户填写大表。
4. 每轮对话后更新：
   - `shaping/01-product-shaping.md`
   - `shaping/02-jtbd.md`
   - `shaping/03-scope.md`
   - `shaping/04-pages-and-flows.md`
   - `shaping/05-open-questions.md`
5. 当关键信息足够时，输出「定型摘要」并等待用户确认。

## 需求澄清维度

- 产品一句话：为谁，在什么场景，解决什么高价值问题。
- 目标用户：主用户、决策者、影响者、被影响者。
- JTBD：情境、动机、期望进展、功能/情感/社会任务。
- 当前替代方案：用户现在如何解决，痛点和切换阻力是什么。
- MVP 边界：必须有、暂缓、不做。
- 核心流程：入口、主路径、关键分支、失败/空/等待状态。
- 页面与信息架构：页面清单、页面职责、跳转关系。
- 业务规则：状态、权限、数据来源、关键约束。

详细提问方法按需读取 [shaping-playbook.md](references/shaping-playbook.md)。

## 定型通过标准

只有同时满足以下条件，才建议进入 PRD 或原型：

- 产品定位能用 1-2 句话准确表述。
- 至少 1 个核心用户、1 个核心场景、1 条主流程明确。
- MVP 范围有明确「做/不做/待确认」。
- 关键业务规则、权限、数据对象没有被含糊带过。
- 未确认内容已集中写入 `shaping/05-open-questions.md`。
