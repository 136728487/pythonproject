import subprocess

import pyautogui
from PIL import ImageGrab

# 定义应用程序名称和路径
# app_name = "NeteaseMusic.app"

app_path ='C:\Program Files (x86)\aerbien\launcher\AlbionLauncher.exe'

# 打开应用程序
subprocess.Popen(app_path,shell=True)

# 等待3秒钟，以确保应用程序加载完成
pyautogui.sleep(3)

screen_width, screen_height = pyautogui.size()

print(screen_width, screen_height)

screen_shot = ImageGrab.grab()
print(f"Screenshot size: {screen_shot.size}")
print(f"Screenshot mode: {screen_shot.mode}")
screenshot_width, screenshot_height = screen_shot.size
scaling_ratio_X = screen_width / screenshot_width
Scaling_ratio_Y = screen_height / screenshot_height
filename = 'screenshot.png'
screen_shot.save(filename)
print(f"Saved screenshot to {filename}.")

image_path = '/Users/liuchangying/Local/png/update.png'
cancel_image_path = '/Users/liuchangying/Local/png/cancel_button.png'
# 暂停按钮
stop_image = '/Users/liuchangying/Local/png/stop.png'

confidence = 0.5
play_button_region = pyautogui.locateOnScreen(stop_image, 'screenshot.png', confidence=confidence)
print(f"Found the play button! The region is located at: {play_button_region}")
if play_button_region is not None:
    # 获取区域左上角坐标和宽度高度信息
    x, y, w, h = play_button_region
    # 计算中心点坐标
    cx = x + w / 2
    cy = y + h / 2
    # 移动鼠标到中心点位置
    print(cx, cy)
    relay_cx = cx * scaling_ratio_X
    relay_cy = cy * Scaling_ratio_Y
    print(relay_cx, relay_cy)
    pyautogui.moveTo(relay_cx, relay_cy)

    pyautogui.click()
else:
    print("Could not find the play button.")

pyautogui.click(play_button_region)

# # 使用 PyAutoGUI 在屏幕上找到"播放"按钮，并进行点击操作
# play_button = pyautogui.locateCenterOnScreen('/Users/liuchangying/Local/png/MiniPlayerPlayButton.tiff', confidence=0.9, grayscale=True)
#


# 将窗口最大化
# pyautogui.hotkey('command', 'f')