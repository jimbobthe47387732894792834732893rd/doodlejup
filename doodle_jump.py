import pygame
pygame.init()

# configuration variables
SCREEN_WIDTH = 500
SCREEN_HEIGHT = SCREEN_WIDTH * 1.5

# pygame setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#FFF1DC")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen,"green",(250,250,SCREEN_WIDTH / 7,SCREEN_WIDTH / 6))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()