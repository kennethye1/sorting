import pygame, sys
import random

RED = (255, 0, 0)
TURQUOISE = (41, 216, 216)
WHITE = (255, 255, 255)
pygame.init()
WIDTH = 1000
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


class Bar:
    def __init__(self, value, width, pos):
        self.value = value
        self.width = width
        self.height = height
        self.pos = pos
        self.rect = pygame.draw.Rect(pos, (self.width, self.height))
        self.color = TURQUOISE

    def draw(self, screen):
        pygame.draw.Rect(screen, self.color, self.rect)

    def chosen(self):
        self.color = RED
    
    def reset(self):
        self.color = TURQUOISE
    
def bubble_sort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = arr[j]
                swap = True
        if not swap:
            break


def main(screen, n, bar_width):
    screen.fill(WHITE)
    arr = [Bar(random.randint(1, HEIGHT), bar_width, (0, i*bar_width)) for i in range(n)]

    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if even

        pygame.display.update()

main(SCREEN, 10, WIDTH//10)
    
    
