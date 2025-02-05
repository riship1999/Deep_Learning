import pygame
import random
from collections import deque

# Initialize Pygame
pygame.init()

# Set window dimensions
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Simple Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake initial position and size
snake_x = window_width // 2
snake_y = window_height // 2
snake_size = 10
snake_list = deque()
snake_length = 1

# Food initial position
food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0

# Game variables
game_over = False
x_change = 0
y_change = 0
clock = pygame.time.Clock()
snake_speed = 15
score = 0

# Function to display the snake
def display_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(window, green, [x, y, snake_size, snake_size])

# Function to display the score
def display_score(score):
    font_style = pygame.font.SysFont(None, 30)
    score_text = font_style.render("Score: " + str(score), True, white)
    window.blit(score_text, [0, 0])

# Function to display messages
def message(msg, color):
    font_style = pygame.font.SysFont(None, 30)
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [window_width / 6, window_height / 3])

# Function to generate food at a valid location
def generate_food(snake_list):
    while True:
        food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0
        if (food_x, food_y) not in snake_list:
            return food_x, food_y

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_change != snake_size:
                x_change = -snake_size
                y_change = 0
            elif event.key == pygame.K_RIGHT and x_change != -snake_size:
                x_change = snake_size
                y_change = 0
            elif event.key == pygame.K_UP and y_change != snake_size:
                y_change = -snake_size
                x_change = 0
            elif event.key == pygame.K_DOWN and y_change != -snake_size:
                y_change = snake_size
                x_change = 0

    # Check for boundaries
    if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
        game_over = True

    snake_x += x_change
    snake_y += y_change

    window.fill(black)

    # Generate food if eaten
    if snake_x == food_x and snake_y == food_y:
        food_x, food_y = generate_food(snake_list) #Call the new function
        snake_length += 1
        score += 1

    pygame.draw.rect(window, red, [food_x, food_y, snake_size, snake_size])

    snake_head = (snake_x, snake_y)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        snake_list.popleft()

    # Self-collision detection
    for x, y in list(snake_list)[:-1]:
        if x == snake_x and y == snake_y:
            game_over = True

    display_snake(snake_list)
    display_score(score)
    pygame.display.update()

    clock.tick(snake_speed)

message("Game Over!", red)
pygame.display.update()
pygame.time.delay(2000)
pygame.quit()
quit()
