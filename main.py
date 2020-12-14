import pygame
import random
import math

# init pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((800, 600))

# Title and icon of our game
pygame.display.set_caption("Balloon Shooting Game")
icon = pygame.image.load("balloon.png")
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load("rocket.png")
player_x = 720
player_y = 300
player_y_change = 0

# Balloon
balloon_img = pygame.image.load("balloon_g.png")
balloon_x = 0
balloon_y = random.randint(0, 600)
balloon_y_change = 0.3
balloon_x_change = 0

# Dart
dart_img = pygame.image.load("dart.png")
dart_x = 740
dart_y = 300

dart_x_change = 0.3 * 1.5
dart_state = "ready"

# Times fired

times_fired = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10


def show_times_fired(x, y):
    score = font.render("Times Fired:" + str(times_fired), True, (0, 0, 0))
    screen.blit(score, (x, y))


score = 0
fired_times = 0

def player(x, y):
    screen.blit(player_img, (x, y))


def balloon(x, y):
    screen.blit(balloon_img, (x, y))


def fire_dart(x, y):
    global dart_state
    dart_state = "fire"
    screen.blit(dart_img, (x + 6, y + 20))


def is_collision(balloon_x, balloon_y, dart_x, dart_y):
    distance = math.sqrt(math.pow(balloon_x - dart_x, 2) + (math.pow(balloon_y - dart_y, 2)))
    if distance < 27:
        return True
    else:
        return False


def show_you_won(x, y):
    msg = font.render("You won! It took you " + str(times_fired), True, (0, 0, 0))
    screen.blit(msg, (x, y))


# Game Loop
running = True
while running:

    # Background color of the game window in RGB
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Update Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_y_change = 0.2
            if event.key == pygame.K_UP:
                player_y_change = -0.2
            if event.key == pygame.K_SPACE:
                if dart_state is "ready":
                    # Gets the Y cord of the player
                    dart_y = player_y
                    fire_dart(dart_x, dart_y)
                    times_fired += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or pygame.K_UP:
                player_y_change = 0

    # Player movement
    player_y += player_y_change
    # Restricts Player from leaving the screen
    if player_y > 536:
        player_y = 536
    elif player_y < 0:
        player_y = 0

    # Balloon movement
    balloon_y += balloon_y_change
    balloon_x += balloon_x_change

    # Restricts balloon from leaving the screen
    if balloon_y >= 536:
        balloon_y_change = -0.3
    elif balloon_x >= 720:
        balloon_x_change = -0.3
    elif balloon_y <= 0:
        balloon_y_change = 0.3
    elif balloon_x <= 0:
        balloon_x_change = 0.3

    # Dart movement
    if dart_x <= 0:
        dart_x = 740
        dart_state = "ready"

    if dart_state is "fire":
        fire_dart(dart_x, dart_y)
        dart_x -= dart_x_change

    if dart_state is "fin":
        dart_x = 740

    collision = is_collision(balloon_x, balloon_y, dart_x, dart_y)
    if collision:
        dart_x_change = 0
        balloon_x_change = 0
        balloon_y_change = 0
        show_you_won(100, 100)

    player(player_x, player_y)
    balloon(balloon_x, balloon_y)

    show_times_fired(text_x, text_y)
    pygame.display.update()
    #more
