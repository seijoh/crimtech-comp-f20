import random
import pygame
import sys

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1,0),
    'r' : (1,0)
}


class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False
    eating_apple = False

    def __init__(self):
        pass

    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        self.direction = dir

    def collision(self, x, y):
        # TODO: See section 2, "Collisions", and section 4, "Self Collisions"
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            return True

        for i in range(1, len(self.body)):
            if self.body[i][0] == self.body[0][0] and self.body[i][1] == self.body[0][1]:
                return True

        return False

    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self, apple):
        # TODO: See section 1, "Move the snake!". You will be revisiting this section a few times.
        self.eating_apple = False
        current_pos = (0, 0)
        previous_pos = (0, 0)

        # moves each unit of the snake into previous location of preceding unit
        for i in range(len(self.body)):
            current_pos = (self.body[i][0], self.body[i][1])
            if i == 0:
                self.body[i] = (self.body[i][0] + DIR[self.direction][0], self.body[i][1] + DIR[self.direction][1])
            else:
                self.body[i] = (previous_pos[0], previous_pos[1])
            previous_pos = current_pos

        # check for collision
        if self.collision(self.body[0][0], self.body[0][1]) == True:
            self.kill()

        # check if eating apple and grow snake
        if self.get_head()[0] == apple.position[0] and self.get_head()[1] == apple.position[1]:
            self.eating_apple = True
            apple.place(self)
            self.l += 1
            self.body.append(previous_pos)

    def kill(self):
        # TODO: See section 11, "Try again!"
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)

    # implements feature #10 - wait for keypress to start game (any key)
    def wait_for_key(self):
        # TODO: see section 10, "wait for user input".
        start = False
        while not start:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    start = True


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self, snake):
        self.place(snake)

    def get_pos(self):
        return self.position

    # place apple at random location and check that not touching snake
    def place(self, snake):
        # TODO: see section 6, "moving the apple".
        touching_snake = True

        while (touching_snake == True):
            self.position = (rand_int(23), rand_int(23))
            touching_snake = False

            for i in snake.body:
                if i == self.position:
                    touching_snake = True
                    break

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    font = pygame.font.Font(pygame.font.get_default_font(), 16)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple(snake)

    score = 0
    speed = 5

    # show initial frozen game before keypress
    snake.draw(surface)
    apple.draw(surface)
    screen.blit(surface, (0,0))
    pygame.display.update()

    snake.wait_for_key()

    while True:
        # TODO: see section 10, "incremental difficulty".
        clock.tick(speed)
        snake.check_events()
        draw_grid(surface)
        snake.move(apple)
        score_display = font.render('%d' % score, True, (0, 0, 0))

        snake.draw(surface)
        apple.draw(surface)

        # TODO: see section 5, "Eating the Apple".
        # update score and speed when snake eats apple
        if snake.eating_apple:
            print('The snake ate an apple!')
            score += 1
            # implements feature #9 - make speed variable as score increases
            speed *= 1.1

        screen.blit(surface, (0,0))
        # TODO: see section 8, "Display the Score"
        screen.blit(score_display, (5,5))

        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()
