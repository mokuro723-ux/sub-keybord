import subprocess, sys, os

# pyinstallerインストール
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

# launcher.pyを同じフォルダに作成
script_dir = os.path.dirname(os.path.abspath(__file__))
launcher = os.path.join(script_dir, "launcher.py")
with open(launcher, "w", encoding="utf-8") as f:
    f.write('''import subprocess, os, sys
html = os.path.join(os.path.dirname(sys.executable if getattr(sys, "frozen", False) else os.path.abspath(__file__)), "lefthand-device-config.html")
subprocess.Popen(["msedge.exe", html])
''')

ico = os.path.join(script_dir, "knob.ico")
subprocess.check_call([
    sys.executable, "-m", "PyInstaller",
    "--onefile", "--noconsole", "--clean",
    f"--icon={ico}",
    "--name=左手デバイス設定",
    f"--distpath={script_dir}",
    launcher
])

print("\n完了！同じフォルダに「左手デバイス設定.exe」が出来ました。")
print("それを右クリック→タスクバーに固定 してください。")
input("Enterで閉じる")
