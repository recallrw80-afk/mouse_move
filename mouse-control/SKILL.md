---
name: mouse-control
description: 通过 mouse_move.exe 控制鼠标移动、点击、拖拽和垂直滚动。当用户需要自动化鼠标操作时使用此技能。
---

# 鼠标控制技能

通过调用 `scripts/mouse_move.exe` 实现鼠标自动化操作，无需安装 Python 环境。

## 用法

```bash
scripts/mouse_move.exe <x> <y> --click           # 移动到 (x,y) 并单击
scripts/mouse_move.exe <x> <y> --roll [amount]   # 移动到 (x,y) 并垂直滚动（默认1）
scripts/mouse_move.exe <x1> <y1> --drag <x2> <y2> # 从 (x1,y1) 拖拽到 (x2,y2)
```

## 参数说明

| 参数 | 说明 |
|------|------|
| `x`, `y` | 目标坐标（位置参数，必填） |
| `--click` | 鼠标左键单击 |
| `--roll [N]` | 垂直滚动 N 个单位，正数向上，负数向下，默认 1 |
| `--drag X2 Y2` | 鼠标拖拽，从起始坐标到目标坐标 |
