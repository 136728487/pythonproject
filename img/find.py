import cv2
import numpy as np
import pyautogui

# Step 1: Press 'n' to get a screenshot
pyautogui.press('n')
pyautogui.sleep(1)  # wait for a moment to let the screenshot be taken

# Step 2: Capture screen
screenshot = pyautogui.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Step 3: Find farms and the character in the screenshot
farm_template = cv2.imread('farm.png', cv2.IMREAD_UNCHANGED)
character_template = cv2.imread('character.png', cv2.IMREAD_UNCHANGED)

res_farm = cv2.matchTemplate(screenshot, farm_template, cv2.TM_CCOEFF_NORMED)
res_character = cv2.matchTemplate(screenshot, character_template, cv2.TM_CCOEFF_NORMED)

_, _, _, max_loc_farm = cv2.minMaxLoc(res_farm)
_, _, _, max_loc_character = cv2.minMaxLoc(res_character)

# Step 4: Compute distances between the character and each farm
distances = np.sqrt((max_loc_farm[0]-max_loc_character[0])**2 + (max_loc_farm[1]-max_loc_character[1])**2)

# Step 5: Find the closest farm
closest_farm_index = np.argmin(distances)
closest_farm_location = max_loc_farm[closest_farm_index]

# Step 6: Move character to the closest farm using WASD keys
if closest_farm_location[0] > max_loc_character[0]:  # if the farm is on the right
    pyautogui.keyDown('d')
    pyautogui.sleep(1)  # adjust the sleep time to move the correct distance
    pyautogui.keyUp('d')
elif closest_farm_location[0] < max_loc_character[0]:  # if the farm is on the left
    pyautogui.keyDown('a')
    pyautogui.sleep(1)  # adjust the sleep time to move the correct distance
    pyautogui.keyUp('a')

if closest_farm_location[1] > max_loc_character[1]:  # if the farm is below
    pyautogui.keyDown('s')
    pyautogui.sleep(1)  # adjust the sleep time to move the correct distance
    pyautogui.keyUp('s')
elif closest_farm_location[1] < max_loc_character[1]:  # if the farm is above
    pyautogui.keyDown('w')
    pyautogui.sleep(1)  # adjust the sleep time to move the correct distance
    pyautogui.keyUp('w')