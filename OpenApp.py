import subprocess
import time
import pywinauto

# Requires admin
# 定义应用程序名称和路径
# app_name = "NeteaseMusic.app"

app_path = r'C:\Program Files (x86)\aerbien\launcher\AlbionLauncher.exe'
process = subprocess.Popen(app_path, shell=True)

while not app.window(title='AlbionLauncher'):
    time.sleep(0.5)

time.sleep(5)


app = pywinauto.application.Application()
dlg = app.top_window()

start_btn = dlg.child_window(title="启动", control_type="Button")
start_btn.click()


