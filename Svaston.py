print("""  __                       
 (_      _.  _ _|_  _  ._  
 __) \/ (_| _>  |_ (_) | | """)
print("[1].Penis")
print("[2].Swastika(not avaible)")

choose = input(">>>")
if choose == "1":
    import pyautogui
    import time
    time.sleep(5)
    pyautogui.click(button='right')
    pyautogui.moveTo(963,241)
    pyautogui.click(button='right')
    pyautogui.moveTo(1280,815)
    pyautogui.click(button='right')
    pyautogui.moveTo(335,532)
    pyautogui.click(button='right')
    pyautogui.moveTo(1280,249)
    pyautogui.keyDown('Space')
    pyautogui.click(button='right')
    pyautogui.keyUp('Space')
    pyautogui.PAUSE = 5
    screenshot = pyautogui.screenshot()
    screenshot.save('SvastonScreen.png')
    print("[Penis.minecraft]Succesfully")
if choose == "2":
    print("Not avaible")
