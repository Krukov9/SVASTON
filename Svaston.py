print("""  __                       
 (_      _.  _ _|_  _  ._  
 __) \/ (_| _>  |_ (_) | | """)
print("[1].Построить член")
while 1 == 1:
    choose = input(">>>")
    if choose == "1":
        print("[1].построить один раз")
        print("[2].авто постройка")
        while 1 == 1:
            choose = input(">>>")
            if choose == "1":
            import pyautogui
            import time
            time.sleep(5)
            pyautogui.click(button='right')
            pyautogui.keyDown("D")
            time.sleep(0.25)
            pyautogui.keyUp("D")
            pyautogui.click(button='right')
            time.sleep(0.25)
            pyautogui.keyDown("A")
            time.sleep(0.10)
            pyautogui.keyUp("A")
            pyautogui.click(button='right')
            pyautogui.keyDown("Space")
            time.sleep(0.10)
            pyautogui.keyUp("Space")
            pyautogui.click(button='right')
            pyautogui.keyDown("Space")
            time.sleep(0.10)
            pyautogui.keyUp("Space")
            pyautogui.click(button='right')
            screenshot = pyautogui.screenshot()
            screenshot.save('SvastonScreen.png')
            print("[Penis.minecraft]Succesfully")
