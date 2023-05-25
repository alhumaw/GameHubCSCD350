import pygame
import random
from enum import Enum
from options import options
from pygame import mixer


def start_snake(window):
    score_font = pygame.font.Font('res/fonts/chary___.ttf', 72)
    width = 1280
    height = 720
    pause = False
    mixer.init()
    death_sound = pygame.mixer.Sound('res/death_sound.mp3')

    bound_width = 1000
    bound_height = 700

    retx = int((width - bound_width) / 2)
    rety = int((height - bound_height) / 2)

    play_area = pygame.display.set_mode((retx, rety))
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")

    block_size = 20
    snake = Snake(block_size, play_area, retx, rety)
    food = Food(block_size, play_area, retx, rety)
    font = pygame.font.SysFont('comicsans', 60, True)
    high_score = 0
    run = True
    while run:
        pygame.time.delay(100)
        if snake.length - 3 > high_score:
            high_score = snake.length - 3
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape pressed")
                    pause = not pause
                    if pause:
                        state = options(window, pause)
                        if not state:
                            print()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake.steer(Direction.LEFT)
        elif keys[pygame.K_RIGHT]:
            snake.steer(Direction.RIGHT)
        elif keys[pygame.K_UP]:
            snake.steer(Direction.UP)
        elif keys[pygame.K_DOWN]:
            snake.steer(Direction.DOWN)

        if snake.check_bounds() or snake.check_tail_collision():
            death_sound.play()
            text = font.render('Game Over', True, (255, 255, 255))
            window.blit(text, (width / 2, height / 2))
            pygame.display.update()
            pygame.time.delay(1000)
            snake.respawn(retx, rety)
            food.respawn()
        snake.move()
        snake.check_for_food(food)

        score_text = score_font.render(f"Snake Length: {snake.length - 3} High Score: {high_score}", True,
                                       (255, 255, 255))
        window.fill((0, 0, 0))
        pygame.draw.rect(window, (0, 255, 0), (retx, rety, bound_width, bound_height))
        window.blit(score_text, (width / 2 - 400, 0))
        snake.draw(pygame, play_area)
        food.draw(pygame, play_area)
        pygame.display.update()


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    mixer.init()
    apple_sound = pygame.mixer.Sound('res/apple_sound.mp3')
    retx = 0
    rety = 0
    length = None
    direction = None
    body = None
    block_size = None
    color = (0, 0, 255)
    bounds = None
    starting_point = (100, 100)

    def __init__(self, block_size, play_area, retx, rety):
        self.block_size = block_size
        self.bounds = play_area
        self.respawn(retx, rety)

    def respawn(self, start_x, start_y):
        self.length = 3
        self.body = [(start_x, start_y), (start_x, start_y + self.block_size),
                     (start_x, start_y + 2 * self.block_size)]
        self.direction = Direction.DOWN

    def draw(self, game, play_area):
        for segment in self.body:
            game.draw.rect(play_area, self.color, (segment[0], segment[1], self.block_size, self.block_size))

    def steer(self, direction):
        if self.direction == Direction.DOWN and direction != Direction.UP:
            self.direction = direction
        elif self.direction == Direction.UP and direction != Direction.DOWN:
            self.direction = direction
        elif self.direction == Direction.LEFT and direction != Direction.RIGHT:
            self.direction = direction
        elif self.direction == Direction.RIGHT and direction != Direction.LEFT:
            self.direction = direction

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

    def eat(self):
        self.apple_sound.play()
        self.length += 1

    def check_for_food(self, food):
        head = self.body[-1]
        if head[0] == food.x and head[1] == food.y:
            self.eat()
            food.respawn()

    def check_tail_collision(self):
        head = self.body[-1]
        for i in range(len(self.body) - 1):
            segment = self.body[i]
            if head[0] == segment[0] and head[1] == segment[1]:
                return True
        return False

    def check_bounds(self):
        head = self.body[-1]
        if head[0] >= self.bounds[0] - self.block_size:
            return True
        if head[1] >= self.rety + self.bounds[1] - self.block_size:
            return True
        if head[0] < self.retx:
            return True
        if head[1] < self.rety:
            return True
        return False


class Food:
    block_size = None
    color = (255, 0, 0)
    x = 0
    y = 0
    bounds = None
    retx = 0
    rety = 0

    def __init__(self, block_size, play_area, retx, rety):
        self.block_size = block_size
        self.bounds = play_area.get_size()
        self.rety = rety
        self.retx = retx

    def draw(self, game, play_area):
        game.draw.rect(play_area, self.color, (self.x, self.y, self.block_size, self.block_size))

    def respawn(self):
        blocks_in_x = (self.bounds[0] - self.retx - self.block_size) // self.block_size
        blocks_in_y = (self.bounds[1] - self.rety - self.block_size) // self.block_size
        self.x = random.randint(0, blocks_in_x - 1) * self.block_size + self.retx
        self.y = random.randint(0, blocks_in_y - 1) * self.block_size + self.rety
