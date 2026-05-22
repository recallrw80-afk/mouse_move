# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for mouse_move.py
# 打包命令: pyinstaller mouse_move.spec

block_cipher = None  # 不加密

# ── DPI 感知 manifest ──
# 打包后的 exe 默认无 DPI 感知，导致坐标偏移；嵌入此 manifest 解决
DPI_MANIFEST = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <application xmlns="urn:schemas-microsoft-com:asm.v3">
    <windowsSettings>
      <dpiAware xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">true</dpiAware>
      <dpiAwareness xmlns="http://schemas.microsoft.com/SMI/2016/WindowsSettings">PerMonitorV2</dpiAwareness>
    </windowsSettings>
  </application>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel level="asInvoker" uiAccess="false"/>
      </requestedPrivileges>
    </security>
  </trustInfo>
</assembly>
'''

# 将 manifest 写入临时文件供 EXE() 引用
import tempfile, os  # 标准库
_manifest_path = os.path.join(tempfile.gettempdir(), 'mouse_move_dpi.manifest')  # 临时路径
with open(_manifest_path, 'w', encoding='utf-8') as f:  # 写入 manifest
    f.write(DPI_MANIFEST)  # 写入内容

a = Analysis(
    ['mouse_move.py'],  # 入口脚本
    pathex=[],  # 搜索路径
    binaries=[],  # 额外的二进制文件
    datas=[],  # 数据文件
    hiddenimports=[
        # ── PyAutoGUI 全套 ──
        'pyautogui',  # 主模块
        'pyautogui._pyautogui_win',  # Windows 平台底层（ctypes 调 user32.dll）
        'pyautogui._pyautogui_java',  # Java 平台兜底
        'pyautogui._pyautogui_osx',  # macOS 平台兜底
        # ── PyAutoGUI 依赖链 ──
        'pyscreeze',  # 截图/图片定位
        'pymsgbox',  # 弹窗
        'pytweening',  # 缓动函数（moveTo duration 依赖）
        'pygetwindow',  # 窗口操作
        'pyrect',  # 矩形对象
        'mouseinfo',  # 鼠标信息
        'pyperclip',  # 剪贴板
        # ── Pillow（pyscreeze 图片识别依赖） ──
        'PIL',  # 图片处理
        'PIL.Image',  # 图片对象
        'PIL.ImageGrab',  # 截图（pyscreeze screenshot 依赖）
        # ── 标准库中容易漏的 ──
        'ctypes',  # Windows API 调用
        'json',  # 可能被动态加载
        'argparse',  # 命令行解析
    ],
    hookspath=[],  # 自定义 hook 路径
    hooksconfig={},  # hook 配置
    runtime_hooks=[],  # 运行时 hook
    excludes=[
        'tkinter',  # 不需要 GUI
        'matplotlib',  # 不需要画图
        'IPython',  # 不需要交互式 shell
        'jupyter',  # 不需要 notebook
        'numpy',  # 不需要数值计算
        'cv2',  # 不需要 OpenCV
    ],
    noarchive=False,  # 不归档
)

pyz = PYZ(a.pure)  # 编译 .pyc 字节码压缩包

exe = EXE(
    pyz,  # Python 字节码
    a.scripts,  # 入口脚本
    a.binaries,  # 二进制文件
    a.datas,  # 数据文件
    [],
    name='mouse_move',  # 输出 exe 文件名（不含 .exe）
    debug=True,  # 调试模式打开，方便排查
    bootloader_ignore_signals=False,  # 不忽略信号
    strip=False,  # 不裁剪符号
    upx=True,  # UPX 压缩
    upx_exclude=[],  # 不排除压缩
    runtime_tmpdir=None,  # 默认临时目录
    console=True,  # 保留控制台窗口
    disable_windowed_traceback=False,  # 不禁用错误追踪
    argv_emulation=False,  # 不模拟 argv
    target_arch=None,  # 默认架构
    codesign_identity=None,  # 不签名
    entitlements_file=None,  # 无权限文件
    manifest=_manifest_path,  # ★ DPI 感知 manifest
)

coll = COLLECT(
    exe,  # 打包可执行文件
    a.binaries,  # 收集二进制
    a.zipfiles,  # 收集压缩包
    a.datas,  # 收集数据文件
    strip=False,  # 不裁剪
    upx=True,  # UPX 压缩
    upx_exclude=[],  # 不排除
    name='mouse_move_dist',  # 输出目录名
)
