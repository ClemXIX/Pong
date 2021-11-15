# https://www.youtube.com/watch?v=Qf3-aDXG8q4

import pygame, sys, random


# functions who will be used in the game loop

def ball_animation():

    global ball_speed_x, ball_speed_y

    # movements each frame
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # when the ball touch one side of the screen, reverse the axis, like this the ball stay inside the window
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    # if the ball touch player or opponent side, the ball goes in the middle
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():
    player.y += player_speed
    # the player can't leave the screen if he try to move to far, he come back to the max of the sides
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    if opponent.top <= 0:
        opponent.top = 0


def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

# Create the game


pygame.init()
clock = pygame.time.Clock()

# constants for the window
screen_width = 1280
screen_height = 960

# create the window and name it
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# rectangle for the ball, W and H / 2 will not put them exactly in the center, but put the top left of the rect centred
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 -15, 30, 30)
player = pygame.Rect(screen_width -20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

# colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# constants for the speed
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

# main loop
while True:
    # event are the input of the player
    for event in pygame.event.get():
        # explicit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # pygame input work like :when pressed, and when released
        # so must handle the 2 situation, for pong, when player when to go up he pressed up till he want to stop

        # if the input is pressed, change the rectangle of the player to 7pixel each frame till the key is down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_ai()

    # initialize the object into the window in order, first line is create before the other,
    # first the background, then the player / oppment, then the ball
    # pygame.draw take the shape and three argument :
    # the surface to draw
    # the color (rgb), or name of the color
    # the Rectangle to draw
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)

    # anti aliasing line is a smooth line
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))

    pygame.display.flip()
    clock.tick(60)

