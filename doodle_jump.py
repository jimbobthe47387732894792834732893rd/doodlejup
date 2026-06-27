import pygame
pygame.init()

# configuration variables
SCREEN_WIDTH = 500
SCREEN_HEIGHT = SCREEN_WIDTH * 1.5
PLAYER_WIDTH = SCREEN_WIDTH / 7
PLAYER_HEIGHT = SCREEN_WIDTH / 6
MAX_X_SPEED = 7

# pygame setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
player_y = 250
player_y_speed = 0
player_x = 250
player_x_speed = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # get which keys are being pressed
    player_x += player_x_speed
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        # move the player left
        player_x_speed -= 0.05
        if player_x_speed < -MAX_X_SPEED:
            player_x_speed = -MAX_X_SPEED
        if player_x < -PLAYER_WIDTH:
            player_x = SCREEN_WIDTH
    if keys_pressed[pygame.K_RIGHT]:
        # move the player right
        player_x_speed += 0.05
        if player_x_speed > MAX_X_SPEED:
            player_x_speed = MAX_X_SPEED
        if player_x > SCREEN_WIDTH:
            player_x = -PLAYER_WIDTH

    # make the player fall down
    player_y += player_y_speed
    player_y_speed += 0.2

    # make the player bounce
    if player_y >= 650 - PLAYER_HEIGHT:
        player_y_speed = -10

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#FFF1DC")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen,"green",(player_x,player_y,SCREEN_WIDTH / 7,SCREEN_WIDTH / 6))
    pygame.draw.rect(screen,"green",(0, 650,SCREEN_WIDTH,SCREEN_WIDTH / 35))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()