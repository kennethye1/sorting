import pygame 

RED = (255, 0, 0)
TURQUOISE = (41, 216, 216)
pygame.init()
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Bar:
    def __init__(self, value, width, height, pos, color):
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
    
def bubble_sort(list):
