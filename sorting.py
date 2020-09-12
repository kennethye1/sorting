import pygame, sys
import random

RED = (255, 0, 0)
TURQUOISE = (41, 216, 216)
WHITE = (255, 255, 255)
DARKBLUE= (6, 30, 138)
BLACK = (0, 0, 0)
pygame.init()
WIDTH = 1000
HEIGHT = 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
speed = 3
font = pygame.font.SysFont('comicsans', 16)

def draw(colors, arr, screen, bar_width):
    x = 0
    for i in range(len(arr)):
        pygame.draw.rect(screen, colors[i], (x, 600 - arr[i], bar_width, arr[i]))
        pygame.draw.line(screen, WHITE, (x, 600 - arr[i]), (x+bar_width, 600-arr[i]))
        pygame.draw.line(screen, WHITE, (x, 600- arr[i]), (x, 600))
        pygame.draw.line(screen, WHITE, (x+bar_width, 600-arr[i]), (x+bar_width, 600))
        x += bar_width
    pygame.draw.line(screen, WHITE, (0, 600), (WIDTH, 600))
    pygame.display.update()

def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]

def delay():
    if speed == 2:
        pygame.time.delay(10)
    elif speed == 3:
        pygame.time.delay(25)
    elif speed == 4:
        pygame.time.delay(100)

def change_bar_color(arr, index, color, colors, bar_width):
    x_coord = index*bar_width
    pygame.draw.rect(SCREEN, color, (x_coord, 600-arr[index], bar_width, arr[index]))
    pygame.display.update()
    colors[index] = color

def change_speed(inc = True):
    global speed
    if inc and speed <= 4:
        speed += 1
    elif speed > 1 :
        speed -= 1  

def clear():
    pygame.draw.rect(SCREEN, BLACK, (0, 0, WIDTH, 600))

def bubble_sort(arr, bar_width, colors):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)- i- 1):
            pygame.event.pump()
            change_bar_color(arr, j, RED, colors, bar_width)
            change_bar_color(arr, j+1, RED, colors, bar_width)
            delay()
            if arr[j+1] < arr[j]:
                swap(arr, j, j+1)
                clear()
                draw(colors, arr, SCREEN, bar_width)
            change_bar_color(arr, j, TURQUOISE, colors, bar_width)
            change_bar_color(arr, j+1, TURQUOISE, colors, bar_width)

def selection_sort(arr, colors, bar_width):
    for i in range(len(arr)):
        curr_min = i
        for j in range(i+1, len(arr)):
            pygame.event.pump()
            change_bar_color(arr, j, RED, colors, bar_width)
            delay()
            if arr[j] < arr[curr_min]:
                change_bar_color(arr, curr_min, TURQUOISE, colors, bar_width)
                curr_min = j
                change_bar_color(arr, j, DARKBLUE, colors, bar_width)
            else:
                change_bar_color(arr, j, TURQUOISE, colors, bar_width)
            draw(colors, arr, SCREEN, bar_width)
        change_bar_color(arr, curr_min, TURQUOISE, colors, bar_width)
        if (curr_min != i):
            swap(arr, i, curr_min)
        clear()
        draw(colors, arr, SCREEN, bar_width)


def merge_sort(arr, left, right, colors, bar_width):
    delay()
    mid = (left + right)//2
    if left < right:
        merge_sort(arr, left, mid, colors, bar_width)
        merge_sort(arr, mid+1, right, colors, bar_width)
        merge(arr, left, mid, mid+1, right, colors, bar_width)

def merge(arr, left, mid_l, mid_r, right, colors, bar_width):
    temp = []
    i, j = left, mid_r
    pygame.event.pump()
    while i <= mid_l and j <= right:
        change_bar_color(arr, i, RED, colors, bar_width)
        change_bar_color(arr, j, RED, colors, bar_width)
        clear()
        draw(colors, arr, SCREEN, bar_width)
        delay()
        change_bar_color(arr, i, TURQUOISE, colors, bar_width)
        change_bar_color(arr, j, TURQUOISE, colors, bar_width)
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while i <= mid_l:
        change_bar_color(arr, i, RED, colors, bar_width)
        clear()
        draw(colors, arr, SCREEN, bar_width)
        delay()
        change_bar_color(arr, i, TURQUOISE, colors, bar_width)
        temp.append(arr[i])
        i+=1
    while j <= right:
        change_bar_color(arr, j, RED, colors, bar_width)
        clear()
        draw(colors, arr, SCREEN, bar_width)
        delay()
        change_bar_color(arr, j, TURQUOISE, colors, bar_width)
        temp.append(arr[j])
        j+=1

    k = 0    

    for i in range(left, right+1):
        pygame.event.pump()
        arr[i] = temp[k]
        k+=1
        clear()
        draw(colors, arr, SCREEN, bar_width)
        delay()

def quick_sort(arr, lo, hi, colors, bar_width):
    if lo < hi:
        p = partition(arr, lo, hi,  colors, bar_width)
        quick_sort(arr, lo, p,  colors, bar_width)
        quick_sort(arr, p+1, hi, colors, bar_width)
    clear()
    draw(colors, arr, SCREEN, bar_width)

def partition(arr, lo, hi, colors, bar_width):
    pivot = arr[lo]
    i, j = lo-1, hi+1
    while True:
        pygame.event.pump()
        i+=1
        j-=1
        change_bar_color(arr, j, RED, colors, bar_width)
        draw(colors, arr, SCREEN, bar_width)
        delay()
        pygame.display.update()
        while arr[i] < pivot:
            change_bar_color(arr, i, TURQUOISE, colors, bar_width)
            draw(colors, arr, SCREEN, bar_width)
            delay()
            pygame.display.update()
            i+=1
        while arr[j] > pivot:
            change_bar_color(arr, j, TURQUOISE, colors, bar_width)
            draw(colors, arr, SCREEN, bar_width)
            delay()
            pygame.display.update()
            j-=1
        if i >= j:
            change_bar_color(arr, i, TURQUOISE, colors, bar_width)
            change_bar_color(arr, j, TURQUOISE, colors, bar_width)
            draw(colors, arr, SCREEN, bar_width)
            pygame.display.update()
            return j
        
        swap(arr, i, j)
        pygame.display.update()


#taken from https://stackoverflow.com/a/57558056
class Button(pygame.sprite.Sprite):
    def __init__(self, color, hover_col, rect, effect, outline = None, text = ""):
        super().__init__()
        self.text = text
        tmp_rect = pygame.Rect(0, 0, *rect.size)
        self.org = self.create(color, outline, text, tmp_rect)
        self.hov = self.create(hover_col, outline, text, tmp_rect)
        self.image = self.org
        self.rect = rect
        self.effect = effect
        
    def create(self, color, outline, text, rect):
        img = pygame.Surface(rect.size)
        if outline:
            img.fill(outline)
            img.fill(color, rect.inflate(-4, -4))
        else:
            img.fill(color)
        if text != "":
            text_surf = font.render(text, 1, WHITE)
            text_rect = text_surf.get_rect(center=rect.center)
            img.blit(text_surf, text_rect)
        return img
    def update(self, events):
        pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(pos)
        self.image = self.hov if hit else self.org
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and hit:
                self.effect(self)
    def change_eff(self, effect):
        self.effect = effect

def reset(arr, colors, n, screen, bar_width):
    screen.fill(BLACK)
    colors[:] = [TURQUOISE for i in range(n)]
    arr[:] = [random.randint(5, 600) for i in range(n)]
    draw(colors, arr, screen, bar_width)



def main(n, screen):
    
    screen.fill(BLACK)
    arr = [random.randint(5, 600) for i in range(n)]
    colors = [TURQUOISE for i in range(n)]
    bar_width =  WIDTH//n

    draw(colors, arr, screen, bar_width)
    sprites = pygame.sprite.Group()
    sprites.add(Button((222, 49, 193), (240, 72, 212), pygame.Rect(60, 620, 100, 40), lambda x: merge_sort(arr, 0, len(arr)-1, colors, bar_width), WHITE, "Mergesort", ))
    sprites.add(Button((222, 49, 193), (240, 72, 212), pygame.Rect(170, 620, 100, 40), lambda x: bubble_sort(arr, bar_width, colors), WHITE, "Bubblesort"))
    sprites.add(Button((222, 49, 193), (240, 72, 212), pygame.Rect(280, 620, 100, 40), lambda x: quick_sort(arr, 0, len(arr)-1, colors, bar_width), WHITE, "Quicksort"))
    sprites.add(Button((222, 49, 193), (240, 72, 212), pygame.Rect(390, 620, 100, 40), lambda x: selection_sort(arr, colors, bar_width), WHITE, "Selection Sort"))
    sprites.add(Button((154, 45, 227), (175, 101, 224), pygame.Rect(850, 610, 100, 30), lambda x: change_speed(True), WHITE, "Increase Speed"))
    sprites.add(Button((154, 45, 227), (175, 101, 224), pygame.Rect(850, 650, 100, 30), lambda x: change_speed(False), WHITE, "Decrease Speed"))
    sprites.add(Button((66, 135, 245), (128, 172, 242), pygame.Rect(720, 620, 120, 50), lambda x: reset(arr, colors, n, screen, bar_width), WHITE, "Reset"))
    
    running = True
    while running:
        for sprite in sprites:
            if sprite.text == "Mergesort":
                sprite.change_eff(lambda x: merge_sort(arr, 0, len(arr)-1, colors, bar_width))
            elif sprite.text == "Bubblesort":
                sprite.change_eff(lambda x: bubble_sort(arr, bar_width, colors))
            elif sprite.text == "Quicksort":
                sprite.change_eff(lambda x: quick_sort(arr, 0, len(arr)-1, colors, bar_width))
            elif sprite.text == "Selection sort":
                sprite.change_eff(lambda x: selection_sort(arr, colors, bar_width))

            elif sprite.text == "Increase Speed":
                sprite.change_eff(lambda x: change_speed(True))
            elif sprite.text == "Decrease Speed":
                sprite.change_eff(lambda x: change_speed(False))
            elif sprite.text == "Reset":
                sprite.change_eff(lambda x: reset(arr, colors, n, screen, bar_width))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    bubble_sort(arr, bar_width, colors)
                if event.key == pygame.K_m:
                    merge_sort(arr, 0, len(arr)-1, colors, bar_width)
        sprites.update(events)
        sprites.draw(screen)
        pygame.display.update()
        

main(40, SCREEN)  