import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Snake initial position and direction
snake_head = [GRID_WIDTH // 2, GRID_HEIGHT // 2]
snake_body = [snake_head]
snake_direction = [0, 0]  # [dx, dy]

# Food initial position
food_position = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = [0, -1]
            elif event.key == pygame.K_DOWN:
                snake_direction = [0, 1]
            elif event.key == pygame.K_LEFT:
                snake_direction = [-1, 0]
            elif event.key == pygame.K_RIGHT:
                snake_direction = [1, 0]

    # Move the snake
    new_head = [snake_head[0] + snake_direction[0], snake_head[1] + snake_direction[1]]
    snake_body.insert(0, new_head)

    # Check if the snake ate the food
    if snake_head == food_position:
        food_position = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]
    else:
        snake_body.pop()

    # Check for collisions
    if (new_head in snake_body[1:]) or (new_head[0] < 0 or new_head[0] >= GRID_WIDTH) or (new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
        pygame.quit()
        sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the food
    pygame.draw.rect(screen, GREEN, (food_position[0] * GRID_SIZE, food_position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.flip()

    # Control game speed
    pygame.time.delay(100)
