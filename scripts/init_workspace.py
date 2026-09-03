#!/usr/bin/env python3
"""Initialize a PM shaping workspace with reusable templates."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip() or "pm-product"
    slug = re.sub(r"[^\w\u4e00-\u9fff.-]+", "-", value, flags=re.UNICODE).strip("-")
    return slug or "pm-product"


def write_once(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def looks_like_workspace(path: Path) -> bool:
    markers = [
        path / "shaping",
        path / "prd",
        path / "prototype",
        path / "00-intake.md",
        path / "01-product-shaping.md",
    ]
    return any(marker.exists() for marker in markers)


def resolve_workspace(name: str, root: str | None) -> Path:
    target_name = f"{slugify(name)}-workspace"
    cwd = Path.cwd()
    for candidate in [cwd, *cwd.parents]:
        if candidate.name == target_name or looks_like_workspace(candidate):
            return candidate

    if root:
        base = Path(root).expanduser()
        if base.name == target_name or looks_like_workspace(base):
            return base
        return base / target_name

    return cwd / target_name


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="未命名产品")
    parser.add_argument("--type", default="待确认")
    parser.add_argument("--root", default=None)
    args = parser.parse_args()

    workspace = resolve_workspace(args.name, args.root)
    shaping = workspace / "shaping"
    today = date.today().isoformat()

    write_once(
        shaping / "00-intake.md",
        f"""# 输入材料

| 项目 | 内容 |
| --- | --- |
| 产品名 | {args.name} |
| 产品类型 | {args.type} |
| 创建日期 | {today} |

## 用户原始想法

[待确认]

## 已有材料

- [待确认: 文档、截图、竞品、会议纪要、数据来源]
""",
    )
    write_once(
        shaping / "01-product-shaping.md",
        """# 产品定型

## 一句话定位

[待确认: 为谁，在什么场景，解决什么问题，带来什么进展]

## 目标用户

| 用户类型 | 特征 | 核心诉求 | 决策权/影响 |
| --- | --- | --- | --- |
| 主用户 | [待确认] | [待确认] | [待确认] |

## 核心场景

| 场景 | 触发条件 | 当前做法 | 痛点 | 成功标准 |
| --- | --- | --- | --- | --- |
| [待确认] | [待确认] | [待确认] | [待确认] | [待确认] |

## 产品形态

[待确认: Web / App / 小程序 / 插件 / API / 内部系统 / 其他]
""",
    )
    write_once(
        shaping / "02-jtbd.md",
        """# JTBD 分析

## Job Story

当 [情境]，我想要 [动机]，从而 [期望进展]。

## 四力分析

| Push 当前痛点 | Pull 新方案吸引力 | Anxiety 顾虑 | Habit 惯性 |
| --- | --- | --- | --- |
| [待确认] | [待确认] | [待确认] | [待确认] |

## 任务分层

| 类型 | 内容 |
| --- | --- |
| 功能任务 | [待确认] |
| 情感任务 | [待确认] |
| 社会任务 | [待确认] |
""",
    )
    write_once(
        shaping / "03-scope.md",
        """# MVP 范围

## 做

- [待确认]

## 暂缓

- [待确认]

## 不做

- [待确认]

## 成功指标

| 指标 | 定义 | 目标 | 数据来源 |
| --- | --- | --- | --- |
| [待确认] | [待确认] | [待确认] | [待确认] |
""",
    )
    write_once(
        shaping / "04-pages-and-flows.md",
        """# 页面与流程

## 页面清单

| 页面 | 用户任务 | 核心信息 | 主要操作 | 入口/出口 |
| --- | --- | --- | --- | --- |
| [待确认] | [待确认] | [待确认] | [待确认] | [待确认] |

## 主流程

```mermaid
flowchart TD
  A[进入产品] --> B[完成核心任务]
  B --> C[获得结果]
```

## 关键状态

| 对象 | 状态 | 触发条件 | 可执行操作 |
| --- | --- | --- | --- |
| [待确认] | [待确认] | [待确认] | [待确认] |
""",
    )
    write_once(
        shaping / "05-open-questions.md",
        """# 待确认问题

| 编号 | 问题 | 影响范围 | 优先级 | 结论 |
| --- | --- | --- | --- | --- |
| Q1 | [待确认] | [待确认] | 高 | [待确认] |
""",
    )
    write_once(
        shaping / "06-shaped-brief.md",
        """# 定型摘要记录

> 每次用户确认后，把摘要追加到本文件末尾，不覆盖历史版本。
""",
    )
    print(workspace)


if __name__ == "__main__":
    main()
