import os, pyautogui, time


def start(lvl):

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

    def make_login_pass():
      file = open("login.txt", 'r')
      login = file.readlines()
      login = [line.rstrip('\n') for line in login]

      file = open("pass.txt", 'r')
      password = file.readlines()
      password = [line.rstrip('\n') for line in password]
      file.close()
      return login, password
    login, password = ['abdusaid.a',
                       'samirabdumalikov', 'aabdurakhmankhanov', 'khurshidabulkasimov', 'agzamkhanovt', 'mukhammadiorazamatov', 'sardorazamatov', 'ikramkhonakbarkhanov', 'atabekovacharos', 'olimzhon.a', 'islambekbatirkhanov', 'zgairatzhanov', 'dadametovikhtiiar', 'buniodzhorabekov', 'dilmurodibaidillaev', 'sanzharbek_irismatov', 'muslimakarimberdieva', 'm_marzhona', 'sunnatmirabzalov', 'mirzhaalov', 'mirazizmirzakarimov', 'dilmurotmirrakhimov', 'mirsakhatovmiraziz', 'azizkhannarkhodzhaev', 'imronsaidimuratov', 'tadzhikhanovk', 'abdukarim.t', 'utkirbektursimetov', 'utabaevbobomurod', 'khaiitmetovoktamzhon', 'nigorakholmatova', 'shamuratovbegzod', 'shamuratova.madina20', 'ermetovdavron'], ['SS12345++',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'Ss123++', 'Ss123++', 'SS12345++', 'Ss123++', 'SS12345++', 'SS12345++', 'Ss123++', 'SS12345++', 'Ss123++', 'SS12345++', 'Ss123++', 'SS12345++', 'Ss123++', 'SS12345++', 'Ss123++', 'SS12345++', 'Ss123++', 'SS12345++', 'Ss123++', 'Ss123++', 'Ss123++', 'SS12345++', 'SS12345++', 'SS12345++', 'SS12345++', 'Ss123++', 'Ss123++', 'Ss123++', 'SS12345++', 'SS12345++', 'SS12345++', 'Ss123++', 'Ss123++']   #make_login_pass()

    os.system("taskkill /f /im  chrome.exe")
    time.sleep(1)
    os.startfile(r'C:\Program Files\Google\Chrome\Application\Chrome.exe')
    time.sleep(0.5)
    pyautogui.PAUSE = (0.75 + (lvl * 0.25))

    pyautogui.hotkey('ctrl', 'n')
    pyautogui.typewrite('https://login.kundelik.kz/logout')
    pyautogui.press('enter')
    time.sleep(2.5 + (lvl * 0.35))
    pyautogui.hotkey('ctrl', 'w')

    for i in range(0, len(login)):
        pyautogui.hotkey('ctrl', 'n')
        pyautogui.typewrite('https://login.kundelik.kz/login')
        pyautogui.press('enter')
        pyautogui.press('f11')
        while pyautogui.locateOnScreen('images/log.png') is None:
            time.sleep(0.25)
        pyautogui.press('tab', presses=10)
        pyautogui.typewrite(login[i])
        pyautogui.press('tab')

        pyautogui.typewrite(password[i])
        pyautogui.press('enter')
        while pyautogui.locateOnScreen('images/loaded.png') is None:
            time.sleep(0.25)
        time.sleep(1.75 + (lvl * 0.35))
        pyautogui.press('tab', presses=12)
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(1)
        tmp = 1
        while pyautogui.locateOnScreen('images/end.png') is None:
            time.sleep(0.25)
            print(tmp)
            tmp+= 1
            if tmp >= 12:
                break
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.hotkey('ctrl', 'n')
        pyautogui.typewrite('https://login.kundelik.kz/logout')
        pyautogui.press('enter')
        time.sleep(1.75 + (lvl * 0.35))
        pyautogui.hotkey('ctrl', 'w')

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
