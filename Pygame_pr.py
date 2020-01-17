import pygame
import os
from copy import copy

pygame.init()

pygame.mixer.music.load('data\\саундтрек.mp3')
pygame.mixer.music.play(1000000)

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    image.set_colorkey(colorkey)
    return image


screen = pygame.display.set_mode((1500, 900))
clock = pygame.time.Clock()
running = True

bg_group = pygame.sprite.Group()
btn_g1 = pygame.sprite.Group()
btn_g2 = pygame.sprite.Group()
btn_g3 = pygame.sprite.Group()
btn_g4 = pygame.sprite.Group()

play_g1 = pygame.sprite.Group()

place_list = None
tv_list = None
player_index = None
war_list = []

war_g = pygame.sprite.Group()
g_board = pygame.sprite.Group()

def play():
    global running
    global player_index
    global tv_list
    global game_pos
    global kol_players
    global players_list
    global resurs_list
    pos = 'заставка'
    running1 = True

    g1 = pygame.sprite.Group()
    btn_g = pygame.sprite.Group()
    g_rok = pygame.sprite.Group()

    im1 = load_image("заставка(Россия).png")
    im2 = load_image("заставка(США).png")
    im3 = load_image("заставка(Китай).png")
    im4 = load_image("заставка(Германия).png")
    im6 = load_image("цель.png", (255, 255, 255))
    im7 = load_image('победа России.png')
    im8 = load_image('победа США.png')
    im9 = load_image('победа Китая.png')
    im10 = load_image('победа Германии.png')

    sl = {'Россия': '5', 'США': '6', 'Китай': '7', 'Германия': '8'}

    btn_ok = Button(g1, (625, 700, 250, 100), 'начать', 60, (0, 0, 0))
    btn_next = Button(btn_g, (1340, 785, 150, 80), 'закончить ход', 25, (0, 0, 0))
    rockets = Rockets(g_rok)
    rok_target = Rocket_target(g_rok)

    u = False
    d = False
    r = False
    l = False
    choose_list = [False, False, False, False, False, False, False, False]
    move_unit = (False, None, None)
    orb_udar_f = False

    n = 0

    BMP('Россия', 27, 27, board, 15, 2)

    while running1:
        n += 1
        if n == 5:
            n = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_pos = 'Меню'
                running1 = False
                btn_ru.lock = False
                btn_us.lock = False
                btn_ch.lock = False
                btn_ge.lock = False
                if karta == 1:
                    file = open('data\\карта 1(сохраненная).txt', mode='w')
                    for i in place_list:
                        file.write(', '.join(i) + '\n')
                    file.close()
                    file = open('data\\карта 1(основные данные).txt', mode='w')
                    file.write(str(player_index) + '\n' + str(kol_players) + '\n' + \
                               ', '.join(players_list) + '\n' + ', '.join([str(i) for i in resurs_list]))
                    file.close()
                    file = open('data\\карта 1(войска).txt', mode='w')
                    list2 = []
                    for i in war_list:
                        if type(i) == Pehota:
                            list2.append('Pehota ' + i.con + ' ' + str(i.x) + ' ' + str(i.y) + ' ' + str(i.health) \
                                         + ' ' + str(i.hods))
                        elif type(i) == BMP:
                            list2.append('BMP ' + i.con + ' ' + str(i.x) + ' ' + str(i.y) + ' ' + str(i.health)  + ' '\
                                         + str(i.hods))
                        elif type(i) == Rathvedchik:
                            list2.append('Rathvedchik ' + i.con + ' ' + str(i.x) + ' ' + str(i.y) + ' ' \
                                         + str(i.health) + ' ' + str(i.hods))
                        elif type(i) == Granatomet:
                            list2.append('Granatomet ' + i.con + ' ' + str(i.x) + ' ' + str(i.y) + ' ' + \
                                         str(i.health) + ' ' + str(i.hods))
                        elif type(i) == Tank:
                            list2.append('Tank ' + i.con + ' ' + str(i.x) + ' ' + str(i.y) + ' ' + str(i.health) + ' '\
                                         + str(i.hods))
                    file.write('\n'.join(list2))
                    file.close()
                elif karta == 2:
                    file = open('data\\карта 2(сохраненная).txt', mode='w')
                    for i in place_list:
                        file.write(', '.join(i) + '\n')
                    file.close()
                    file = open('data\\карта 2(основные данные).txt', mode='w')
                    file.write(str(player_index) + '\n' + str(kol_players) + '\n' + \
                               ', '.join(players_list) + '\n' + ', '.join([str(i) for i in resurs_list]))
                    file.close()
                    file = open('data\\карта 2(войска).txt', mode='w')
                    list2 = []
                    for i in war_list:
                        if type(i) == Pehota:
                            list2.append('Pehota ' + i.con + ' ' + str(i.x) + ' ' + str(i.y) + ' ' + str(i.health) \
                                         + ' ' + str(i.hods))
                        elif type(i) == BMP:
                            list2.append('BMP ' + i.con + ' ' + str(i.x) + ' ' + str(i.y) + ' ' + str(i.health) \
                                         + ' ' + str(i.hods))
                        elif type(i) == Rathvedchik:
                            list2.append('Rathvedchik ' + i.con + ' ' + str(i.x) + ' ' + str(i.y) + ' ' \
                                         + str(i.health) + ' ' + str(i.hods))
                        elif type(i) == Granatomet:
                            list2.append('Granatomet ' + i.con + ' ' + str(i.x) + ' ' + str(i.y) + ' ' + str(i.health) \
                                         + ' ' + str(i.hods))
                        elif type(i) == Tank:
                            list2.append('Tank ' + i.con + ' ' + str(i.x) + ' ' + str(i.y) + ' ' + str(i.health) + ' ' \
                                         + str(i.hods))
                    file.write('\n'.join(list2))
                    file.close()
            elif event.type == pygame.MOUSEMOTION:
                if pos == 'заставка':
                    g1.update(event.pos[0], event.pos[1])
                elif pos == 'игровое поле':
                    btn_g.update(event.pos[0], event.pos[1])
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if pos == 'заставка':
                    if btn_ok.click(event.pos[0], event.pos[1]):
                        pos = 'игровое поле'
                        board.open()
                        board.redraw()
                        if player_index == 0 and players_list[player_index] != 'Нет':
                            board.rect.x = 0
                            board.rect.y = 0
                            for i in war_list:
                                i.set_pos()
                        elif player_index == 1 and players_list[player_index] != 'Нет':
                            board.rect.x = -3000
                            board.rect.y = -3750
                            for i in war_list:
                                i.set_pos()
                        elif player_index == 2 and players_list[player_index] != 'Нет':
                            board.rect.x = 0
                            board.rect.y = -3750
                            for i in war_list:
                                i.set_pos()
                        elif player_index == 3 and players_list[player_index] != 'Нет':
                            board.rect.x = -3000
                            board.rect.y = 0
                            for i in war_list:
                                i.set_pos()
                        im5 = load_image('панель управления.png')
                        for i in war_list:
                            if i.con == players_list[player_index]:
                                i.update_health(1)
                                i.update_dam()
                elif pos == 'игровое поле':
                    map_x = event.pos[0] // 150 - board.rect.x // 150
                    map_y = event.pos[1] // 150 - board.rect.y // 150
                    try:
                        if btn_next.click(event.pos[0], event.pos[1]) and not orb_udar_f:
                            for i in war_list:
                                if i.con == players_list[player_index]:
                                    i.hods = i.max_hods
                            s = [j for i in place_list for j in i]
                            resurs_list[player_index] += s.count(sl[players_list[player_index]]) * 10
                            s = None
                            if player_index + 1 != len(players_list):
                                player_index += 1
                            else:
                                player_index = 0
                            while players_list[player_index] == 'Нет':
                                if player_index + 1 != len(players_list):
                                    player_index += 1
                                else:
                                    player_index = 0
                            tv_list = [['0' for i in range(30)] for j in range(30)]
                            choose_list = [False, False, False, False, False, False, False, False]
                            move_unit = (False, None, None, None)
                            pos = 'заставка'
                        elif event.pos[0] > 13 and event.pos[1] > 798 and event.pos[0] < 87 and event.pos[1] < 863 and \
                                not move_unit[0] and resurs_list[player_index] > 9:
                            if choose_list[0]:
                                choose_list[0] = False
                            elif not choose_list[0] and not True in choose_list and not orb_udar_f:
                                choose_list[0] = True
                        elif event.pos[0] > 94 and event.pos[1] > 793 and event.pos[0] < 263 and event.pos[1] < 870 \
                                and not move_unit[0] and resurs_list[player_index] > 19:
                            if choose_list[1]:
                                choose_list[1] = False
                            elif not choose_list[1] and not True in choose_list and not orb_udar_f:
                                choose_list[1] = True
                        elif event.pos[0] > 274 and event.pos[1] > 803 and event.pos[0] < 371 and event.pos[1] < 875 \
                                and not move_unit[0] and resurs_list[player_index] > 19:
                            if choose_list[2]:
                                choose_list[2] = False
                            elif not choose_list[2] and not True in choose_list and not orb_udar_f:
                                choose_list[2] = True
                        elif event.pos[0] > 398 and event.pos[1] > 806 and event.pos[0] < 463 and event.pos[1] < 873 \
                                and not move_unit[0] and resurs_list[player_index] > 29:
                            if choose_list[3]:
                                choose_list[3] = False
                            elif not choose_list[3] and not True in choose_list and not orb_udar_f:
                                choose_list[3] = True
                        elif event.pos[0] > 481 and event.pos[1] > 804 and event.pos[0] < 692 and event.pos[1] < 872 \
                                and not move_unit[0] and resurs_list[player_index] > 49:
                            if choose_list[4]:
                                choose_list[4] = False
                            elif not choose_list[4] and not True in choose_list and not orb_udar_f:
                                choose_list[4] = True
                        elif event.pos[0] > 1242 and event.pos[1] > 755 and event.pos[0] < 1325 and event.pos[1] < 871 \
                                and not move_unit[0] and resurs_list[player_index] > 59:
                            if choose_list[7]:
                                choose_list[7] = False
                            elif not choose_list[7] and not True in choose_list and not orb_udar_f:
                                choose_list[7] = True
                        if event.pos[1] > 750:
                            pass
                        elif not True in choose_list and True in [i.pos_check(map_x, map_y) for i in war_list] and \
                                [players_list[player_index]] == \
                                [i.con for i in war_list if i.x == map_x and i.y == map_y] and \
                                [i for i in war_list if i.pos_check(map_x, map_y)][0].hods > 0 and not orb_udar_f:
                            if move_unit == (True, map_x, map_y):
                                move_unit = (False, None, None)
                            elif move_unit:
                                move_unit = (True, copy(map_x), copy(map_y))
                        elif place_list[map_y][map_x] == sl[players_list[player_index]] and choose_list[0] and \
                                not True in [i.pos_check(map_x, map_y) for i in war_list]:
                            resurs_list[player_index] -= 10
                            Pehota(war_g, players_list[player_index], map_x, map_y, board, 10, 0)
                            choose_list[0] = False
                        elif place_list[map_y][map_x] == sl[players_list[player_index]] and choose_list[1] and \
                                not True in [i.pos_check(map_x, map_y) for i in war_list]:
                            resurs_list[player_index] -= 20
                            BMP(players_list[player_index], map_x, map_y, board, 15, 0)
                            choose_list[1] = False
                        elif place_list[map_y][map_x] == sl[players_list[player_index]] and choose_list[2] and \
                                not True in [i.pos_check(map_x, map_y) for i in war_list]:
                            resurs_list[player_index] -= 20
                            Rathvedchik(players_list[player_index], map_x, map_y, board, 10, 0)
                            board.open()
                            board.redraw()
                            choose_list[2] = False
                        elif place_list[map_y][map_x] == sl[players_list[player_index]] and choose_list[3] and \
                                not True in [i.pos_check(map_x, map_y) for i in war_list]:
                            resurs_list[player_index] -= 30
                            Granatomet(players_list[player_index], map_x, map_y, board, 10, 0)
                            choose_list[3] = False
                        elif place_list[map_y][map_x] == sl[players_list[player_index]] and choose_list[4] and \
                                not True in [i.pos_check(map_x, map_y) for i in war_list]:
                            resurs_list[player_index] -= 50
                            Tank(players_list[player_index], map_x, map_y, board, 25, 0)
                            choose_list[4] = False
                        elif move_unit[0] and not orb_udar_f:
                            for i in war_list:
                                if i.pos_check(move_unit[1], move_unit[2]) and \
                                        abs(map_x - move_unit[1]) < 2 and abs(map_y - move_unit[2]) < 2:
                                    i.attack(map_x, map_y)
                                    move_unit = (False, None, None)
                        elif choose_list[7] and True in [i.pos_check(map_x, map_y) for i in war_list \
                                                         if i.con != players_list[player_index] and \
                                                            tv_list[map_y][map_x] == '1']:
                            rockets.set_target(map_x, map_y)
                            rockets.set_pos(map_x * 150 + board.rect.x, (map_y - 8) * 150 + board.rect.y)
                            rok_target.set_pos(map_x * 150 + board.rect.x, (map_y) * 150 + board.rect.y + 140)
                            choose_list[7] = False
                            orb_udar_f = True
                            rockets.image = rockets.im
                            resurs_list[player_index] -= 60
                    except IndexError:
                        pass
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    u = True
                elif event.key == pygame.K_s:
                    d = True
                elif event.key == pygame.K_a:
                    l = True
                elif event.key == pygame.K_d:
                    r = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    u = False
                elif event.key == pygame.K_s:
                    d = False
                elif event.key == pygame.K_a:
                    l = False
                elif event.key == pygame.K_d:
                    r = False
                elif event.key == pygame.K_c:
                    if move_unit[0] and [i for i in war_list if i.pos_check(move_unit[1], move_unit[2])][0].hods > 0 \
                            and type([i for i in war_list if i.pos_check(move_unit[1], move_unit[2])][0]) \
                            != Rathvedchik:
                        list1 = [str(i) for i in range(4, 9)]
                        list1.remove(sl[players_list[player_index]])
                        if place_list[move_unit[2]][move_unit[1]] in list1:
                            place_list[move_unit[2]][move_unit[1]] = sl[players_list[player_index]]
                            board.redraw()
                            [i for i in war_list if i.pos_check(move_unit[1], move_unit[2])][0].hods = 0
                            list3 = [j for i in place_list for j in i]
                            if 'Россия' in players_list and not '5' in list3:
                                players_list[players_list.index('Россия')] = 'Нет'
                            elif 'США' in players_list and not '6' in list3:
                                players_list[players_list.index('США')] = 'Нет'
                            elif 'Китай' in players_list and not '7' in list3:
                                players_list[players_list.index('Китай')] = 'Нет'
                            elif 'Германия' in players_list and not '8' in list3:
                                players_list[players_list.index('Германия')] = 'Нет'
                        move_unit = (False, None, None)
                        if 'Россия' in players_list and players_list.count('Нет') == len(players_list) - 1:
                            pos = 'победа России'
                        elif 'США' in players_list and players_list.count('Нет') == len(players_list) - 1:
                            pos = 'победа США'
                        elif 'Китай' in players_list and players_list.count('Нет') == len(players_list) - 1:
                            pos = 'победа Китая'
                        elif 'Германия' in players_list and players_list.count('Нет') == len(players_list) - 1:
                            pos = 'победа Германии'
        if pos == 'заставка':
            if players_list[player_index] == 'Россия':
                screen.blit(im1, (0, 0))
            elif players_list[player_index] == 'США':
                screen.blit(im2, (0, 0))
            elif players_list[player_index] == 'Китай':
                screen.blit(im3, (0, 0))
            else:
                screen.blit(im4, (0, 0))
            font = pygame.font.Font(None, 65)
            text = font.render(str(player_index + 1), 1, (0, 0, 0))
            screen.blit(text, (815, 91))
            g1.draw(screen)
        elif pos == 'игровое поле':
            if u and board.rect.y != 0 and n == 0:
                board.move_up()
                for i in war_list:
                    i.map_move_up()
                rockets.map_move_up()
                rok_target.map_move_up()
            if d and board.rect.y != -3750 and n == 0:
                board.move_down()
                for i in war_list:
                    i.map_move_down()
                rockets.map_move_down()
                rok_target.map_move_down()
            if l and board.rect.x != 0 and n == 0:
                board.move_left()
                for i in war_list:
                    i.map_move_left()
                rockets.map_move_left()
                rok_target.map_move_left()
            if r and board.rect.x != -3000 and n == 0:
                board.move_right()
                for i in war_list:
                    i.map_move_right()
                rockets.map_move_right()
                rok_target.map_move_right()
            g_board.draw(screen)
            if True in choose_list[:7]:
                for i in range(30):
                    for j in range(30):
                        if place_list[i][j] == sl[players_list[player_index]]:
                            pygame.draw.rect(screen, (255, 0, 0),
                                             (j * 150 + board.rect.x, i * 150 + board.rect.y, 150, 150), 2)
            for i in war_list:
                a = i.x * 150 + board.rect.x
                b = i.y * 150 + board.rect.y
                if i.con == players_list[player_index] or i.con != players_list[player_index] \
                        and tv_list[i.y][i.x] == '1':
                    screen.blit(i.image, (a, b))
                    if i.hods == 0:
                        pygame.draw.line(screen, (255, 0, 0), (a + 110, b + 134), (a + 120, b + 144), 2)
                        pygame.draw.line(screen, (255, 0, 0), (a + 120, b + 134), (a + 110, b + 144), 2)
                    else:
                        pygame.draw.line(screen, (0, 0, 0), (a + 110, b + 134), (a + 120, b + 144), 2)
                        pygame.draw.line(screen, (0, 0, 0), (a + 120, b + 134), (a + 110, b + 144), 2)
                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i.health), 1, (250, 250, 250))
                    screen.blit(text, (a + 124, b + 131))
            if orb_udar_f:
                g_rok.draw(screen)
                if not rockets.update_image(rok_target, n):
                    rockets.self_move()
                elif rockets.f and n == 0:
                    orb_udar_f = False
            for i in war_list:
                if move_unit[0] and i.pos_check(move_unit[1], move_unit[2]):
                    pygame.draw.rect(screen, (255, 255, 0), (move_unit[1] * 150 + board.rect.x,
                                                             move_unit[2] * 150 + board.rect.y, 150, 150), 2)
                    if i.at_range == 1:
                        for y in range(3):
                            for x in range(3):
                                a = 150 * (x + move_unit[1]) - 150
                                b = 150 * (y + move_unit[2]) - 150
                                if a > -1 and b > -1 and a < 4500 and b < 4500 and \
                                        True in [j.pos_check(a // 150, b // 150) for j in war_list] and \
                                        [j for j in war_list if j.pos_check(a // 150, b // 150)][0].con \
                                        != players_list[player_index]:
                                    screen.blit(im6, (a + board.rect.x, b + board.rect.y))
                    list1 = [str(i) for i in range(4, 9)]
                    list1.remove(sl[players_list[player_index]])
                    if place_list[move_unit[2]][move_unit[1]] in list1 and \
                            type(i) != Rathvedchik:
                        font = pygame.font.Font(None, 80)
                        text = font.render('c', 1, (250, 250, 0))
                        screen.blit(text,
                                    (move_unit[1] * 150 + board.rect.x + 60, move_unit[2] * 150 + board.rect.y + 5))
                elif choose_list[7]:
                    if i.con != players_list[player_index] and tv_list[i.y][i.x] == '1':
                        screen.blit(im6, (i.x * 150 + board.rect.x, i.y * 150 + board.rect.y))

            screen.blit(im5, (0, 750))
            btn_g.draw(screen)
            font = pygame.font.Font(None, 35)
            text = font.render(str(resurs_list[player_index]), 1, (255, 255, 0))
            screen.blit(text, (135, 761))
            if choose_list[0]:
                pygame.draw.rect(screen, (0, 200, 0), (13, 798, 74, 65), 1)
            elif choose_list[1]:
                pygame.draw.rect(screen, (0, 200, 0), (94, 793, 169, 77), 1)
            elif choose_list[2]:
                pygame.draw.rect(screen, (0, 200, 0), (274, 803, 97, 72), 1)
            elif choose_list[3]:
                pygame.draw.rect(screen, (0, 200, 0), (398, 806, 65, 67), 1)
            elif choose_list[3]:
                pygame.draw.rect(screen, (0, 200, 0), (398, 806, 65, 67), 1)
            elif choose_list[4]:
                pygame.draw.rect(screen, (0, 200, 0), (481, 804, 211, 68), 1)
            elif choose_list[7]:
                pygame.draw.rect(screen, (0, 200, 0), (1242, 755, 83, 116), 1)
        elif pos == 'победа России':
            screen.blit(im7, (0, 0))
        elif pos == 'победа США':
            screen.blit(im8, (0, 0))
        elif pos == 'победа Китая':
            screen.blit(im9, (0, 0))
        elif pos == 'победа Германии':
            screen.blit(im10, (0, 0))
        if not running1:
            kol_players = None
            players_list = []
        pygame.display.flip()
        clock.tick(60)


class Bg(pygame.sprite.Sprite):
    image1 = load_image('Bg.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Bg_airplane(pygame.sprite.Sprite):
    image1 = load_image('bg_airplane.png', (255, 255, 255))

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Bg_airplane.image1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Button(pygame.sprite.Sprite):
    def __init__(self, group, rect, text, font, color):
        super().__init__(group)
        self.im1 = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
        font = pygame.font.Font(None, font)
        text1 = font.render(text, 1, color)
        pygame.draw.rect(self.im1, (100, 100, 100), (0, 0, rect[2], rect[3]))
        pygame.draw.rect(self.im1, (0, 0, 0), (5, 5, rect[2] - 10, rect[3] - 10), 5)
        self.im1.blit(text1, ((rect[2] - text1.get_width()) // 2, (rect[3] - text1.get_height()) // 2))

        self.im2 = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
        text1 = font.render(text, 1, (255, 255, 0))
        pygame.draw.rect(self.im2, (100, 100, 100), (0, 0, rect[2], rect[3]))
        pygame.draw.rect(self.im2, (255, 255, 0), (5, 5, rect[2] - 10, rect[3] - 10), 5)
        self.im2.blit(text1, ((rect[2] - text1.get_width()) // 2, (rect[3] - text1.get_height()) // 2))

        self.im3 = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
        text1 = font.render(text, 1, (255, 0, 0))
        pygame.draw.rect(self.im3, (100, 100, 100), (0, 0, rect[2], rect[3]))
        pygame.draw.rect(self.im3, (255, 0, 0), (5, 5, rect[2] - 10, rect[3] - 10), 5)
        self.im3.blit(text1, ((rect[2] - text1.get_width()) // 2, (rect[3] - text1.get_height()) // 2))

        self.image = self.im1
        self.rect = pygame.Rect(0, 0, rect[2], rect[3])
        self.rect.x = rect[0]
        self.rect.y = rect[1]

        self.lock = False

    def update(self, x, y):
        if not self.lock:
            if x > self.rect.x and y > self.rect.y and x < self.rect.x + self.rect[2] \
                    and y < self.rect.y + self.rect[3]:
                self.image = self.im2
            else:
                self.image = self.im1
        else:
            self.image = self.im3

    def click(self, x, y):
        if not self.lock:
            if x > self.rect.x and y > self.rect.y and x < self.rect.x + self.rect[2] \
                    and y < self.rect.y + self.rect[3]:
                self.image = self.im1
                return True
            else:
                return False


class Board(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.im_pole_tv = load_image("поле(тв).png")
        self.im_les_tv = load_image("лес(тв).png")
        self.im_gore_tv = load_image("горы(тв).png")
        self.im_voda_tv = load_image("вода(тв).png")
        self.im_ploshadka_tv = load_image("площадка(тв).png")
        self.im_pole = load_image("поле.png")
        self.im_les = load_image("лес.png")
        self.im_gore = load_image("горы.png")
        self.im_voda = load_image("вода.png")
        self.im_ploshadka = load_image("площадка.png")
        self.im_batha_ru = load_image("база(Россия).png")
        self.im_batha_us = load_image("база(США).png")
        self.im_batha_ch = load_image("база(Китай).png")
        self.im_batha_ge = load_image("база(Германия).png")

        sl = {'Россия': '5', 'США': '6', 'Китай': '7', 'Германия': '8'}
        for i in players_list:
            if i != 'Нет':
                if players_list.index(i) == 0:
                    place_list[1][1] = sl[i]
                elif players_list.index(i) == 1:
                    place_list[28][28] = sl[i]
                elif players_list.index(i) == 2:
                    place_list[28][1] = sl[i]
                elif players_list.index(i) == 3:
                    place_list[1][28] = sl[i]

        self.redraw()
        self.rect = pygame.Rect(0, 0, 4500, 4500)
        self.rect.x = 0
        self.rect.y = 0

    def move_down(self):
        self.rect.y -= 150

    def move_up(self):
        self.rect.y += 150

    def move_left(self):
        self.rect.x += 150

    def move_right(self):
        self.rect.x -= 150

    def open(self):
        sl = {'Россия': '5', 'США': '6', 'Китай': '7', 'Германия': '8'}
        for i in range(30):
            for j in range(30):
                tv_list[i][j] = '0'
        for i in range(30):
            for j in range(30):
                if place_list[i][j] == sl[players_list[player_index]]:
                    for y in range(3):
                        for x in range(3):
                            tv_list[y + (i - 1)][x + (j - 1)] = '1'

        for i in war_list:
            if i.con == players_list[player_index] and i.at_range == 1:
                for y in range(3):
                    for x in range(3):
                        if y + (i.y - 1) > -1 and x + (i.x - 1) > -1 and y + (i.y - 3) < 30 and x + (i.x - 3) < 30:
                            tv_list[y + (i.y - 1)][x + (i.x - 1)] = '1'
            elif i.con == players_list[player_index] and i.at_range == 3:
                for y in range(7):
                    for x in range(7):
                        if y + (i.y - 3) > -1 and x + (i.x - 3) > -1 and y + (i.y - 3) < 30 and x + (i.x - 3) < 30:
                            tv_list[y + (i.y - 3)][x + (i.x - 3)] = '1'

    def redraw(self):
        im = pygame.Surface((4800, 4800), pygame.SRCALPHA)
        for i in range(30):
            for j in range(30):
                if place_list[i][j] == '0':
                    if tv_list[i][j] == '0':
                        im.blit(self.im_pole_tv, (j * 150, i * 150))
                    else:
                        im.blit(self.im_pole, (j * 150, i * 150))
                elif place_list[i][j] == '1':
                    if tv_list[i][j] == '0':
                        im.blit(self.im_les_tv, (j * 150, i * 150))
                    else:
                        im.blit(self.im_les, (j * 150, i * 150))
                elif place_list[i][j] == '2':
                    if tv_list[i][j] == '0':
                        im.blit(self.im_gore_tv, (j * 150, i * 150))
                    else:
                        im.blit(self.im_gore, (j * 150, i * 150))
                elif place_list[i][j] == '3':
                    if tv_list[i][j] == '0':
                        im.blit(self.im_voda_tv, (j * 150, i * 150))
                    else:
                        im.blit(self.im_voda, (j * 150, i * 150))
                elif place_list[i][j] == '4':
                    if tv_list[i][j] == '0':
                        im.blit(self.im_ploshadka_tv, (j * 150, i * 150))
                    else:
                        im.blit(self.im_ploshadka, (j * 150, i * 150))
                elif place_list[i][j] == '5':
                    if tv_list[i][j] == '0':
                        im.blit(self.im_ploshadka_tv, (j * 150, i * 150))
                    else:
                        im.blit(self.im_batha_ru, (j * 150, i * 150))
                elif place_list[i][j] == '6':
                    if tv_list[i][j] == '0':
                        im.blit(self.im_ploshadka_tv, (j * 150, i * 150))
                    else:
                        im.blit(self.im_batha_us, (j * 150, i * 150))
                elif place_list[i][j] == '7':
                    if tv_list[i][j] == '0':
                        im.blit(self.im_ploshadka_tv, (j * 150, i * 150))
                    else:
                        im.blit(self.im_batha_ch, (j * 150, i * 150))
                elif place_list[i][j] == '8':
                    if tv_list[i][j] == '0':
                        im.blit(self.im_ploshadka_tv, (j * 150, i * 150))
                    else:
                        im.blit(self.im_batha_ge, (j * 150, i * 150))
        self.image = im


class Pehota(pygame.sprite.Sprite):
    im = load_image('пехота(Россия).png', (255, 255, 255))
    im1 = load_image('пехота(США).png', (255, 255, 255))
    im2 = load_image('пехота(Китай).png', (255, 255, 255))
    im3 = load_image('пехота(Германия).png', (255, 255, 255))

    def __init__(self, group, con, x, y, pl, h, hods):
        super().__init__(group)
        self.pl = pl
        self.con = con
        self.health = h
        self.dam = 2
        self.defense = 1
        self.at_range = 1
        self.hods = hods
        self.max_hods = 1
        self.can_move = ['0', '1', '4', '5', '6', '7', '8']
        self.type = 'пехота'
        self.x = x
        self.y = y

        if con == 'Россия':
            self.image = self.im
        if con == 'США':
            self.image = self.im1
        if con == 'Китай':
            self.image = self.im2
        if con == 'Германия':
            self.image = self.im3
        self.rect = pygame.Rect(0, 0, 150, 150)
        self.rect.x = x * 150 + pl.rect.x
        self.rect.y = y * 150 + pl.rect.y
        war_list.append(self)

    def map_move_down(self):
        self.rect.y -= 150

    def map_move_up(self):
        self.rect.y += 150

    def map_move_left(self):
        self.rect.x += 150

    def map_move_right(self):
        self.rect.x -= 150

    def set_pos(self):
        self.rect.x = self.x * 150 + self.pl.rect.x
        self.rect.y = self.y * 150 + self.pl.rect.y

    def pos_check(self, x1, y1):
        if self.x == x1 and self.y == y1:
            return True
        else:
            return False

    def move_to(self, x1, y1):
        if self.hods != 0 and place_list[y1][x1] in self.can_move and \
                not True in [i.pos_check(x1, y1) for i in war_list]:
            if x1 > self.x:
                self.x += 1
                self.rect.x += 150
            elif x1 < self.x:
                self.x -= 1
                self.rect.x -= 150
            if y1 > self.y:
                self.y += 1
                self.rect.y += 150
            elif y1 < self.y:
                self.y -= 1
                self.rect.y -= 150
            self.pl.open()
            self.pl.redraw()
            self.hods -= 1

    def update_dam(self):
        if self.health > 5:
            self.dam = 2
            self.defense = 1
        elif self.health > 2:
            self.dam = 1
            self.defense = 1
        else:
            self.dam = 0
            self.defense = 0

    def update_health(self, n):
        if self.health + n > 10:
            self.health = 10
        else:
            self.health += n

    def attack(self, x1, y1):
        if self.hods > 0 and True in [i.pos_check(x1, y1) for i in war_list if i.con != players_list[player_index]]:
            un = [i for i in war_list if i.pos_check(x1, y1)][0]
            if un.type == 'пехота':
                un.health -= self.dam * 2
            else:
                un.health -= self.dam
            if place_list[un.y][un.x] == '1' and un.health < 10:
                if self.dam > 0:
                    un.health += 1
            if un.health < 1:
                war_list.remove(un)
                self.hods = 1
            else:
                if type(un) == Pehota:
                    self.health -= un.defense * 2
                elif type(un) == Rathvedchik:
                    pass
                else:
                    self.health -= un.defense
                if place_list[self.y][self.x] == '1' and self.health < 10:
                    if un.dam > 0:
                        self.health += 1
                self.hods = 0
                if self.health < 1:
                    war_list.remove(self)
        self.move_to(x1, y1)


class BMP(Pehota):
    im = load_image('бмп(Россия).png', (255, 255, 255))
    im1 = load_image('бмп(США).png', (255, 255, 255))
    im2 = load_image('бмп(Китай).png', (255, 255, 255))
    im3 = load_image('бмп(Германия).png', (255, 255, 255))

    def __init__(self, con, x, y, pl, h, hods):
        self.pl = pl
        self.con = con
        self.health = h
        self.dam = 3
        self.defense = 2
        self.at_range = 1
        self.hods = hods
        self.max_hods = 2
        self.can_move = ['0', '3', '4', '5', '6', '7', '8']
        self.type = 'легкая бронетехника'
        self.x = x
        self.y = y

        if con == 'Россия':
            self.image = self.im
        if con == 'США':
            self.image = self.im1
        if con == 'Китай':
            self.image = self.im2
        if con == 'Германия':
            self.image = self.im3
        self.rect = pygame.Rect(0, 0, 150, 150)
        self.rect.x = x * 150 + pl.rect.x
        self.rect.y = y * 150 + pl.rect.y
        war_list.append(self)

    def update_dam(self):
        if self.health > 7:
            self.dam = 3
            self.defense = 2
        elif self.health > 2:
            self.dam = 2
            self.defense = 1
        else:
            self.dam = 1
            self.defense = 0

    def attack(self, x1, y1):
        if self.hods > 0 and True in [i.pos_check(x1, y1) for i in war_list]:
            un = [i for i in war_list if i.pos_check(x1, y1)][0]
            if un.type == 'легкая бронетехника':
                un.health -= self.dam * 2
            else:
                un.health -= self.dam
                if place_list[un.y][un.x] == '1' and un.health < 10:
                    un.health += 1
            if un.health < 1:
                war_list.remove(un)
                self.hods = 1
            else:
                if un.type == 'легкая бронетехника':
                    self.health -= un.defense * 2
                elif type(un) == Tank:
                    self.health -= un.defense * 3
                elif type(un) == Granatomet:
                    self.health -= un.defense * 4
                elif type(un) == Rathvedchik:
                    pass
                else:
                    self.health -= un.defense
                un.update_dam()
                self.hods = 0
                if self.health < 1:
                    war_list.remove(self)
        self.move_to(x1, y1)

    def update_health(self, n):
        pass


class Rathvedchik(Pehota):
    im = load_image('разведчик(Россия).png', (255, 255, 255))
    im1 = load_image('разведчик(США).png', (255, 255, 255))
    im2 = load_image('разведчик(Китай).png', (255, 255, 255))
    im3 = load_image('разведчик(Германия).png', (255, 255, 255))

    def __init__(self, con, x, y, pl, h, hods):
        self.pl = pl
        self.con = con
        self.health = h
        self.at_range = 3
        self.hods = hods
        self.max_hods = 3
        self.can_move = [str(i) for i in range(9)]
        self.type = 'авиация'
        self.x = x
        self.y = y

        if con == 'Россия':
            self.image = self.im
        if con == 'США':
            self.image = self.im1
        if con == 'Китай':
            self.image = self.im2
        if con == 'Германия':
            self.image = self.im3
        self.rect = pygame.Rect(0, 0, 150, 150)
        self.rect.x = x * 150 + pl.rect.x
        self.rect.y = y * 150 + pl.rect.y
        war_list.append(self)

    def update_health(self, n):
        pass

    def attack(self, x1, y1):
        self.move_to(x1, y1)


class Granatomet(Pehota):
    im = load_image('гранатометчики(Россия).png', (255, 255, 255))
    im1 = load_image('гранатометчики(США).png', (255, 255, 255))
    im2 = load_image('гранатометчики(Китай).png', (255, 255, 255))
    im3 = load_image('гранатометчики(Германия).png', (255, 255, 255))

    def __init__(self, con, x, y, pl, h, hods):
        self.pl = pl
        self.con = con
        self.health = h
        self.dam = 4
        self.defense = 1
        self.at_range = 1
        self.hods = hods
        self.max_hods = 1
        self.can_move = ['0', '1', '4', '5', '6', '7', '8']
        self.type = 'пехота'
        self.x = x
        self.y = y

        if con == 'Россия':
            self.image = self.im
        if con == 'США':
            self.image = self.im1
        if con == 'Китай':
            self.image = self.im2
        if con == 'Германия':
            self.image = self.im3
        self.rect = pygame.Rect(0, 0, 150, 150)
        self.rect.x = x * 150 + pl.rect.x
        self.rect.y = y * 150 + pl.rect.y
        war_list.append(self)

    def update_dam(self):
        if self.health > 5:
            self.dam = 4
            self.defense = 1
        elif self.health > 2:
            self.dam = 2
            self.defense = 1
        else:
            self.dam = 1
            self.defense = 0

    def update_health(self, n):
        if self.health + n > 10:
            self.health = 10
        else:
            self.health += n

    def attack(self, x1, y1):
        if self.hods > 0 and True in [i.pos_check(x1, y1) for i in war_list]:
            un = [i for i in war_list if i.pos_check(x1, y1)][0]
            if un.type == 'легкая бронетехника':
                un.health -= self.dam * 3
            elif un.type == Tank:
                un.health -= self.dam * 2
            else:
                un.health -= self.dam
            if place_list[un.y][un.x] == '1' and un.health < 10:
                if self.dam > 0:
                    un.health += 1
            if un.health < 1:
                war_list.remove(un)
                self.hods = 1
            else:
                if un.type == 'пехота':
                    self.health -= un.defense * 2
                elif type(un) == Rathvedchik:
                    pass
                else:
                    self.health -= un.defense
                if place_list[self.y][self.x] == '1' and self.health < 10:
                    if un.dam > 0:
                        self.health += 1
                self.hods = 0
                if self.health < 1:
                    war_list.remove(self)
        self.move_to(x1, y1)


class Tank(Pehota):
    im = load_image('танк(Россия).png', (255, 255, 255))
    im1 = load_image('танк(США).png', (255, 255, 255))
    im2 = load_image('танк(Китай).png', (255, 255, 255))
    im3 = load_image('танк(Германия).png', (255, 255, 255))

    def __init__(self, con, x, y, pl, h, hods):
        self.pl = pl
        self.con = con
        self.health = h
        self.dam = 4
        self.defense = 3
        self.at_range = 1
        self.hods = hods
        self.max_hods = 1
        self.can_move = ['0', '4', '5', '6', '7', '8']
        self.type = 'тяжелая бронетехника'
        self.x = x
        self.y = y

        if con == 'Россия':
            self.image = self.im
        if con == 'США':
            self.image = self.im1
        if con == 'Китай':
            self.image = self.im2
        if con == 'Германия':
            self.image = self.im3
        self.rect = pygame.Rect(0, 0, 150, 150)
        self.rect.x = x * 150 + pl.rect.x
        self.rect.y = y * 150 + pl.rect.y
        war_list.append(self)

    def update_dam(self):
        if self.health > 12:
            self.dam = 4
            self.defense = 3
        elif self.health > 5:
            self.dam = 3
            self.defense = 2
        else:
            self.dam = 2
            self.defense = 1

    def attack(self, x1, y1):
        if self.hods > 0 and True in [i.pos_check(x1, y1) for i in war_list]:
            un = [i for i in war_list if i.pos_check(x1, y1)][0]
            if un.type == 'легкая бронетехника' or un.type == 'тяжелая бронетехника':
                un.health -= self.dam * 2
            else:
                un.health -= self.dam
                if place_list[un.y][un.x] == '1' and un.health < 10:
                    un.health += 1
            if un.health < 1:
                war_list.remove(un)
                self.hods = 1
            else:
                if type(un) == Tank:
                    self.health -= un.defense * 2
                elif type(un) == Granatomet:
                    self.health -= un.defense * 3
                elif type(un) == Rathvedchik:
                    pass
                else:
                    self.health -= un.defense
                un.update_dam()
                self.hods = 0
                if self.health < 1:
                    war_list.remove(self)
        self.move_to(x1, y1)

    def update_health(self, n):
        pass


class SAU:
    pass


class Rockets(pygame.sprite.Sprite):
    im = load_image('орбитальный удар.png', (255, 255, 255))
    im1 = load_image('взрыв1.png', (0, 255, 0))
    im2 = load_image('взрыв2.png', (0, 255, 0))
    im3 = load_image('взрыв3.png', (0, 255, 0))
    im4 = load_image('взрыв4.png', (0, 255, 0))
    im5 = load_image('взрыв5.png', (0, 255, 0))
    im6 = load_image('взрыв6.png', (0, 255, 0))

    def __init__(self, group):
        super().__init__(group)
        self.f = True
        self.x1 = None
        self.y1 = None
        self.image = self.im
        self.rect = pygame.Rect(0, 0, 150, 150)
        self.rect.x = 0
        self.rect.y = 0

    def map_move_down(self):
        self.rect.y -= 150

    def map_move_up(self):
        self.rect.y += 150

    def map_move_left(self):
        self.rect.x += 150

    def map_move_right(self):
        self.rect.x -= 150

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_target(self, x, y):
        self.x1 = x
        self.y1 = y

    def self_move(self):
        self.rect.y += 12

    def update_image(self, other, pause):
        if pygame.sprite.collide_rect(self, other) and pause == 0:
            if self.image == self.im:
                self.image = self.im1
                if self.f:
                    self.f = False
                    self.rect.x -= 20
                    self.rect.y -= 20
            elif self.image == self.im1:
                self.image = self.im2
            elif self.image == self.im2:
                self.image = self.im3
            elif self.image == self.im3:
                self.image = self.im4
            elif self.image == self.im4:
                self.image = self.im5
            elif self.image == self.im5:
                self.image = self.im6
            elif self.image == self.im6:
                self.image = pygame.Surface((0, 0))
                self.f = True
                un = [i for i in war_list if i.pos_check(self.x1, self.y1)][0]
                un.health -= 15
                if un.health < 1:
                    war_list.remove(un)
            return True
        elif pygame.sprite.collide_rect(self, other):
            return True
        else:
            return False


class Rocket_target(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.Surface((150, 10), pygame.SRCALPHA)
        self.rect = pygame.Rect(0, 0, 150, 150)
        self.rect.x = 0
        self.rect.y = 0

    def map_move_down(self):
        self.rect.y -= 150

    def map_move_up(self):
        self.rect.y += 150

    def map_move_left(self):
        self.rect.x += 150

    def map_move_right(self):
        self.rect.x -= 150

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y


bg = Bg(bg_group)
bg_plane1 = Bg_airplane(bg_group, 1600, 100)
bg_plane2 = Bg_airplane(bg_group, 1800, 200)

game_pos = 'Меню'
kol_players = None
players_list = []

btn_play = Button(btn_g1, (625, 400, 250, 100), 'играть', 60, (0, 0, 0))

btn_2players = Button(btn_g2, (625, 260, 250, 100), '2 игрока', 60, (0, 0, 0))
btn_3players = Button(btn_g2, (625, 370, 250, 100), '3 игрока', 60, (0, 0, 0))
btn_4players = Button(btn_g2, (625, 480, 250, 100), '4 игрока', 60, (0, 0, 0))
btn_back = Button(btn_g2, (650, 590, 200, 80), 'назад', 50, (0, 0, 0))

btn_ru = Button(btn_g3, (625, 210, 250, 100), 'Россия', 60, (0, 0, 0))
btn_us = Button(btn_g3, (625, 320, 250, 100), 'США', 60, (0, 0, 0))
btn_ch = Button(btn_g3, (625, 430, 250, 100), 'Китай', 60, (0, 0, 0))
btn_ge = Button(btn_g3, (625, 540, 250, 100), 'Германия', 60, (0, 0, 0))
btn_back1 = Button(btn_g3, (650, 650, 200, 80), 'назад', 50, (0, 0, 0))

btn_choose1 = Button(btn_g4, (333, 580, 250, 100), 'новая игра', 60, (0, 0, 0))
btn_choose2 = Button(btn_g4, (916, 580, 250, 100), 'новая игра', 60, (0, 0, 0))
btn_continue1 = Button(btn_g4, (333, 690, 250, 100), 'продолжить', 50, (0, 0, 0))
btn_continue2 = Button(btn_g4, (916, 690, 250, 100), 'продолжить', 50, (0, 0, 0))
btn_back2 = Button(btn_g4, (649, 810, 200, 80), 'назад', 50, (0, 0, 0))
btn_ok = Button(play_g1, (625, 710, 250, 100), 'Начать', 60, (0, 0, 0))

im = load_image("карта 1.png")
im_karta2 = load_image("карта 2.png")

karta = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            if game_pos == 'Меню':
                btn_g1.update(event.pos[0], event.pos[1])
            elif game_pos == 'Кол-во игроков':
                btn_g2.update(event.pos[0], event.pos[1])
            elif game_pos == 'Выбор страны':
                btn_g3.update(event.pos[0], event.pos[1])
            elif game_pos == 'Выбор карты':
                btn_g4.update(event.pos[0], event.pos[1])
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if game_pos == 'Меню':
                if btn_play.click(event.pos[0], event.pos[1]):
                    game_pos = 'Выбор карты'
                    btn_g4.update(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            elif game_pos == 'Кол-во игроков':
                if btn_back.click(event.pos[0], event.pos[1]):
                    game_pos = 'Выбор карты'
                    place_list = None
                elif btn_2players.click(event.pos[0], event.pos[1]):
                    kol_players = 2
                    game_pos = 'Выбор страны'
                    btn_g3.update(event.pos[0], event.pos[1])
                elif btn_3players.click(event.pos[0], event.pos[1]):
                    kol_players = 3
                    game_pos = 'Выбор страны'
                    btn_g3.update(event.pos[0], event.pos[1])
                elif btn_4players.click(event.pos[0], event.pos[1]):
                    kol_players = 4
                    game_pos = 'Выбор страны'
                    btn_g3.update(event.pos[0], event.pos[1])
            elif game_pos == 'Выбор страны':
                if btn_back1.click(event.pos[0], event.pos[1]):
                    game_pos = 'Кол-во игроков'
                    kol_players = None
                    players_list = []
                    btn_ru.lock = False
                    btn_us.lock = False
                    btn_ch.lock = False
                    btn_ge.lock = False
                    btn_g2.update(event.pos[0], event.pos[1])
                elif btn_ru.click(event.pos[0], event.pos[1]):
                    players_list.append('Россия')
                    btn_ru.lock = True
                    btn_ru.update(event.pos[0], event.pos[1])
                elif btn_us.click(event.pos[0], event.pos[1]):
                    players_list.append('США')
                    btn_us.lock = True
                    btn_us.update(event.pos[0], event.pos[1])
                elif btn_ch.click(event.pos[0], event.pos[1]):
                    players_list.append('Китай')
                    btn_ch.lock = True
                    btn_ch.update(event.pos[0], event.pos[1])
                elif btn_ge.click(event.pos[0], event.pos[1]):
                    players_list.append('Германия')
                    btn_ge.lock = True
                    btn_ge.update(event.pos[0], event.pos[1])
            elif game_pos == 'Выбор карты':
                if btn_back2.click(event.pos[0], event.pos[1]):
                    game_pos = 'Меню'
                if btn_choose1.click(event.pos[0], event.pos[1]):
                    game_pos = 'Кол-во игроков'
                    btn_g2.update(event.pos[0], event.pos[1])
                    karta = 1
                elif btn_choose2.click(event.pos[0], event.pos[1]):
                    game_pos = 'Кол-во игроков'
                    btn_g2.update(event.pos[0], event.pos[1])
                    karta = 2
                elif btn_continue1.click(event.pos[0], event.pos[1]):
                    karta = 1
                    file = open('data\\карта 1(сохраненная).txt', mode='r')
                    place_list = [i.split(', ') for i in file.read().split('\n')]
                    file.close()
                    file = open('data\\карта 1(основные данные).txt', mode='r')
                    s = file.readlines()
                    player_index = int(s[0][:-1])
                    kol_players = int(s[1][:-1])
                    players_list = s[2][:-1].split(', ')
                    resurs_list = [ int(i) for i in s[3].split(', ')]
                    tv_list = [['0' for i in range(30)] for j in range(30)]
                    file.close()
                    board = Board(g_board)
                    file = open('data\\карта 1(войска).txt', mode='r')
                    s = file.readlines()
                    war_list = []
                    for i in s:
                        s1 = i.split(' ')
                        if s1[0] == 'Pehota':
                            Pehota(war_g, s1[1], int(s1[2]), int(s1[3]), board, int(s1[4]), int(s1[5]))
                        elif s1[0] == 'BMP':
                            BMP(s1[1], int(s1[2]), int(s1[3]), board, int(s1[4]), int(s1[5]))
                        elif s1[0] == 'Rathvedchik':
                            Rathvedchik(s1[1], int(s1[2]), int(s1[3]), board, int(s1[4]), int(s1[5]))
                        elif s1[0] == 'Granatomet':
                            Granatomet(s1[1], int(s1[2]), int(s1[3]), board, int(s1[4]), int(s1[5]))
                        elif s1[0] == 'Tank':
                            Tank(s1[1], int(s1[2]), int(s1[3]), board, int(s1[4]), int(s1[5]))
                    play()
                elif btn_continue2.click(event.pos[0], event.pos[1]):
                    karta = 2
                    file = open('data\\карта 2(сохраненная).txt', mode='r')
                    place_list = [i.split(', ') for i in file.read().split('\n')]
                    file.close()
                    file = open('data\\карта 2(основные данные).txt', mode='r')
                    s = file.readlines()
                    player_index = int(s[0][:-1])
                    kol_players = int(s[1][:-1])
                    players_list = s[2][:-1].split(', ')
                    resurs_list = [int(i) for i in s[3].split(', ')]
                    tv_list = [['0' for i in range(30)] for j in range(30)]
                    file.close()
                    board = Board(g_board)
                    file = open('data\\карта 2(войска).txt', mode='r')
                    s = file.readlines()
                    war_list = []
                    for i in s:
                        s1 = i.split(' ')
                        if s1[0] == 'Pehota':
                            Pehota(war_g, s1[1], int(s1[2]), int(s1[3]), board, int(s1[4]),
                                   int(s1[5]))
                        elif s1[0] == 'BMP':
                            BMP(s1[1], int(s1[2]), int(s1[3]), board, int(s1[4]), int(s1[5]))
                        elif s1[0] == 'Rathvedchik':
                            Rathvedchik(s1[1], int(s1[2]), int(s1[3]), board, int(s1[4]),
                                        int(s1[5]))
                        elif s1[0] == 'Granatomet':
                            Granatomet(s1[1], int(s1[2]), int(s1[3]), board, int(s1[4]), int(s1[5]))
                        elif s1[0] == 'Tank':
                            Tank(s1[1], int(s1[2]), int(s1[3]), board, int(s1[4]), int(s1[5]))
                    play()




    bg_plane1.rect.x -= 20
    bg_plane2.rect.x -= 20
    if bg_plane1.rect.x < -20000:
        bg_plane1.rect.x = 1600
        bg_plane2.rect.x = 1800
    bg_group.draw(screen)
    if game_pos == 'Меню':
        btn_g1.draw(screen)
    elif game_pos == 'Кол-во игроков':
        btn_g2.draw(screen)
    elif game_pos == 'Выбор страны':
        btn_g3.draw(screen)
        font = pygame.font.Font(None, 70)
        if len(players_list) == kol_players:
            if karta == 1:
                file = open('data\\карта 1(рельеф).txt', mode='r')
            elif karta == 2:
                file = open('data\\карта 2(рельеф).txt', mode='r')
            war_list = []
            place_list = [i.split(', ') for i in file.read().split('\n')]
            tv_list = [['0' for i in range(30)] for j in range(30)]
            file.close()
            player_index = 0
            resurs_list = [20 for i in range(len(players_list))]
            board = Board(g_board)
            play()
        elif len(players_list) == 0:
            text = font.render('Игрок 1', 1, (0, 0, 0))
            screen.blit(text, (662, 50))
        elif len(players_list) == 1:
            text = font.render('Игрок 2', 1, (0, 0, 0))
            screen.blit(text, (662, 50))
        elif len(players_list) == 2:
            text = font.render('Игрок 3', 1, (0, 0, 0))
            screen.blit(text, (662, 50))
        elif len(players_list) == 3:
            text = font.render('Игрок 4', 1, (0, 0, 0))
            screen.blit(text, (662, 50))
    elif game_pos == 'Выбор карты':
        font = pygame.font.Font(None, 70)
        text = font.render('Выберите карту', 1, (0, 0, 0))
        screen.blit(text, (562, 15))
        screen.blit(im, (230, 90))
        screen.blit(im_karta2, (820, 90))
        btn_g4.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()