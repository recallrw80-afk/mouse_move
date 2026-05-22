---
name: mouse-control
description: 通过 mouse_move.exe 控制鼠标移动、点击、双击、右键、中键、拖拽、滚轮滚动、长按和图片识别定位。当用户需要自动化鼠标操作时使用此技能。
---

# 鼠标控制技能

通过调用 `scripts/mouse_move.exe` 实现鼠标自动化操作，无需安装 Python 环境。

## 用法

```bash
mouse_move <x> <y> --click           # 移动到 (x,y) 左键单击
mouse_move <x> <y> --double          # 移动到 (x,y) 左键双击
mouse_move <x> <y> --right           # 移动到 (x,y) 右键单击
mouse_move <x> <y> --middle          # 移动到 (x,y) 中键单击
mouse_move <x> <y> --move            # 只移动到 (x,y) 不点击
mouse_move <x> <y> --roll [N]        # 移动到 (x,y) 垂直滚动 N 格(默认1,正上负下)
mouse_move <x> <y> --hroll [N]       # 移动到 (x,y) 水平滚动 N 格(默认1,正右负左)
mouse_move <x> <y> --hold <秒>       # 移动到 (x,y) 长按指定秒数
mouse_move <x1> <y1> --drag <x2> <y2> # 从 (x1,y1) 拖拽到 (x2,y2)
mouse_move --image <图片> --click    # 通过图片识别定位后单击
```

## 参数说明

| 参数 | 说明 |
|------|------|
| `x`, `y` | 目标坐标（--image 模式下可选） |
| `--click` | 左键单击 |
| `--double` | 左键双击 |
| `--right` | 右键单击 |
| `--middle` | 中键单击 |
| `--move` | 只移动不点击 |
| `--roll [N]` | 垂直滚动 N 格，正向上负向下，默认 1 |
| `--hroll [N]` | 水平滚动 N 格，正向右负向左，默认 1 |
| `--hold <秒>` | 长按指定秒数 |
| `--drag X2 Y2` | 拖拽到目标坐标 |
| `--image <图片>` | 通过图片识别定位目标 |
