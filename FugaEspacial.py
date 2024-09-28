# Jogo: Fuga Espacial
# História: Um grupo de pessoas importantes para a salvação da humanidade escapam em uma nave danificada. A nave precisa desviar das ameaças até a zona segura.

import os
import time
import random 
import pygame

class Background:
    """
    Define o plano de fundo do jogo
    """
    image = None
    margin_left = None
    margin_right = None
    
    def __init__(self):
        background_fig = pygame.image.load("images/background.png")
        background_fig.convert()
        background_fig = pygame.transform.scale(background_fig, (800, 602))
        self.image = background_fig
        
        margin_left_fig = pygame.image.load("images/margin_1.png")
        margin_left_fig.convert()
        margin_left_fig = pygame.transform.scale(margin_left_fig, (60, 602))
        self.margin_left = margin_left_fig
        
        margin_right_fig = pygame.image.load("images/margin_2.png")
        margin_right_fig.convert()
        margin_right_fig = pygame.transform.scale(margin_right_fig, (60, 602))
        self.margin_right = margin_right_fig  
    
    def update(self, dt):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, (0, 0))
        screen.blit(self.margin_left, (0, 0))
        screen.blit(self.margin_right, (740, 0))
    
    def move(self, screen, scr_height, movL_x, movL_y, movR_x, movR_y):
        for i in range(0, 2):
            screen.blit(self.image, (movL_x, movL_y - (i * scr_height)))
            screen.blit(self.margin_left, (movL_x, movL_y - (i * scr_height)))
            screen.blit(self.margin_right, (movR_x, movR_y - (i * scr_height)))

class Player:
    image = None
    x = None
    y = None
    
    def __init__(self, x, y):
        player_fig = pygame.image.load('images/player.png')
        player_fig.convert()
        player_fig = pygame.transform.scale(player_fig, (90, 90))
        self.image = player_fig
        self.x = x
        self.y = y

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

class Hazard:
    image = None
    x = None
    y = None
    
    def __init__(self, img, x, y):
        hazard_fig = pygame.image.load(img)
        hazard_fig.convert()
        hazard_fig = pygame.transform.scale(hazard_fig, (130, 130))
        self.image = hazard_fig
        self.x = x
        self.y = y

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

class Game:
    screen = None
    screen_size = None
    width = 800
    height = 600
    run = True
    background = None
    player = None
    hazard = []
    
    direita = pygame.K_RIGHT
    esquerda = pygame.K_LEFT
    mudar_x = 0.0

    def __init__(self, size, fullscreen):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_size = self.screen.get_size()
        
        pygame.mouse.set_visible(0)
        pygame.display.set_caption('Fuga Espacial')
        
        my_font = pygame.font.Font('fonts/Fonte4.ttf', 100)
        self.render_text_bateuNaLateral = my_font.render('VOCÊ BATEU!', 0, (255, 255, 255))
        self.render_text_perdeu = my_font.render("GAME OVER!", 0, (255, 0, 0))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == self.esquerda:
                    self.mudar_x = -3
                if event.key == self.direita:
                    self.mudar_x = 3
            if event.type == pygame.KEYUP:
                if event.key == self.esquerda or event.key == self.direita:
                    self.mudar_x = 0

    def elements_update(self, dt):
        self.background.update(dt)

    def elements_draw(self):
        self.background.draw(self.screen)

    def loop(self):
        score = 0
        h_passou = 0

        self.background = Background()
        
        x = (self.width - 56) / 2
        y = self.height - 125
        
        self.player = Player(x, y)
        
        clock = pygame.time.Clock()
        dt = 16
        
        velocidade_background = 10
        velocidade_hazard = 10

        hzrd = 0
        h_x = random.randrange(125, 660)
        h_y = -550

        h_width = 100
        h_height = 110

        movL_x = 0
        movL_y = 0
        
        movR_x = 740
        movR_y = 0
        
        self.hazard.append(Hazard('images/satelite.png', h_x, h_y))
        self.hazard.append(Hazard('images/nave.png', h_x, h_y))
        self.hazard.append(Hazard('images/cometaVermelho.png', h_x, h_y))
        self.hazard.append(Hazard('images/meteoros.png', h_x, h_y))
        self.hazard.append(Hazard('images/buracoNegro.png', h_x, h_y))

        def score_card(screen, h_passou, score):
            font = pygame.font.SysFont(None, 35)
            passou = font.render('Passou: ' + str(h_passou), True, (255, 255, 128))
            score = font.render('Score: ' + str(score), True, (253, 231, 32))
            screen.blit(passou, (0, 50))
            screen.blit(score, (0, 100))

        while self.run:
            clock.tick(1000 / dt)

            self.background.move(self.screen, self.height, movL_x, movL_y, movR_x, movR_y)
            movL_y = movL_y + velocidade_background
            movR_y = movR_y + velocidade_background

            if movL_y > 600 and movR_y > 600:
                movL_y -= 600
                movR_y -= 600

            x = x + self.mudar_x
            
            self.player.draw(self.screen, x, y)
            score_card(self.screen, h_passou, score)

            if x > 760 - 92 or x < 40 + 5:
                text_rect = self.render_text_bateuNaLateral.get_rect(center = ((740 - 60) // 2 + 60, self.height // 2))
                self.screen.blit(self.render_text_bateuNaLateral, text_rect)
                pygame.display.update()  
                time.sleep(1.5)
                movL_y = 0
                movR_y = 0
                h_y = -550
                score = 0
                self.run = True

            self.hazard[hzrd].draw(self.screen, h_x, h_y)
            h_y = h_y + velocidade_hazard

            if h_y > self.height:
                h_y = 0 - h_height
                h_x = random.randrange(125, 650 - h_height)
                hzrd = random.randint(0, 4)
                h_passou = h_passou + 1
                score = h_passou * 10

            self.handle_events()
            self.elements_update(dt)
            
            pygame.display.update()
            clock.tick(120)

game = Game('resolution', 'fullscreen')
game.loop()
