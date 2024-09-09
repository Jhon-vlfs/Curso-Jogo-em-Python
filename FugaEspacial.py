#Jogo: Fuga Espacial
#História: Um grupo de pessoas importantes para a salvação da humanidade escapam em uma nave danificada. A nave precisa desviar das ameaças até a zona segura.

import pygame

class Background:
    image = None
    margin_left = None
    margin_right = None

    def __init__(self):

        background_fig = pygame.image.load('teste-jogo-python/images/background.png')
        background_fig.convert()
        background_fig = pygame.transform.scale(background_fig, (800, 602))
        self.image = background_fig

        margin_left_fig = pygame.image.load('teste-jogo-python/images/margin_1.png')
        margin_left_fig.convert()
        margin_left_fig = pygame.transform.scale(margin_left_fig, (60, 602))
        self.margin_left = margin_left_fig

        margin_right_fig = pygame.image.load('teste-jogo-python/images/margin_2.png')
        margin_right_fig.convert()
        margin_right_fig = pygame.transform.scale(margin_right_fig, (60, 602))
        self.margin_right = margin_right_fig
    # __init__()



    def update(self, dt):
        pass
    # update()

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
        screen.blit(self.margin_left, (0, 0))
        screen.blit(self.margin_right, (740, 0))
    # draw()

    def move(self, screen, scr_height, movE_x, movE_y, movD_x, movD_y):

        for i in range(0, 2):
            screen.blit(self.image, (movE_x, (movE_y - (i * scr_height))))
            screen.blit(self.margin_left, (movE_x, (movE_y - (i * scr_height))))
            screen.blit(self.margin_right, (movD_x, (movD_y - (i * scr_height))))
    # move()
# Background

class Game:
    screen = None
    screen_size = None
    width = 800
    height = 600
    run = True
    background = None

    def __init__(self, size, fullscreen):
        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_size = self.screen.get_size()

        pygame.mouse.set_visible(0)
        pygame.display.set_caption('Fuga Espacial')
    # init()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
    # handle_events()

    def elements_update(self, dt):
        self.background.update(dt)
    # elements_update()

    def elements_draw(self):
        self.background.draw(self.screen)
    # elements_draw()

    def loop(self):
        # Criar plano de fundo
        self.background = Background()
        
        # Limitador de FPS do jogo
        clock = pygame.time.Clock()
        dt = 16
        
        # Movimentação do Background e margens
        velocidade_background = 10

        movE_x = 0
        movE_y = 0

        movD_x = 740
        movD_y = 0

        # Loop principal do programa
        while self.run:
            clock.tick(1000 / dt)

            # movimento ao background
            self.background.move(self.screen, self.height, movE_x, movE_y, movD_x, movD_y)
            movE_y = movE_y + velocidade_background
            movD_y = movD_y + velocidade_background

            # limite do movimento da tela
            if movE_y > 600 and movD_y > 600:
                movE_y -= 600
                movD_y -= 600

            self.handle_events()

            self.elements_update(dt)

            pygame.display.update()
            clock.tick(2000)
        # while self.run()
    # loop()
#Game

game = Game('resolution', 'fullscreen')
game.loop()