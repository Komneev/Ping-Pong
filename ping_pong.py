import pygame
pygame.init()
dark = (0,0,0)
ww = pygame.display.set_mode((500, 500))
back = (243, 224, 82)
black = (0,0,0)
ww.fill(back)
kryt_x = 200
kryt_y = 330
game_over = False
class Area():
    def __init__(self, x=0, y=0, weight=10,height=10):
        self.rect = pygame.Rect(x, y, weight, height)
        self.fill_color = back
    def draw(self):
        pygame.draw.rect(ww, self.fill_color, self.rect)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    def fill(self):
        pygame.draw.rect(ww, self.fill_color, self.rect)
class Label(Area):
    def text_tep(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text,True, text_color)
    def draw1(self, shift_x = 0, shift_y = 0):
        ww.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
platform_x = 300
platform_y = 160
ball_x = 220
ball_y = 100
tue = pygame.time.Clock()
class Picture(Area):
    def __init__(self,filename,x=10, y=10, weight=10, height=10):
        Area.__init__(self, x=x, y=y, weight=weight, height=height)
        self.image = pygame.image.load(filename)
    def draw(self):
        ww.blit(self.image, (self.rect.x, self.rect.y))
myach = Picture('ball.png', ball_x, ball_y, 50, 50)
platforma = Picture('platform.png', platform_x, platform_y, 100, 30)
count = 9
start_x = 5
start_y = 5
speed_x = 3
speed_y = 3
move_right = False
move_left = False
while not game_over:
    myach.fill()
    platforma.fill()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                move_right = True
            if event.key == pygame.K_z:
                move_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_x:
                move_right = False
            if event.key == pygame.K_z:
                move_left = False
    if myach.rect.y > (platform_y + 20):
        time_text = Label(150, 150, 50, 50)
        time_text.text_tep('Проиграл, хех', 60, (255,0,0))
        time_text.draw1()
        game_over = True
    if move_right:
        platforma.rect.x += 3
    if move_left:
        platforma.rect.x -= 3
    if myach.colliderect(platforma.rect):
        speed_y *= -1
    if myach.rect.y < 0:
        speed_y *= -1
    if myach.rect.x > 450 or myach.rect.x < 0:
        speed_x *= -1
    
    myach.rect.x += speed_x
    myach.rect.y += speed_y

    myach.draw()
    platforma.draw()
