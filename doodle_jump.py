import pygame
import random
pygame.init()

# configuration variables
SCREEN_WIDTH = 500
SCREEN_HEIGHT = SCREEN_WIDTH * 1.5
PLAYER_WIDTH = SCREEN_WIDTH / 7
PLAYER_HEIGHT = SCREEN_WIDTH / 6
PLATFORM_WIDTH = 100
MAX_X_SPEED = 7

PLAYER_IMAGE_ORIGINAL = pygame.image.load("images/bin.png")
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE_ORIGINAL, (PLAYER_WIDTH, PLAYER_HEIGHT))

# pygame setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
player_y = 0
player_y_speed = 0
player_x = 0
player_x_speed = 0

# helper functions
def screen_to_game_coordinates(screen_coordinate):
    # screen_coordinate is an (x,y) pixel position
    return (
        screen_coordinate[0] - 250,    # x
        -(screen_coordinate[1] - 375)  # y
    )

def game_to_screen_coordinates(game_coordinate):
    # screen_coordinate is an (x,y) game position
    return (
        game_coordinate[0] + 250,   # x
        -game_coordinate[1] + 375  # y
    )

# classes
class Platform:
    def __init__(self, starting_y):
        self.x = random.randint(
            int(-SCREEN_WIDTH/2 + PLATFORM_WIDTH),
            int(SCREEN_WIDTH/2 - PLATFORM_WIDTH)
        )
        self.y = starting_y
    
    def bounce_touching_player(self):
        global player_y_speed
        if (
            player_y <= self.y + PLAYER_HEIGHT and
            player_y > -SCREEN_HEIGHT/2 and
            player_x < PLATFORM_WIDTH + self.x and
            player_x + PLAYER_WIDTH > self.x
        ):
            player_y_speed = 10
            self.x = random.randint(
                int(-SCREEN_WIDTH/2 + PLATFORM_WIDTH),
                int(SCREEN_WIDTH/2 - PLATFORM_WIDTH)
            )
            self.y += 10
    
    def draw(self):
        screen_position = game_to_screen_coordinates((self.x, self.y))
        pygame.draw.rect(screen,"green",(screen_position[0], screen_position[1], PLATFORM_WIDTH, SCREEN_WIDTH / 35))

platforms = [
    Platform(-SCREEN_HEIGHT/2 + 20),
    # Platform(-30),
    # Platform(-20),
    # Platform(-10),
    # Platform(0)
]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # get which keys are being pressed
    # player_x += player_x_speed
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        # move the player left
        player_x -= 6.7
        if player_x_speed < -MAX_X_SPEED:
            player_x_speed = -MAX_X_SPEED
        if player_x < -PLAYER_WIDTH:
            player_x = SCREEN_WIDTH
    if keys_pressed[pygame.K_RIGHT]:
        # move the player right
        player_x += 6.7
        if player_x_speed > MAX_X_SPEED:
            player_x_speed = MAX_X_SPEED
        if player_x > SCREEN_WIDTH:
            player_x = -PLAYER_WIDTH

    # make the player fall down
    player_y += player_y_speed
    player_y_speed -= 0.25

    # make the player bounce
    for platform in platforms:
        platform.bounce_touching_player()

    # fill the screen with a color to wipe away anything from last frame
    if player_y < -SCREEN_HEIGHT/2:
        screen.fill("#FFDCDC")
    else:
        screen.fill("#FFF1DC")

    # RENDER YOUR GAME HERE
    #pygame.draw.rect(screen,"green",(player_x,player_y,SCREEN_WIDTH / 7,SCREEN_WIDTH / 6))
    screen.blit(PLAYER_IMAGE, game_to_screen_coordinates((player_x,player_y)))
    for platform in platforms:
        platform.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60


pygame.quit()