import pygame, sys
import random

RED = (255, 0, 0)
TURQUOISE = (41, 216, 216)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()
WIDTH = 1000
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


class Bar:
    def __init__(self, value, width, pos):
        self.value = value
        self.width = width
        self.pos = pos
        self.color = TURQUOISE

    def draw(self, screen):
        rect = pygame.Rect(self.pos, (self.width, self.value))
        pygame.draw.rect(screen, self.color, rect)
        pygame.draw.line(screen, WHITE, self.pos, (self.pos[0], self.pos[1]+self.value))
        pygame.draw.line(screen, WHITE, (self.pos[0]+self.width, self.pos[1]), (self.pos[0]+self.width, self.pos[1]+self.value))
        pygame.draw.line(screen, WHITE,(self.pos[0], self.pos[1]+self.value), (self.pos[0]+self.width, self.pos[1]+self.value))

    def chosen(self):
        self.color = RED
    
    def reset(self):
        self.color = TURQUOISE
    
def bubble_sort(arr, delay):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j].value > arr[j+1].value:
                arr[j].pos, arr[j+1].pos = arr[j+1].pos, arr[j].pos
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swap = True
            clear(SCREEN, arr)
            pygame.time.delay(delay)
            pygame.display.update()
              
        if not swap:
            break
    pygame.display.flip()
    
def clear(screen, arr):
    screen.fill(BLACK)
    for bar in arr:
        bar.draw(screen)

def merge_sort(arr, delay):
    if len(arr)> 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, delay)
        merge_sort(right, delay)

        i = l = r = 0
        while l < len(left) and r < len(right):
            if left[l].value < right[r].value:
                left[l].pos, arr[i+l].pos = arr[i].pos, left[l].pos
                arr[i] = left[l]
                l+=1

            else:
                right[r].pos, arr[mid+r].pos = arr[i].pos, right[r].pos
                arr[i] = right[r]
                r+=1
            i+=1
        print(arr[0].pos, arr[0].value)
        while l < len(left):
            #left[l].pos = arr[i].pos
            arr[i] = left[l]
            l+=1
            i+=1
        while r < len(right):
            right[r].pos = arr[i].pos
            arr[i] = right[r]
            r+=1
            i+=1
        clear(SCREEN, arr)
        pygame.time.delay(delay)
        pygame.display.update()


def main(screen, n):
    bar_width = WIDTH // n
    screen.fill(BLACK)
    arr = [Bar(random.randint(1, HEIGHT), bar_width, (bar_width*i, 0)) for i in range(n)]
    for bar in arr:
        bar.draw(screen)
    delay = 40
    pygame.display.update()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    bubble_sort(arr, delay)

                elif event.key == pygame.K_m:
                    for a in arr:
                        print(a.value)
                    merge_sort(arr, delay)
                    for a in arr:
                        print(a.pos)
        pygame.display.update()

main(SCREEN, 2)
    
    
