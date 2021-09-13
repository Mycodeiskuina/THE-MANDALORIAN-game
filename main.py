



import pygame
import os
import pygame as pg
from pygame.locals import *
import sys
import time
import random
import json
import sys

pygame.font.init()
scores1 = {}



def niveles():
    # Colores
    blanco = (255, 255, 255)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    # Variables de la Pantalla
    pantalla_x = 1280
    pantalla_y = 720
    tamanho_pantalla = (pantalla_x, pantalla_y)
    # texto
    letra_fondo4 = pygame.font.SysFont('Arial Rounded MT Bold', 40)
    # Textoboton
    text = letra_fondo4.render('Nivel 0', True, amarillo)
    text2 = letra_fondo4.render('Nivel 1', True, amarillo)
    text3 = letra_fondo4.render('Nivel 2', True, amarillo)
    text4 = letra_fondo4.render('Nivel 3', True, amarillo)
    text5 = letra_fondo4.render('Nivel 4', True, amarillo)
    text6 = letra_fondo4.render('Nivel 5', True, amarillo)
    text7 = letra_fondo4.render('Back', True, amarillo)
    # imagen fondo
    inicio_fondo = pygame.transform.scale(pygame.image.load(os.path.join('Imagenes', 'background.png')),
                                          (tamanho_pantalla))
    Nivel01 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'fondo1.jpeg')), (300, 200))
    Nivel2 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'fondo2.jpeg')), (300, 200))
    Nivel3 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'fondo3.jpeg')), (300, 200))
    Nivel4 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'fondo4.jpeg')), (300, 200))
    Nivel5 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'fondo5.jpeg')), (300, 200))
    # Dimensiones de la pantalla
    pantalla = pygame.display.set_mode(tamanho_pantalla)
    # Reloj: FPS
    reloj = pygame.time.Clock()
    # Flag: bandera de fin del juego
    game_over = False
    pos1nivel0 = 200
    pos2nivel0 = 320
    pos1nivel1 = 590
    pos2nivel1 = 320
    pos1nivel2 = 980
    pos2nivel2 = 320
    pos1nivel3 = 200
    pos2nivel3 = 620
    pos1nivel4 = 590
    pos2nivel4 = 620
    pos1nivel5 = 980
    pos2nivel5 = 620
    pos1back = 0
    pos2back = 0
    mouse = pygame.mouse.get_pos()

    while not game_over:
        # Hasta que el jugador decida romper el bucle: salir del juego
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pos1nivel0 <= mouse[0] <= pos1nivel0 + 100 and pos2nivel0 <= mouse[1] <= pos2nivel0 + 45:
                    main_menu0()
                if pos1nivel1 <= mouse[0] <= pos1nivel1 + 100 and pos2nivel1 <= mouse[1] <= pos2nivel1 + 45:
                    main_menu1()
                if pos1nivel2 <= mouse[0] <= pos1nivel2 + 100 and pos2nivel2 <= mouse[1] <= pos2nivel2 + 45:
                    main_menu2()
                if pos1nivel3 <= mouse[0] <= pos1nivel3 + 100 and pos2nivel3 <= mouse[1] <= pos2nivel3 + 45:
                    main_menu3()
                if pos1nivel4 <= mouse[0] <= pos1nivel4 + 100 and pos2nivel4 <= mouse[1] <= pos2nivel4 + 45:
                    main_menu4()
                if pos1nivel5 <= mouse[0] <= pos1nivel5 + 100 and pos2nivel5 <= mouse[1] <= pos2nivel5 + 45:
                    main_menu5()
                if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                    uwu()

        pantalla.blit(inicio_fondo, (0, 0))
        pantalla.blit(Nivel01, (100, 100))
        pantalla.blit(Nivel01, (490, 100))
        pantalla.blit(Nivel2, (880, 100))
        pantalla.blit(Nivel3, (100, 400))
        pantalla.blit(Nivel4, (490, 400))
        pantalla.blit(Nivel5, (880, 400))

        mouse = pygame.mouse.get_pos()

        # Boton Nivel 0
        if pos1nivel0 <= mouse[0] <= pos1nivel0 + 100 and pos2nivel0 <= mouse[1] <= pos2nivel0 + 45:
            pygame.draw.rect(pantalla, blanco, [pos1nivel0, pos2nivel0, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1nivel0, pos2nivel0, 100, 45])

        # Boton Nivel 1
        if pos1nivel1 <= mouse[0] <= pos1nivel1 + 100 and pos2nivel1 <= mouse[1] <= pos2nivel1 + 45:
            pygame.draw.rect(pantalla, blanco, [pos1nivel1, pos2nivel1, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1nivel1, pos2nivel1, 100, 45])

        # Boton Nivel 2
        if pos1nivel2 <= mouse[0] <= pos1nivel2 + 100 and pos2nivel2 <= mouse[1] <= pos2nivel2 + 45:
            pygame.draw.rect(pantalla, blanco, [pos1nivel2, pos2nivel2, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1nivel2, pos2nivel2, 100, 45])

        # Boton Nivel 3
        if pos1nivel3 <= mouse[0] <= pos1nivel3 + 100 and pos2nivel3 <= mouse[1] <= pos2nivel3 + 45:
            pygame.draw.rect(pantalla, blanco, [pos1nivel3, pos2nivel3, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1nivel3, pos2nivel3, 100, 45])
        # Boton Nivel 4
        if pos1nivel4 <= mouse[0] <= pos1nivel4 + 100 and pos2nivel4 <= mouse[1] <= pos2nivel4 + 45:
            pygame.draw.rect(pantalla, blanco, [pos1nivel4, pos2nivel4, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1nivel4, pos2nivel4, 100, 45])
        # Boton Nivel 5
        if pos1nivel5 <= mouse[0] <= pos1nivel5 + 100 and pos2nivel5 <= mouse[1] <= pos2nivel5 + 45:
            pygame.draw.rect(pantalla, blanco, [pos1nivel5, pos2nivel5, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1nivel5, pos2nivel5, 100, 45])
        # Boton Back
        if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
            pygame.draw.rect(pantalla, blanco, [pos1back, pos2back, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1back, pos2back, 100, 45])

        pantalla.blit(text, (pos1nivel0 + 3, pos2nivel0 + 7))
        pantalla.blit(text2, (pos1nivel1 + 3, pos2nivel1 + 7))
        pantalla.blit(text3, (pos1nivel2 + 3, pos2nivel2 + 7))
        pantalla.blit(text4, (pos1nivel3 + 3, pos2nivel3 + 7))
        pantalla.blit(text5, (pos1nivel4 + 3, pos2nivel4 + 7))
        pantalla.blit(text6, (pos1nivel5 + 3, pos2nivel5 + 7))
        pantalla.blit(text7, (pos1back + 12, pos2back + 7))

        # Actualización de pantalla
        pygame.display.update()
        # FPS
        reloj.tick(60)
    pygame.quit()

def ingresar_jugador():
    screen = pg.display.set_mode((1280, 720))
    font = pg.font.Font(None, 50)
    clock = pg.time.Clock()
    input_box = pg.Rect(540, 300, 250, 50)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    tamanho_pantalla = (1280, 720)
    inicio_fondo = pygame.transform.scale(pygame.image.load(os.path.join('Imagenes', 'background.png')),
                                          (tamanho_pantalla))
    letra_fondo= pygame.font.SysFont('Arial Rounded MT Bold', 70)
    texto= letra_fondo.render('Ingrese nombre del jugador', True, "blue")
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT: done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        Player.name = text
                        return Player.name
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(inicio_fondo,(0,0))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        screen.blit(texto, (350, 200))
        pg.draw.rect(screen, color, input_box, 2)
        pg.display.flip()
        clock.tick(30)

def top_scores(dict):
    x = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
    a = [[k, v] for k, v in x.items()]
    nd = {v[0]: v[1] for k, v in enumerate(a[:5])}
    return nd

def puntajes1():
    amarillo = (255, 233, 0)
    # Variables de la Pantalla
    pantalla_x = 1280
    pantalla_y = 720
    tamanho_pantalla = (pantalla_x, pantalla_y)
    inicio_fondo = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'score.jpg')), (tamanho_pantalla))
    # Dimensiones de la pantalla
    pantalla = pygame.display.set_mode(tamanho_pantalla)
    # Reloj: FPS
    reloj = pygame.time.Clock()
    # Flag: bandera de fin del juego
    game_over = False
    letra_fondo3 = pygame.font.SysFont('Arial Rounded MT Bold', 50)
    # Textoboton
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = letra_fondo3.render('Quit', True, amarillo)
    text2 = letra_fondo3.render('Start', True, amarillo)
    text3 = letra_fondo3.render('Estadisticas', True, amarillo)
    mouse = pygame.mouse.get_pos()
    pos1back = 0
    pos2back = 0
    pos1next = 1180
    pos2next = 680
    mouse = pygame.mouse.get_pos()
    blanco = (255, 255, 255)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    reloj = pygame.time.Clock()
    letra_fondo4 = pygame.font.SysFont('Arial Rounded MT Bold', 40)
    text7 = letra_fondo4.render('Back', True, amarillo)
    text8 = letra_fondo4.render('Next', True, amarillo)
    with open('scores_nivel1.json') as json_file:
       scores1 = json.load(json_file)
    pantalla.blit(inicio_fondo, (0, 0))
    temp={}
    while not game_over:
        # Hasta que el jugador decida romper el bucle: salir del juego
        for evento in pygame.event.get():
            letra_fondo3 = pygame.font.SysFont('Arial Rounded MT Bold', 30)
            x = 130
            for i in scores1.keys():
                for j in range(len(scores1[i])):
                    text1 = letra_fondo3.render(str(scores1[i][j]), True, "red")
                    text2 = letra_fondo3.render(i, True, "red")
                    pantalla.blit(text1, (1000, x))
                    pantalla.blit(text2, (690, x))
                    x += 50
                temp[i]=max(scores1[i])
            top5=top_scores(temp)
            y=350
            for i in top5.keys():
                    text1 = letra_fondo3.render(str(top5[i]), True, "red")
                    text2 = letra_fondo3.render(i, True, "red")
                    pantalla.blit(text1, (370, y))
                    pantalla.blit(text2, (160, y))
                    y += 50

            if evento.type == pygame.QUIT:
                game_over = True

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                    uwu()
                if pos1next <= mouse[0] <= pos1next + 100 and pos2next <= mouse[1] <= pos2next + 45:
                    puntajes2()

        if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
            pygame.draw.rect(pantalla, blanco, [pos1back, pos2back, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1back, pos2back, 100, 45])
        pantalla.blit(text7, (pos1back + 12, pos2back + 7))

        if pos1next<= mouse[0] <= pos1next+ 100 and pos2next <= mouse[1] <= pos2next + 45:
            pygame.draw.rect(pantalla, blanco, [pos1next, pos2next, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1next, pos2next, 100, 45])
        pantalla.blit(text8, (pos1next + 12, pos2next + 7))

        pygame.display.update()

        mouse = pygame.mouse.get_pos()
        # FPS
        reloj.tick(60)

    pygame.quit()

def puntajes2():
    amarillo = (255, 233, 0)
    # Variables de la Pantalla
    pantalla_x = 1280
    pantalla_y = 720
    tamanho_pantalla = (pantalla_x, pantalla_y)
    inicio_fondo = pygame.transform.scale(pygame.image.load(os.path.join('assets', '8.jpg')), (tamanho_pantalla))
    # Dimensiones de la pantalla
    pantalla = pygame.display.set_mode(tamanho_pantalla)
    # Reloj: FPS
    reloj = pygame.time.Clock()
    # Flag: bandera de fin del juego
    game_over = False
    letra_fondo3 = pygame.font.SysFont('Arial Rounded MT Bold', 50)
    # Textoboton
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = letra_fondo3.render('Quit', True, amarillo)
    text2 = letra_fondo3.render('Start', True, amarillo)
    text3 = letra_fondo3.render('Estadisticas', True, amarillo)
    mouse = pygame.mouse.get_pos()
    pos1back = 0
    pos2back = 0
    pos1next = 1180
    pos2next = 680
    mouse = pygame.mouse.get_pos()
    blanco = (255, 255, 255)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    reloj = pygame.time.Clock()
    letra_fondo4 = pygame.font.SysFont('Arial Rounded MT Bold', 40)
    text7 = letra_fondo4.render('Back', True, amarillo)
    text8 = letra_fondo4.render('Next', True, amarillo)
    with open('scores_nivel2.json') as json_file:
        scores2 = json.load(json_file)
    pantalla.blit(inicio_fondo, (0, 0))
    temp={}
    while not game_over:
        # Hasta que el jugador decida romper el bucle: salir del juego
        for evento in pygame.event.get():
            letra_fondo3 = pygame.font.SysFont('Arial Rounded MT Bold', 30)
            x = 130
            for i in scores2.keys():
                for j in range(len(scores2[i])):
                    text1 = letra_fondo3.render(str(scores2[i][j]), True, "red")
                    text2 = letra_fondo3.render(i, True, "red")
                    pantalla.blit(text1, (1000, x))
                    pantalla.blit(text2, (700, x))
                    x += 50
                temp[i] = max(scores2[i])
            top5 = top_scores(temp)
            y = 350
            for i in top5.keys():
                text1 = letra_fondo3.render(str(top5[i]), True, "red")
                text2 = letra_fondo3.render(i, True, "red")
                pantalla.blit(text1, (370, y))
                pantalla.blit(text2, (160, y))
                y += 50

            if evento.type == pygame.QUIT:
                game_over = True

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                    puntajes1()
                if pos1next <= mouse[0] <= pos1next + 100 and pos2next <= mouse[1] <= pos2next + 45:
                    puntajes3()

        if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
            pygame.draw.rect(pantalla, blanco, [pos1back, pos2back, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1back, pos2back, 100, 45])
        pantalla.blit(text7, (pos1back + 12, pos2back + 7))

        if pos1next<= mouse[0] <= pos1next+ 100 and pos2next <= mouse[1] <= pos2next + 45:
            pygame.draw.rect(pantalla, blanco, [pos1next, pos2next, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1next, pos2next, 100, 45])
        pantalla.blit(text8, (pos1next + 12, pos2next + 7))

        pygame.display.update()

        mouse = pygame.mouse.get_pos()
        # FPS
        reloj.tick(60)

    pygame.quit()

def puntajes3():
    amarillo = (255, 233, 0)
    # Variables de la Pantalla
    pantalla_x = 1280
    pantalla_y = 720
    tamanho_pantalla = (pantalla_x, pantalla_y)
    inicio_fondo = pygame.transform.scale(pygame.image.load(os.path.join('assets', '9.jpg')), (tamanho_pantalla))
    # Dimensiones de la pantalla
    pantalla = pygame.display.set_mode(tamanho_pantalla)
    # Reloj: FPS
    reloj = pygame.time.Clock()
    # Flag: bandera de fin del juego
    game_over = False
    letra_fondo3 = pygame.font.SysFont('Arial Rounded MT Bold', 50)
    # Textoboton
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = letra_fondo3.render('Quit', True, amarillo)
    text2 = letra_fondo3.render('Start', True, amarillo)
    text3 = letra_fondo3.render('Estadisticas', True, amarillo)
    mouse = pygame.mouse.get_pos()
    pos1back = 0
    pos2back = 0
    pos1next = 1180
    pos2next = 680
    mouse = pygame.mouse.get_pos()
    blanco = (255, 255, 255)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    reloj = pygame.time.Clock()
    letra_fondo4 = pygame.font.SysFont('Arial Rounded MT Bold', 40)
    text7 = letra_fondo4.render('Back', True, amarillo)
    text8 = letra_fondo4.render('Next', True, amarillo)
    with open('scores_nivel3.json') as json_file:
        scores3 = json.load(json_file)
    pantalla.blit(inicio_fondo, (0, 0))
    temp={}
    while not game_over:
        # Hasta que el jugador decida romper el bucle: salir del juego
        for evento in pygame.event.get():
            letra_fondo3 = pygame.font.SysFont('Arial Rounded MT Bold', 30)
            x = 130
            for i in scores3.keys():
                for j in range(len(scores3[i])):
                    text1 = letra_fondo3.render(str(scores3[i][j]), True, "red")
                    text2 = letra_fondo3.render(i, True, "red")
                    pantalla.blit(text1, (1000, x))
                    pantalla.blit(text2, (700, x))
                    x += 50
                temp[i] = max(scores3[i])
            top5 = top_scores(temp)
            y = 350
            for i in top5.keys():
                text1 = letra_fondo3.render(str(top5[i]), True, "red")
                text2 = letra_fondo3.render(i, True, "red")
                pantalla.blit(text1, (370, y))
                pantalla.blit(text2, (160, y))
                y += 50

            if evento.type == pygame.QUIT:
                game_over = True

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                    puntajes2()
                if pos1next <= mouse[0] <= pos1next + 100 and pos2next <= mouse[1] <= pos2next + 45:
                    puntajes4()

        if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
            pygame.draw.rect(pantalla, blanco, [pos1back, pos2back, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1back, pos2back, 100, 45])
        pantalla.blit(text7, (pos1back + 12, pos2back + 7))

        if pos1next<= mouse[0] <= pos1next+ 100 and pos2next <= mouse[1] <= pos2next + 45:
            pygame.draw.rect(pantalla, blanco, [pos1next, pos2next, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1next, pos2next, 100, 45])
        pantalla.blit(text8, (pos1next + 12, pos2next + 7))

        pygame.display.update()

        mouse = pygame.mouse.get_pos()
        # FPS
        reloj.tick(60)

    pygame.quit()

def puntajes4():
    amarillo = (255, 233, 0)
    # Variables de la Pantalla
    pantalla_x = 1280
    pantalla_y = 720
    tamanho_pantalla = (pantalla_x, pantalla_y)
    inicio_fondo = pygame.transform.scale(pygame.image.load(os.path.join('assets', '10.jpg')), (tamanho_pantalla))
    # Dimensiones de la pantalla
    pantalla = pygame.display.set_mode(tamanho_pantalla)
    # Reloj: FPS
    reloj = pygame.time.Clock()
    # Flag: bandera de fin del juego
    game_over = False
    letra_fondo3 = pygame.font.SysFont('Arial Rounded MT Bold', 50)
    pos1back = 0
    pos2back = 0
    pos1next = 1180
    pos2next = 680
    mouse = pygame.mouse.get_pos()
    blanco = (255, 255, 255)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    reloj = pygame.time.Clock()
    letra_fondo4 = pygame.font.SysFont('Arial Rounded MT Bold', 40)
    text7 = letra_fondo4.render('Back', True, amarillo)
    text8 = letra_fondo4.render('Next', True, amarillo)
    with open('scores_nivel4.json') as json_file:
       scores4 = json.load(json_file)
    pantalla.blit(inicio_fondo, (0, 0))
    temp={}
    while not game_over:
        # Hasta que el jugador decida romper el bucle: salir del juego
        for evento in pygame.event.get():
            letra_fondo3 = pygame.font.SysFont('Arial Rounded MT Bold', 30)
            x = 130
            for i in scores4.keys():
                for j in range(len(scores4[i])):
                    text1 = letra_fondo3.render(str(scores4[i][j]), True, "red")
                    text2 = letra_fondo3.render(i, True, "red")
                    pantalla.blit(text1, (1000, x))
                    pantalla.blit(text2, (700, x))
                    x += 50
                temp[i] = max(scores4[i])
            top5 = top_scores(temp)
            y = 350
            for i in top5.keys():
                text1 = letra_fondo3.render(str(top5[i]), True, "red")
                text2 = letra_fondo3.render(i, True, "red")
                pantalla.blit(text1, (370, y))
                pantalla.blit(text2, (160, y))
                y += 50

            if evento.type == pygame.QUIT:
                game_over = True

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                    puntajes3()
                if pos1next <= mouse[0] <= pos1next + 100 and pos2next <= mouse[1] <= pos2next + 45:
                    puntajes5()

        if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
            pygame.draw.rect(pantalla, blanco, [pos1back, pos2back, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1back, pos2back, 100, 45])
        pantalla.blit(text7, (pos1back + 12, pos2back + 7))

        if pos1next<= mouse[0] <= pos1next+ 100 and pos2next <= mouse[1] <= pos2next + 45:
            pygame.draw.rect(pantalla, blanco, [pos1next, pos2next, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1next, pos2next, 100, 45])
        pantalla.blit(text8, (pos1next + 12, pos2next + 7))

        pygame.display.update()

        mouse = pygame.mouse.get_pos()
        # FPS
        reloj.tick(60)

    pygame.quit()

def puntajes5():
    amarillo = (255, 233, 0)
    # Variables de la Pantalla
    pantalla_x = 1280
    pantalla_y = 720
    tamanho_pantalla = (pantalla_x, pantalla_y)
    inicio_fondo = pygame.transform.scale(pygame.image.load(os.path.join('assets', '11.jpg')), (tamanho_pantalla))
    # Dimensiones de la pantalla
    pantalla = pygame.display.set_mode(tamanho_pantalla)
    # Reloj: FPS
    reloj = pygame.time.Clock()
    # Flag: bandera de fin del juego
    game_over = False
    letra_fondo3 = pygame.font.SysFont('Arial Rounded MT Bold', 50)
    # Textoboton
    pos1back = 0
    pos2back = 0
    mouse = pygame.mouse.get_pos()
    blanco = (255, 255, 255)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    reloj = pygame.time.Clock()
    letra_fondo4 = pygame.font.SysFont('Arial Rounded MT Bold', 40)
    text7 = letra_fondo4.render('Back', True, amarillo)
    text8 = letra_fondo4.render('Next', True, amarillo)
    with open('scores_nivel5.json') as json_file:
        scores5 = json.load(json_file)
    pantalla.blit(inicio_fondo, (0, 0))
    temp={}
    while not game_over:
        # Hasta que el jugador decida romper el bucle: salir del juego
        for evento in pygame.event.get():
            letra_fondo3 = pygame.font.SysFont('Arial Rounded MT Bold', 30)
            x = 130
            for i in scores5.keys():
                for j in range(len(scores5[i])):
                    text1 = letra_fondo3.render(str(scores5[i][j]), True, "red")
                    text2 = letra_fondo3.render(i, True, "red")
                    pantalla.blit(text1, (1000, x))
                    pantalla.blit(text2, (700, x))
                    x += 50
                temp[i] = max(scores5[i])
            top5 = top_scores(temp)
            y = 350
            for i in top5.keys():
                text1 = letra_fondo3.render(str(top5[i]), True, "red")
                text2 = letra_fondo3.render(i, True, "red")
                pantalla.blit(text1, (370, y))
                pantalla.blit(text2, (160, y))
                y += 50

            if evento.type == pygame.QUIT:
                game_over = True

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                    puntajes4()

        if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
            pygame.draw.rect(pantalla, blanco, [pos1back, pos2back, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1back, pos2back, 100, 45])
        pantalla.blit(text7, (pos1back + 12, pos2back + 7))

        pygame.display.update()

        mouse = pygame.mouse.get_pos()
        # FPS
        reloj.tick(60)

    pygame.quit()


def uwu():
    negro = (0, 0, 0)
    blanco = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    # Variables de la Pantalla
    pantalla_x = 1280
    pantalla_y = 720
    tamanho_pantalla = (pantalla_x, pantalla_y)
    # imagen fondo
    inicio_fondo = pygame.transform.scale(pygame.image.load(os.path.join('Imagenes', 'background.png')),(tamanho_pantalla))
    inicio_fondo2 = pygame.transform.scale(pygame.image.load(os.path.join('Imagenes', 'menupic.png')),(tamanho_pantalla))
    # Dimensiones de la pantalla
    pantalla = pygame.display.set_mode(tamanho_pantalla)
    pygame.mixer.music.load('Audio/Main Theme.mp3')
    pygame.mixer.music.play(100000000)
    # Reloj: FPS
    reloj = pygame.time.Clock()
    # Flag: bandera de fin del juego
    game_over = False
    letra_fondo = pygame.font.SysFont('comicsans', 34)
    letra_fondo2 = pygame.font.SysFont('Cooper Black', 70)
    letra_fondo3 = pygame.font.SysFont('Arial Rounded MT Bold', 50)
    # Textoboton
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = letra_fondo3.render('Quit', True, amarillo)
    text2 = letra_fondo3.render('Start', True, amarillo)
    text3 = letra_fondo3.render('Scores', True, amarillo)
    mouse = pygame.mouse.get_pos()

    pos1 = 800
    pos2 = 500
    pos_start = 795
    pos2_start = 400
    pos1_ig = 800
    pos2_ig = 600
    while not game_over:
        # Hasta que el jugador decida romper el bucle: salir del juego
        for evento in pygame.event.get():
            pantalla.blit(inicio_fondo, (0, 0))
            pantalla.blit(inicio_fondo2, (0, 0))
            # Si sale del juego
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pos_start <= mouse[0] <= pos_start + 90 and pos2_start <= mouse[1] <= pos2_start + 45:
                    niveles()

                if pos1 <= mouse[0] <= pos1 + 90 and pos2 <= mouse[1] <= pos2 + 45:
                    pygame.quit()

                if pos1_ig <= mouse[0] <= pos1_ig + 125 and pos2_ig <= mouse[1] <= pos2_ig + 45:
                    puntajes1()

        mouse = pygame.mouse.get_pos()

        if pos_start <= mouse[0] <= pos_start + 90 and pos2_start <= mouse[1] <= pos2_start + 45:
            pygame.draw.rect(pantalla, blanco, [pos_start, pos2_start, 90, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos_start, pos2_start, 90, 45])

        if pos1 <= mouse[0] <= pos1 + 90 and pos2 <= mouse[1] <= pos2 + 45:
            pygame.draw.rect(pantalla, blanco, [pos1 - 5, pos2 - 5, 90, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1 - 5, pos2 - 5, 90, 45])

        if pos1_ig <= mouse[0] <= pos1_ig + 125 and pos2_ig <= mouse[1] <= pos2_ig + 45:
            pygame.draw.rect(pantalla, blanco, [pos1_ig - 5, pos2_ig - 5, 125, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1_ig - 5, pos2_ig - 5, 125, 45])

        # superimposing the text onto our button
        pantalla.blit(text, (pos1, pos2))
        pantalla.blit(text2, (pos_start + 2, pos2_start + 2))
        pantalla.blit(text3, (pos1_ig + 2, pos2_ig + 2))
        # Actualización de pantalla
        pygame.display.update()
        # FPS
        reloj.tick(60)

    pygame.quit()


# fuentes de escritura
pygame.font.init()
pygame.mixer.init()
# dimensiones de la pantalla
WIDTH = 1280
HEIGHT = 720
# pantalla
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# titulo de la pantalla
pygame.display.set_caption("THE MANDALORIAN REDEMPTION")
icon = pygame.image.load(os.path.join("assets", "icon.png"))
pygame.display.set_icon(icon)
# enemigo

enemigo = pygame.image.load(os.path.join("assets", "tiefighter.png"))
vida = pygame.image.load(os.path.join("assets", "item_life.png"))
escudo = pygame.image.load(os.path.join("assets", "item_boost.png"))

# jugador
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "razorcrest_shield.png"))

# lasers
RED_LASER = pygame.image.load(os.path.join("assets", "shoot_tiefighter.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "shoot_tiefighter.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "shoot_tiefighter.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "shoot_razorcrest.png"))

# fondo y lo transforma segun dimensiones
BG1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "fondo1.jpeg")), (WIDTH, HEIGHT))
BG2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "fondo2.jpeg")), (WIDTH, HEIGHT))
BG3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "fondo3.jpeg")), (WIDTH, HEIGHT))
BG4 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "fondo4.jpeg")), (WIDTH, HEIGHT))
BG5 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "fondo5.jpeg")), (WIDTH, HEIGHT))


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.x -= vel

    def off_screen(self, width):
        return not (self.x <= width and self.x >= 0)

    def collision(self, obj):
        return collide(self, obj)


# todo lo que tenga que ver con el jugador y los enemigos
class Ship:
    COOLDOWN = 30

    # health es la barra de vida
    def __init__(self, x, y, health=100):
        # atributos
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        self.color = None
        self.score = 0
        self.name = None

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(WIDTH):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                if obj.color == "red":
                    obj.score += 1
                obj.health -= 20
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        self.sonido_disparo = pygame.mixer.Sound('Audio/Disparo.wav')
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 5
            self.sonido_disparo.play()

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.score = 0
        self.name = None
        # colision mas cvr
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        self.sonido_explosion = pygame.mixer.Sound('Audio/Explosion.wav')
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(WIDTH):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        if obj.color == "red":
                            obj.health -= 50
                            self.score += 10
                            self.sonido_explosion.play()
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    # barra de vida
    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
        self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health / self.max_health),
        10))


class Enemy(Ship):
    COLOR_MAP = {
        "red": (enemigo, RED_LASER),
        "blue": (vida, GREEN_LASER),
        "green": (escudo, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.color = color

    def move(self, vel):
        self.x -= vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def gana(puntos):
    amarillo = (255, 233, 0)
    # Variables de la Pantalla
    pantalla_x = 1280
    pantalla_y = 720
    tamanho_pantalla = (pantalla_x, pantalla_y)
    inicio_fondo = pygame.transform.scale(pygame.image.load(os.path.join('Imagenes', 'background.png')), (tamanho_pantalla))
    # Dimensiones de la pantalla
    pantalla = pygame.display.set_mode(tamanho_pantalla)
    # Reloj: FPS
    reloj = pygame.time.Clock()
    # Flag: bandera de fin del juego
    game_over = False
    letra_fondo3 = pygame.font.SysFont('Arial Rounded MT Bold', 50)
    pos1back = 500
    pos2back = 340
    pos1next = 700
    pos2next = 340
    mouse = pygame.mouse.get_pos()
    blanco = (255, 255, 255)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    reloj = pygame.time.Clock()
    letra_fondo4 = pygame.font.SysFont('Arial Rounded MT Bold', 40)
    letra_fondo5 = pygame.font.SysFont('Arial Rounded MT Bold', 70)
    text4 = letra_fondo5.render('Haz derrotado a todas las fuerzas imperiales', True, amarillo)
    text5 = letra_fondo5.render('Tu puntaje es', True, amarillo)
    text6 = letra_fondo5.render(str(puntos), True, amarillo)
    text7 = letra_fondo4.render('Inicio', True, amarillo)
    text8 = letra_fondo4.render('Niveles', True, amarillo)
    pantalla.blit(inicio_fondo, (0, 0))
    while not game_over:
        # Hasta que el jugador decida romper el bucle: salir del juego
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                    uwu()
                if pos1next <= mouse[0] <= pos1next + 100 and pos2next <= mouse[1] <= pos2next + 45:
                    niveles()

        if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
            pygame.draw.rect(pantalla, blanco, [pos1back, pos2back, 100, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1back, pos2back, 100, 45])
        pantalla.blit(text7, (pos1back + 12, pos2back + 7))

        if pos1next <= mouse[0] <= pos1next + 120 and pos2next <= mouse[1] <= pos2next + 45:
            pygame.draw.rect(pantalla, blanco, [pos1next, pos2next, 120, 45])
        else:
            pygame.draw.rect(pantalla, color_dark, [pos1next, pos2next, 120, 45])
        pantalla.blit(text8, (pos1next + 12, pos2next + 7))
        pantalla.blit(text4, (100, 100))
        pantalla.blit(text5, (450, 200))
        pantalla.blit(text6, (780, 200))

        pygame.display.update()

        mouse = pygame.mouse.get_pos()
        # FPS
        reloj.tick(60)

    pygame.quit()
def main0():
    run = True
    FPS = 50
    level = 0
    lives = 3
    # inicializa el tipo de texto(fuente) en la pantalla
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 6
    enemy_vel = 1

    player_vel = 5
    laser_vel = 2

    player = Player(50, 360)
    player.name=ingresar_jugador()
    player.score = 0
    max_score = -10000
    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    # dibuja la pantalla las veces que sea necesario
    def redraw_window():
        # blit: pone las cosas segun sus coordenadas
        SCREEN.blit(BG1, (0, 0))
        # aqui asigna a las variables el texto que imprimira luego
        lives_label = main_font.render(f"Vidas: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Nivel: {level}", 1, (255, 255, 255))
        score_label = main_font.render(f"Puntaje: {player.score}", 1, (255, 255, 255))
        texto_moverse = main_font.render('Usa w,a,s,d para moverte', 1, (255, 255, 255))
        texto_disparar = main_font.render('Usa barra espaciadora para disparar', 1, (255, 255, 255))
        # muestra el texto en la pantalla
        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        SCREEN.blit(score_label, (WIDTH / 2 - 100, 10))
        SCREEN.blit(texto_moverse, (10, 50))
        SCREEN.blit(texto_disparar, (10, 600))
        for enemy in enemies:
            enemy.draw(SCREEN)

        player.draw(SCREEN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            SCREEN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))
        pygame.display.update()

    cnt = 0
    pos1back = 0
    pos2back = 675
    blanco = (255, 255, 255)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    mouse = pygame.mouse.get_pos()
    reloj = pygame.time.Clock()
    letra_fondo4 = pygame.font.SysFont('Arial Rounded MT Bold', 40)
    text7 = letra_fondo4.render('Back', True, amarillo)
    while run:
        clock.tick(FPS)
        redraw_window()
        # barra de salud y vidas
        if lives <= 0:
            lost = True
            lost_count += 1

        if player.health <= 0:
            lives -= 1
            player.health = 100

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        # cada vez que se sube de nivel se aumenta 5 naves
        if len(enemies) == 0:
            cnt += 1
            if cnt == 2:
                with open("scores_nivel1.json") as scorefile:
                    scores1=json.load(scorefile)

                if player.name in scores1.keys():
                    scores1[player.name].append(player.score)
                else:
                    scores1[player.name]=[]
                    scores1[player.name].append(player.score)

                with open('scores_nivel1.json', 'w') as scorefile:
                    json.dump(scores1, scorefile)
                gana(player.score)
            level += 0
            wave_length += 10
            for i in range(wave_length):
                col = random.choice(["red", "blue", "green"])
                enemy = Enemy(random.randrange(WIDTH, WIDTH + 2000), random.randrange(0, HEIGHT - 150), col)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                    niveles()
            mouse = pygame.mouse.get_pos()
        reloj.tick(60)
        if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
            pygame.draw.rect(SCREEN, blanco, [pos1back, pos2back, 100, 45])
        else:
            pygame.draw.rect(SCREEN, color_dark, [pos1back, pos2back, 100, 45])

        SCREEN.blit(text7, (pos1back + 12, pos2back + 7))
        pygame.display.update()

        # dependiendo de las teclas en que direccion se movera
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
            if enemy.color == "red":
                if random.randrange(0, 2 * 60) == 1:
                    enemy.shoot()

                if collide(enemy, player):
                    player.health -= 25
                    enemies.remove(enemy)

            elif enemy.color == "blue":
                if collide(enemy, player):
                    lives += 1
                    enemies.remove(enemy)
            elif enemy.color == "green":
                if collide(enemy, player):
                    player.score+=5
                    enemies.remove(enemy)
            if enemy.x - enemy.get_width() < 0:
                # lives -= 1
                enemies.remove(enemy)

            # Explosion()

        player.move_lasers(-laser_vel, enemies)


def main_menu0():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True

    while run:
        SCREEN.blit(BG1, (0, 0))
        title_label = title_font.render("PRESIONE SU MOUSE....", 1, (255, 255, 255))
        SCREEN.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            # cuando cierra la ventana
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main0()
    pygame.quit()

def main1():
    run = True
    FPS = 50
    level = 0
    lives = 3
    # inicializa el tipo de texto(fuente) en la pantalla
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 15
    enemy_vel = 2

    player_vel = 5
    laser_vel = 5

    player = Player(50, 360)
    player.name=ingresar_jugador()
    player.score = 0
    max_score = -10000
    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    # dibuja la pantalla las veces que sea necesario
    def redraw_window():
        # blit: pone las cosas segun sus coordenadas
        SCREEN.blit(BG1, (0, 0))
        # aqui asigna a las variables el texto que imprimira luego
        lives_label = main_font.render(f"Vidas: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Nivel: {level}", 1, (255, 255, 255))
        score_label = main_font.render(f"Puntaje: {player.score}", 1, (255, 255, 255))
        # muestra el texto en la pantalla
        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        SCREEN.blit(score_label, (WIDTH / 2 - 100, 10))

        for enemy in enemies:
            enemy.draw(SCREEN)

        player.draw(SCREEN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            SCREEN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))
        pygame.display.update()

    cnt = 0
    pos1back = 0
    pos2back = 675
    blanco = (255, 255, 255)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    mouse = pygame.mouse.get_pos()
    reloj = pygame.time.Clock()
    letra_fondo4 = pygame.font.SysFont('Arial Rounded MT Bold', 40)
    text7 = letra_fondo4.render('Back', True, amarillo)
    while run:
        clock.tick(FPS)
        redraw_window()
        # barra de salud y vidas
        if lives <= 0:
            lost = True
            lost_count += 1

        if player.health <= 0:
            lives -= 1
            player.health = 100

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        # cada vez que se sube de nivel se aumenta 5 naves
        if len(enemies) == 0:
            cnt += 1
            if cnt == 2:
                #significa que termino la partida
                with open("scores_nivel2.json") as scorefile:
                    scores2=json.load(scorefile)

                if player.name in scores2.keys():
                    scores2[player.name].append(player.score)
                else:
                    scores2[player.name]=[]
                    scores2[player.name].append(player.score)
                with open('scores_nivel2.json', 'w') as scorefile:
                    json.dump(scores2, scorefile)
                gana(player.score)


            level += 1
            wave_length += 15
            for i in range(wave_length):
                col = random.choice(["red", "blue", "green"])
                enemy = Enemy(random.randrange(WIDTH, WIDTH + 2000), random.randrange(0, HEIGHT - 150), col)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                    niveles()
            mouse = pygame.mouse.get_pos()
        reloj.tick(60)
        if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
            pygame.draw.rect(SCREEN, blanco, [pos1back, pos2back, 100, 45])
        else:
            pygame.draw.rect(SCREEN, color_dark, [pos1back, pos2back, 100, 45])

        SCREEN.blit(text7, (pos1back + 12, pos2back + 7))
        pygame.display.update()

        # dependiendo de las teclas en que direccion se movera
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
            if enemy.color == "red":
                if random.randrange(0, 2 * 60) == 1:
                    enemy.shoot()

                if collide(enemy, player):
                    player.health -= 25
                    enemies.remove(enemy)

            elif enemy.color == "blue":
                if collide(enemy, player):
                    lives += 1
                    enemies.remove(enemy)
            elif enemy.color == "green":
                if collide(enemy, player):
                    player.score+=5
                    enemies.remove(enemy)
            if enemy.x - enemy.get_width() < 0:
                # lives -= 1
                enemies.remove(enemy)

            # Explosion()

        player.move_lasers(-laser_vel, enemies)


def main_menu1():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True

    while run:
        SCREEN.blit(BG1, (0, 0))
        title_label = title_font.render("PRESIONE SU MOUSE....", 1, (255, 255, 255))
        SCREEN.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            # cuando cierra la ventana
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main1()
    pygame.quit()


def main2():
    run = True
    FPS = 50
    level = 1
    lives = 3
    # inicializa el tipo de texto(fuente) en la pantalla
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 20
    enemy_vel = 4

    player_vel = 5
    laser_vel = 6

    player = Player(50, 360)
    player.score = 0
    player.name = ingresar_jugador()
    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    # dibuja la pantalla las veces que sea necesario
    def redraw_window():
        # blit: pone las cosas segun sus coordenadas
        SCREEN.blit(BG2, (0, 0))
        # aqui asigna a las variables el texto que imprimira luego
        lives_label = main_font.render(f"Vidas: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Nivel: {level}", 1, (255, 255, 255))
        score_label = main_font.render(f"Puntaje: {player.score}", 1, (255, 255, 255))
        # muestra el texto en la pantalla
        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        SCREEN.blit(score_label, (WIDTH / 2 - 100, 10))

        for enemy in enemies:
            enemy.draw(SCREEN)

        player.draw(SCREEN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            SCREEN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))

        pygame.display.update()

    cnt = 0
    pos1back = 0
    pos2back = 675
    blanco = (255, 255, 255)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    mouse = pygame.mouse.get_pos()
    reloj = pygame.time.Clock()
    letra_fondo4 = pygame.font.SysFont('Arial Rounded MT Bold', 40)
    text7 = letra_fondo4.render('Back', True, amarillo)
    while run:
        clock.tick(FPS)
        redraw_window()
        # barra de salud y vidas
        if lives <= 0:
            lost = True
            lost_count += 1

        if player.health <= 0:
            lives -= 1
            player.health = 100

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        # cada vez que se sube de nivel se aumenta 5 naves
        if len(enemies) == 0:
            cnt += 1
            if cnt == 2:
                with open("scores_nivel2.json") as scorefile:
                    scores2=json.load(scorefile)

                if player.name in scores2.keys():
                    scores2[player.name].append(player.score)
                else:
                    scores2[player.name]=[]
                    scores2[player.name].append(player.score)
                with open('scores_nivel2.json', 'w') as scorefile:
                    json.dump(scores2, scorefile)
                gana(player.score)
            level += 1
            wave_length += 20
            for i in range(wave_length):
                col = random.choice(["red", "blue", "green"])
                enemy = Enemy(random.randrange(WIDTH, WIDTH + 2000), random.randrange(0, HEIGHT - 150), col)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                    niveles()
            mouse = pygame.mouse.get_pos()
        reloj.tick(60)
        if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                pygame.draw.rect(SCREEN, blanco, [pos1back, pos2back, 100, 45])
        else:
                pygame.draw.rect(SCREEN, color_dark, [pos1back, pos2back, 100, 45])

        SCREEN.blit(text7, (pos1back + 12, pos2back + 7))
        pygame.display.update()
        reloj.tick(60)
        # dependiendo de las teclas en que direccion se movera
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
            if enemy.color == "red":
                # enemy.move_lasers(laser_vel, player)
                if random.randrange(0, 2 * 60) == 1:
                    enemy.shoot()

                if collide(enemy, player):
                    player.health -= 25
                    enemies.remove(enemy)

            elif enemy.color == "blue":
                if collide(enemy, player):
                    lives += 1
                    enemies.remove(enemy)
            elif enemy.color == "green":
                if collide(enemy, player):
                    player.score+=5
                    enemies.remove(enemy)
            if enemy.x - enemy.get_width() < 0:
                enemies.remove(enemy)

            # Explosion()

        player.move_lasers(-laser_vel, enemies)


def main_menu2():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        SCREEN.blit(BG2, (0, 0))
        title_label = title_font.render("PRESIONE SU MOUSE....", 1, (255, 255, 255))
        SCREEN.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            # cuando cierra la ventana
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main2()
    pygame.quit()


def main3():
    run = True
    FPS = 50
    level = 2
    lives = 2
    # inicializa el tipo de texto(fuente) en la pantalla
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 25
    enemy_vel = 3

    player_vel = 5
    laser_vel = 7

    player = Player(50, 360)
    player.score = 0
    player.name = ingresar_jugador()
    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    # dibuja la pantalla las veces que sea necesario
    def redraw_window():
        # blit: pone las cosas segun sus coordenadas
        SCREEN.blit(BG3, (0, 0))
        # aqui asigna a las variables el texto que imprimira luego
        lives_label = main_font.render(f"Vidas: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Nivel: {level}", 1, (255, 255, 255))
        score_label = main_font.render(f"Puntaje: {player.score}", 1, (255, 255, 255))
        # muestra el texto en la pantalla
        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        SCREEN.blit(score_label, (WIDTH / 2 - 100, 10))

        for enemy in enemies:
            enemy.draw(SCREEN)

        player.draw(SCREEN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            SCREEN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))


        pygame.display.update()

    cnt = 0
    pos1back = 0
    pos2back = 675
    blanco = (255, 255, 255)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    mouse = pygame.mouse.get_pos()
    reloj = pygame.time.Clock()
    letra_fondo4 = pygame.font.SysFont('Arial Rounded MT Bold', 40)
    text7 = letra_fondo4.render('Back', True, amarillo)
    while run:
        clock.tick(FPS)
        redraw_window()
        # barra de salud y vidas
        if lives <= 0:
            lost = True
            lost_count += 1

        if player.health <= 0:
            lives -= 1
            player.health = 100

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        # cada vez que se sube de nivel se aumenta 5 naves
        if len(enemies) == 0:
            cnt += 1
            if cnt == 2:
                with open("scores_nivel3.json") as scorefile:
                    scores3=json.load(scorefile)

                if player.name in scores3.keys():
                    scores3[player.name].append(player.score)
                else:
                    scores3[player.name]=[]
                    scores3[player.name].append(player.score)
                with open('scores_nivel3.json', 'w') as scorefile:
                    json.dump(scores3, scorefile)
                gana(player.score)
            level += 1
            wave_length += 25
            for i in range(wave_length):
                col = random.choice(["red", "blue", "green"])
                enemy = Enemy(random.randrange(WIDTH, WIDTH + 2000), random.randrange(0, HEIGHT - 150), col)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                        niveles()
            mouse = pygame.mouse.get_pos()
        reloj.tick(60)
        if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                pygame.draw.rect(SCREEN, blanco, [pos1back, pos2back, 100, 45])
        else:
                pygame.draw.rect(SCREEN, color_dark, [pos1back, pos2back, 100, 45])

        SCREEN.blit(text7, (pos1back + 12, pos2back + 7))
        pygame.display.update()
        reloj.tick(60)
        # dependiendo de las teclas en que direccion se movera
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
            if enemy.color == "red":
                # enemy.move_lasers(laser_vel, player)
                if random.randrange(0, 2 * 60) == 1:
                    enemy.shoot()

                if collide(enemy, player):
                    player.health -= 25
                    enemies.remove(enemy)

            elif enemy.color == "blue":
                if collide(enemy, player):
                    lives += 1
                    enemies.remove(enemy)
            elif enemy.color == "green":
                if collide(enemy, player):
                    player.score+=5
                    enemies.remove(enemy)
            if enemy.x - enemy.get_width() < 0:
                enemies.remove(enemy)


        player.move_lasers(-laser_vel, enemies)


def main_menu3():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        SCREEN.blit(BG3, (0, 0))
        title_label = title_font.render("PRESIONE SU MOUSE....", 1, (255, 255, 255))
        SCREEN.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            # cuando cierra la ventana
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main3()
    pygame.quit()


def main4():
    run = True
    FPS = 50
    level = 0
    lives = 2
    # inicializa el tipo de texto(fuente) en la pantalla
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 30
    enemy_vel = 3

    player_vel = 5
    laser_vel = 7

    player = Player(50, 360)
    player.score = 0
    player.name = ingresar_jugador()
    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    # dibuja la pantalla las veces que sea necesario
    def redraw_window():
        # blit: pone las cosas segun sus coordenadas
        SCREEN.blit(BG4, (0, 0))
        # aqui asigna a las variables el texto que imprimira luego
        lives_label = main_font.render(f"Vidas: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Nivel: {level}", 1, (255, 255, 255))
        score_label = main_font.render(f"Puntaje: {player.score}", 1, (255, 255, 255))
        # muestra el texto en la pantalla
        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        SCREEN.blit(score_label, (WIDTH / 2 - 100, 10))

        for enemy in enemies:
            enemy.draw(SCREEN)

        player.draw(SCREEN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            SCREEN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))


        pygame.display.update()

    cnt = 0
    pos1back = 0
    pos2back = 675
    blanco = (255, 255, 255)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    mouse = pygame.mouse.get_pos()
    reloj = pygame.time.Clock()
    letra_fondo4 = pygame.font.SysFont('Arial Rounded MT Bold', 40)
    text7 = letra_fondo4.render('Back', True, amarillo)
    while run:
        clock.tick(FPS)
        redraw_window()
        # barra de salud y vidas
        if lives <= 0:
            lost = True
            lost_count += 1

        if player.health <= 0:
            lives -= 1
            player.health = 100

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        # cada vez que se sube de nivel se aumenta 5 naves
        if len(enemies) == 0:
            cnt += 1
            if cnt == 2:
                with open("scores_nivel4.json") as scorefile:
                    scores4=json.load(scorefile)

                if player.name in scores4.keys():
                    scores4[player.name].append(player.score)
                else:
                    scores4[player.name]=[]
                    scores4[player.name].append(player.score)
                with open('scores_nivel4.json', 'w') as scorefile:
                    json.dump(scores4, scorefile)
                gana(player.score)
            level += 1
            wave_length += 30
            for i in range(wave_length):
                col = random.choice(["red", "blue", "green"])
                enemy = Enemy(random.randrange(WIDTH, WIDTH + 2000), random.randrange(0, HEIGHT - 150), col)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                        niveles()
            mouse = pygame.mouse.get_pos()
        reloj.tick(60)
        if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                pygame.draw.rect(SCREEN, blanco, [pos1back, pos2back, 100, 45])
        else:
                pygame.draw.rect(SCREEN, color_dark, [pos1back, pos2back, 100, 45])

        SCREEN.blit(text7, (pos1back + 12, pos2back + 7))
        pygame.display.update()
        reloj.tick(60)
        # dependiendo de las teclas en que direccion se movera
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
            if enemy.color == "red":
                # enemy.move_lasers(laser_vel, player)
                if random.randrange(0, 2 * 60) == 1:
                    enemy.shoot()

                if collide(enemy, player):
                    player.health -= 50
                    enemies.remove(enemy)

            elif enemy.color == "blue":
                if collide(enemy, player):
                    lives += 1
                    enemies.remove(enemy)
            elif enemy.color == "green":
                if collide(enemy, player):
                    player.score+=5
                    enemies.remove(enemy)
            if enemy.x - enemy.get_width() < 0:
                # lives -= 1
                enemies.remove(enemy)

            # Explosion()

        player.move_lasers(-laser_vel, enemies)


def main_menu4():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        SCREEN.blit(BG4, (0, 0))
        title_label = title_font.render("PRESIONE SU MOUSE....", 1, (255, 255, 255))
        SCREEN.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            # cuando cierra la ventana
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main4()
    pygame.quit()


def main5():
    run = True
    FPS = 50
    level = 0
    lives = 2
    # inicializa el tipo de texto(fuente) en la pantalla
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 35
    enemy_vel = 3

    player_vel = 5
    laser_vel = 8

    player = Player(50, 360)
    player.score = 0
    player.name = ingresar_jugador()
    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    # dibuja la pantalla las veces que sea necesario
    def redraw_window():
        # blit: pone las cosas segun sus coordenadas
        SCREEN.blit(BG5, (0, 0))
        # aqui asigna a las variables el texto que imprimira luego
        lives_label = main_font.render(f"Vidas: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Nivel: {level}", 1, (255, 255, 255))
        score_label = main_font.render(f"Puntaje: {player.score}", 1, (255, 255, 255))
        # muestra el texto en la pantalla
        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        SCREEN.blit(score_label, (WIDTH / 2 - 100, 10))

        for enemy in enemies:
            enemy.draw(SCREEN)

        player.draw(SCREEN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            SCREEN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))


        pygame.display.update()

    cnt = 0
    pos1back = 0
    pos2back = 675
    blanco = (255, 255, 255)
    color_dark = (100, 100, 100)
    amarillo = (255, 233, 0)
    mouse = pygame.mouse.get_pos()
    reloj = pygame.time.Clock()
    letra_fondo4 = pygame.font.SysFont('Arial Rounded MT Bold', 40)
    text7 = letra_fondo4.render('Back', True, amarillo)
    while run:
        clock.tick(FPS)
        redraw_window()
        # barra de salud y vidas
        if lives <= 0:
            lost = True
            lost_count += 1

        if player.health <= 0:
            lives -= 1
            player.health = 100

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        # cada vez que se sube de nivel se aumenta 5 naves
        if len(enemies) == 0:
            cnt += 1
            if cnt == 2:
                with open("scores_nivel5.json") as scorefile:
                    scores5=json.load(scorefile)

                if player.name in scores5.keys():
                    scores5[player.name].append(player.score)
                else:
                    scores5[player.name]=[]
                    scores5[player.name].append(player.score)
                with open('scores_nivel5.json', 'w') as scorefile:
                    json.dump(scores5, scorefile)
                gana(player.score)
            level += 1
            wave_length += 35
            for i in range(wave_length):
                col = random.choice(["red", "blue", "green"])
                enemy = Enemy(random.randrange(WIDTH, WIDTH + 2000), random.randrange(0, HEIGHT - 150), col)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
                    niveles()
            mouse = pygame.mouse.get_pos()
        reloj.tick(60)
        if pos1back <= mouse[0] <= pos1back + 100 and pos2back <= mouse[1] <= pos2back + 45:
            pygame.draw.rect(SCREEN, blanco, [pos1back, pos2back, 100, 45])
        else:
            pygame.draw.rect(SCREEN, color_dark, [pos1back, pos2back, 100, 45])

        SCREEN.blit(text7, (pos1back + 12, pos2back + 7))
        pygame.display.update()
        reloj.tick(60)
        # dependiendo de las teclas en que direccion se movera
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
            if enemy.color == "red":
                # enemy.move_lasers(laser_vel, player)
                if random.randrange(0, 2 * 60) == 1:
                    enemy.shoot()

                if collide(enemy, player):
                    player.health -= 50
                    enemies.remove(enemy)

            elif enemy.color == "blue":
                if collide(enemy, player):
                    lives += 1
                    enemies.remove(enemy)
            elif enemy.color == "green":
                if collide(enemy, player):
                    player.score+=5
                    enemies.remove(enemy)
            if enemy.x - enemy.get_width() < 0:
                enemies.remove(enemy)

            # Explosion()

        player.move_lasers(-laser_vel, enemies)


def main_menu5():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        SCREEN.blit(BG5, (0, 0))
        title_label = title_font.render("PRESIONE SU MOUSE....", 1, (255, 255, 255))
        SCREEN.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            # cuando cierra la ventana
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main5()
    pygame.quit()

uwu()
