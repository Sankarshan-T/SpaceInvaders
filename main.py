import pygame, sys, random
from game import Game


pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
OFFSET = 30

GREY = (29, 29, 27)
YELLOW = (243, 216, 63)

RESTART_EVENT = pygame.USEREVENT + 1

font = pygame.font.Font("Fonts/monogram.ttf", 40)
level_surface = font.render("LEVEL 01", False, YELLOW)
game_over_surface = font.render("GAME OVER", False, YELLOW)
score_text_surface = font.render("SCORE", False, YELLOW)
highscore_text_surface = font.render("HIGH-SCORE", False, YELLOW)

screen = pygame.display.set_mode((SCREEN_WIDTH + 2*OFFSET, SCREEN_HEIGHT + 2*OFFSET))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))


while True:
    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
            
        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()

        if event.type == MYSTERYSHIP and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))

        if event.type == RESTART_EVENT:
            game.reset()
            pygame.time.set_timer(RESTART_EVENT, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:
            pygame.time.set_timer(RESTART_EVENT, 10000)

            


    #Update: 
    if game.run:   
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()

    #Drawing
    screen.fill(GREY)

    #UI:
    pygame.draw.rect(screen, YELLOW, (OFFSET, OFFSET, SCREEN_WIDTH, SCREEN_HEIGHT), 2, 0, 60, 60, 60,60)
    pygame.draw.line(screen, YELLOW, (40, 670), (720, 670), 3)

    if game.run:
        screen.blit(level_surface, (550, 680, 50, 50))
    else:
        screen.blit(game_over_surface, (550, 680, 50, 50))

    x = 70
    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 680))
        x += 50

    screen.blit(score_text_surface, ((60, 40, 50, 50)))
    formatted_score = str(game.score).zfill(5)
    score_surface = font.render(formatted_score, False, YELLOW)
    screen.blit(score_surface, ((60, 65, 50, 50)))
    screen.blit(highscore_text_surface, (500, 40, 50, 50))
    formatted_highscore = str(game.highscore).zfill(5)
    highscore_surface = font.render(formatted_highscore, False, YELLOW)
    screen.blit(highscore_surface, (575, 65, 50, 50))


    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)

    pygame.display.update()
    clock.tick(60)

