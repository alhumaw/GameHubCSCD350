import pygame
import random
from enum import Enum
from options import options
from pygame import mixer


def start_snake(window):
    # Defining all the variables
    score_font = pygame.font.Font('res/fonts/chary___.ttf', 72)
    width = 1280
    height = 720
    pause = False
    mixer.init()
    death_sound = pygame.mixer.Sound('res/death_sound.mp3')
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")
    block_size = 20
    snake = Snake(block_size, window)
    food = Food(block_size, window)
    font = pygame.font.SysFont('res/fonts/chary___.ttf', 60, True)
    high_score = 0
    run = True
    # Main Running loop
    while run:
        pygame.time.delay(100)
        # Making sure the High score is correct
        if snake.length - 3 > high_score:
            high_score = snake.length - 3
        # Pausing the game then restarting
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape pressed")
                    pause = not pause
                    if pause:
                        state = options(window, pause)
                        if not state:
                            print()
        # Keys mapped
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            snake.steer(Direction.LEFT)
        elif keys[pygame.K_d]:
            snake.steer(Direction.RIGHT)
        elif keys[pygame.K_w]:
            snake.steer(Direction.UP)
        elif keys[pygame.K_s]:
            snake.steer(Direction.DOWN)
        # Game over Screen printed out
        if snake.check_bounds() or snake.check_tail_collision():
            death_sound.play()
            text = font.render('Game Over', True, (255, 255, 255))
            window.blit(text, (width / 2 - 100, height / 2))
            pygame.display.update()
            pygame.time.delay(1000)
            snake.respawn(100, 100)
            food.respawn()
        snake.move()
        snake.check_for_food(food)
        # Top of the screen leaderboard
        score_text = score_font.render(f"Snake Length: {snake.length - 3} High Score: {high_score}", True,
                                       (255, 255, 255))
        window.fill((0, 0, 0))
        # The window being built
        window.blit(score_text, (width / 2 - 480, 0))
        snake.draw(pygame, window)
        food.draw(pygame, window)
        pygame.display.update()


# Directions for updown left right
class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    # Local vars added
    mixer.init()
    apple_sound = pygame.mixer.Sound('res/apple_sound.mp3')
    length = None
    direction = None
    body = None
    block_size = None
    color = (0, 0, 255)
    bounds = None

    # Creating the snake __init__
    def __init__(self, block_size, play_area):
        self.block_size = block_size
        self.bounds = play_area.get_size()
        self.respawn(100, 100)

    # Respawn the snake at X,Y and back the length 3
    def respawn(self, start_x, start_y):
        self.length = 3
        self.body = [(start_x, start_y), (start_x, start_y + self.block_size),
                     (start_x, start_y + 2 * self.block_size)]
        self.direction = Direction.DOWN

    # Drawing the snake
    def draw(self, game, play_area):

        head_image = pygame.image.load(
            'res/stu.png')  # Replace 'path_to_head_image.png' with the actual image file path for the head
        segment_image = pygame.image.load(
            'res/potato.png')  # Replace 'path_to_segment_image.png' with the actual image file path for the segments

        # Scale the images to the desired size
        scaled_head_image = pygame.transform.scale(head_image, (self.block_size * 2, self.block_size * 2))
        scaled_segment_image = pygame.transform.scale(segment_image, (self.block_size * 2, self.block_size * 2))

        # Draw the head image

        play_area.blit(scaled_head_image, (self.body[0][0], self.body[0][1]))
        # Draw the segment images
        for segment in self.body[1:]:
            play_area.blit(scaled_segment_image, (segment[0], segment[1]))

    # Choosing what direction to move
    def steer(self, direction):
        if self.direction == Direction.DOWN and direction != Direction.UP:
            self.direction = direction
        elif self.direction == Direction.UP and direction != Direction.DOWN:
            self.direction = direction
        elif self.direction == Direction.LEFT and direction != Direction.RIGHT:
            self.direction = direction
        elif self.direction == Direction.RIGHT and direction != Direction.LEFT:
            self.direction = direction

    # Moving the snake in the chosen direction
    def move(self):
        curr_head = self.body[-1]
        if self.direction == Direction.DOWN:
            next_head = (curr_head[0], curr_head[1] + self.block_size)
            self.body.append(next_head)
        elif self.direction == Direction.UP:
            next_head = (curr_head[0], curr_head[1] - self.block_size)
            self.body.append(next_head)
        elif self.direction == Direction.RIGHT:
            next_head = (curr_head[0] + self.block_size, curr_head[1])
            self.body.append(next_head)
        elif self.direction == Direction.LEFT:
            next_head = (curr_head[0] - self.block_size, curr_head[1])
            self.body.append(next_head)

        if self.length < len(self.body):
            self.body.pop(0)

    # Growing the body by one and playing the sound when we hit the potato
    def eat(self):
        self.apple_sound.play()
        self.length += 1

    # Checks if we have eaten the food
    def check_for_food(self, food):
        head = self.body[-1]
        if head[0] == food.x and head[1] == food.y:
            self.eat()
            food.respawn()

    # Check if we are hitting our tail
    def check_tail_collision(self):
        head = self.body[-1]
        for i in range(len(self.body) - 1):
            segment = self.body[i]
            if head[0] == segment[0] and head[1] == segment[1]:
                return True
        return False

    # Checking if we are hitting the edges
    def check_bounds(self):
        head = self.body[-1]
        if head[0] >= self.bounds[0]:
            return True
        if head[1] >= self.bounds[1]:
            return True

        if head[0] < 0:
            return True
        if head[1] < 0:
            return True

        return False


class Food:
    # Local Vars
    block_size = None
    color = (255, 0, 0)
    x = 300
    y = 200
    bounds = None

    def __init__(self, block_size, window):
        self.block_size = block_size
        self.bounds = window.get_size()

    def draw(self, game, window):
        image = pygame.image.load('res/potato.png')  # Replace 'path_to_your_image.png' with the actual image file path
        # Scale the image to the desired size
        scaled_image = pygame.transform.scale(image, (self.block_size * 2, self.block_size * 2))
        # Draw the image on the window at the specified position
        window.blit(scaled_image, (self.x, self.y))

    # Respawn the food
    def respawn(self):
        blocks_in_x = (self.bounds[0]) // self.block_size
        blocks_in_y = (self.bounds[1]) // self.block_size
        self.x = random.randint(0, blocks_in_x - 1) * self.block_size
        self.y = random.randint(0, blocks_in_y - 1) * self.block_size
