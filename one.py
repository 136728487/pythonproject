import subprocess

import pyautogui
from PIL import ImageGrab

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
