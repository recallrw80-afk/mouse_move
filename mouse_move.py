#!/usr/bin/env python3
"""PyAutoGUI 鼠标操作工具

用法:
    python mouse_move.py <x> <y> --click          移动到 (x,y) 单击
    python mouse_move.py <x> <y> --double         移动到 (x,y) 双击
    python mouse_move.py <x> <y> --right          移动到 (x,y) 右键
    python mouse_move.py <x> <y> --middle         移动到 (x,y) 中键
    python mouse_move.py <x> <y> --move           只移动到 (x,y) 不点击
    python mouse_move.py <x> <y> --roll [N]       移动到 (x,y) 垂直滚动 N 格(默认1)
    python mouse_move.py <x> <y> --hroll [N]      移动到 (x,y) 水平滚动 N 格(默认1)
    python mouse_move.py <x> <y> --hold <秒>      移动到 (x,y) 长按 N 秒
    python mouse_move.py <x1> <y1> --drag <x2> <y2>  拖拽
    python mouse_move.py --image <图片> --click   通过图片识别定位后单击
"""
import argparse
import time
import random
import pyautogui

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01


def human_move(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))


def locate_image(img_path):
    loc = pyautogui.locateOnScreen(img_path, confidence=0.9)
    if loc is None:
        raise SystemExit(f"未在屏幕上找到: {img_path}")
    return pyautogui.center(loc)


def cmd_click(x, y):
    human_move(x, y)
    time.sleep(random.uniform(0.03, 0.08))
    pyautogui.click()


def cmd_double(x, y):
    human_move(x, y)
    time.sleep(random.uniform(0.03, 0.08))
    pyautogui.doubleClick()


def cmd_right(x, y):
    human_move(x, y)
    time.sleep(random.uniform(0.03, 0.08))
    pyautogui.rightClick()


def cmd_middle(x, y):
    human_move(x, y)
    time.sleep(random.uniform(0.03, 0.08))
    pyautogui.middleClick()


def cmd_move(x, y):
    human_move(x, y)


def cmd_roll(x, y, amount=1):
    human_move(x, y)
    time.sleep(0.1)
    pyautogui.scroll(amount)


def cmd_hroll(x, y, amount=1):
    human_move(x, y)
    time.sleep(0.1)
    pyautogui.hscroll(amount)


def cmd_hold(x, y, seconds):
    human_move(x, y)
    time.sleep(0.1)
    pyautogui.mouseDown()
    time.sleep(seconds)
    pyautogui.mouseUp()


def cmd_drag(x1, y1, x2, y2):
    human_move(x1, y1)
    time.sleep(0.1)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.moveTo(x2, y2, duration=random.uniform(0.2, 0.5))
    time.sleep(0.1)
    pyautogui.mouseUp()


def main():
    p = argparse.ArgumentParser(description="PyAutoGUI 鼠标操作")
    p.add_argument("x", type=int, nargs="?", help="X 坐标（--image 模式下可选）")
    p.add_argument("y", type=int, nargs="?", help="Y 坐标（--image 模式下可选）")
    p.add_argument("--click", action="store_true", help="左键单击")
    p.add_argument("--double", action="store_true", help="左键双击")
    p.add_argument("--right", action="store_true", help="右键单击")
    p.add_argument("--middle", action="store_true", help="中键单击")
    p.add_argument("--move", action="store_true", help="只移动不点击")
    p.add_argument("--roll", type=int, nargs="?", const=1, default=None,
                   help="垂直滚动（可选指定滚动量，正向上负向下，默认1）")
    p.add_argument("--hroll", type=int, nargs="?", const=1, default=None,
                   help="水平滚动（可选指定滚动量，正向右负向左，默认1）")
    p.add_argument("--hold", type=float, default=None,
                   help="长按指定秒数")
    p.add_argument("--drag", type=int, nargs=2, metavar=("X2", "Y2"),
                   help="拖拽到目标坐标")
    p.add_argument("--image", type=str, default=None,
                   help="通过图片识别定位目标")
    args = p.parse_args()

    # 决定坐标来源：--image 优先，否则用位置参数
    if args.image:
        x, y = locate_image(args.image)
    else:
        if args.x is None or args.y is None:
            p.error("请指定坐标 (x y) 或使用 --image 定位")
        x, y = args.x, args.y

    # 执行动作
    if args.drag:
        cmd_drag(x, y, args.drag[0], args.drag[1])
    elif args.double:
        cmd_double(x, y)
    elif args.right:
        cmd_right(x, y)
    elif args.middle:
        cmd_middle(x, y)
    elif args.move:
        cmd_move(x, y)
    elif args.click:
        cmd_click(x, y)
    elif args.roll is not None:
        cmd_roll(x, y, args.roll)
    elif args.hroll is not None:
        cmd_hroll(x, y, args.hroll)
    elif args.hold is not None:
        cmd_hold(x, y, args.hold)
    else:
        p.error("请指定一个动作: --click, --double, --right, --middle, --move, --roll, --hroll, --hold 或 --drag")


if __name__ == "__main__":
    main()
