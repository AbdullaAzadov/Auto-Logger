import pygame, sys, ctypes, pyautogui, time
from main import start
from buttons import Button
from start import Start_B

def run():

    TRIGGER = False
    Start = False
    Choosed = int(0)
    low = False
    med = False
    high = False
    back_color = (55, 60, 90)
    pygame.init()

    frame = 0
    per_frame = 0
    fps = pygame.time.Clock()
    icon = pygame.image.load('images/icon.png')
    pygame.display.set_caption('Auto Logger v0.2')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((640, 360), vsync=1)
    screen_box = screen.get_rect()
    button = Button(screen)
    start_button = Start_B(screen)

    com_font = pygame.font.Font('comment.ttf', 14)
    main_font = pygame.font.Font('main.ttf', 24)
    choose_txt = main_font.render('Выберите скорость соединения с интернетом:', True, (155, 155, 185))

    low_txt = com_font.render('* 15-20 минут ', True, (125, 125, 155))
    med_txt = com_font.render('* 12-15 минут', True, (125, 125, 155))
    high_txt = com_font.render('* 10-12 минут', True, (125, 125, 155))

    alert_txt = pygame.font.Font('comment.ttf', 13).render('* Для корректной работы программы, требуется Google Chrome и расширение AdBlock Plus.', True, (125, 125, 155))
    info_txt = pygame.font.Font('comment.ttf', 13).render('* После того как нажмете СТАРТ, начнется процесс авторизации, это может занять несколько минут.', True, (125, 125, 155))
    close_txt = pygame.font.Font('comment.ttf', 13).render('* Если хотите прекратить авторизацию, закройте это окно.', True, (125, 125, 155))


    choose_box = choose_txt.get_rect()
    choose_box.centerx = screen_box.centerx + 5
    choose_box.top = 45

    while TRIGGER != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(back_color)
        fps.tick(30)

        screen.blit(choose_txt, choose_box)

        screen.blit(low_txt, (85, 155))
        screen.blit(med_txt, (275, 155))
        screen.blit(high_txt, (470, 155))

        screen.blit(alert_txt, (15, 300))
        screen.blit(info_txt, (15, 315))
        screen.blit(close_txt, (15, 330))

        Choosed = button.blit(low, med, high)
        if Choosed == 10:
            med = False
            high = False
            low = True
        elif Choosed == 20:
            high = False
            low = False
            med = True
        elif Choosed == 30:
            low = False
            med = False
            high = True

        if Start == True:
            per_frame+= 1

        Choosed = start_button.blit(low, med, high)
        if Choosed == 100:
            Start = True

        frame+= 1
        if Start == True and per_frame == 3:
            TRIGGER = True
        pygame.display.flip()
    if low == True:
        return 3
    if med == True:
        return 2
    if high == True:
        return 1
lvl = run()

def get_layout():
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    if hex(pf(0)) == '0x4090409':
        return 'en'
    else:
        return "another"

if get_layout() != 'en':
    time.sleep(0.5)
    print(pyautogui.alert(text='Переключите язык на английский и перезапустите программу.', title='Обратите внимание !', button='OK'))
    sys.exit()
start(lvl)


