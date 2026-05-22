#!/usr/bin/env python3
"""PyAutoGUI 鼠标操作工具

用法:
    python mouse_move.py <x> <y> --click       移动到 (x,y) 并点击
    python mouse_move.py <x> <y> --roll [高度]   移动到 (x,y) 并垂直滚动指定高度
    python mouse_move.py <x1> <y1> --drag <x2> <y2>  从 (x1,y1) 拖到 (x2,y2)
"""
import argparse
import time
import random
import pyautogui

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01


def human_move(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))


def cmd_click(x, y):
    human_move(x, y)
    time.sleep(random.uniform(0.03, 0.08))
    pyautogui.click()


def cmd_roll(x, y, amount=1):
    human_move(x, y)
    time.sleep(0.1)
    pyautogui.scroll(amount)


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
    p.add_argument("x", type=int, help="起始 X 坐标")
    p.add_argument("y", type=int, help="起始 Y 坐标")
    p.add_argument("--click", action="store_true", help="移动到目标并单击")
    p.add_argument("--roll", type=int, nargs="?", const=1, default=None,
                   help="移动到目标并垂直滚动（可选指定滚动量，默认1）")
    p.add_argument("--drag", type=int, nargs=2, metavar=("X2", "Y2"),
                   help="拖动到目标坐标")
    args = p.parse_args()

    if args.drag:
        cmd_drag(args.x, args.y, args.drag[0], args.drag[1])
    elif args.click:
        cmd_click(args.x, args.y)
    elif args.roll is not None:
        cmd_roll(args.x, args.y, args.roll)
    else:
        p.error("请指定 --click, --roll 或 --drag")


if __name__ == "__main__":
    main()
