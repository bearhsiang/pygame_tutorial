import pygame

g = 1

class player(object):
    def __init__(self,x,y,size, img = None):
        self.x = x
        self.y = y
        self.size = size
        self.v = [0, 0]
        self.img = img


    def draw(self, win):
        if self.img:
            img = self.img
            ### 2.
            if self.v[0] < 0:
                img = pygame.transform.flip(img, 1, 0)
            win.blit(img, (self.x, self.y))
        else:
            pygame.draw.rect(win, (255, 0, 0), pygame.Rect(self.x, self.y, self.size[0], self.size[1]))


    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.v[0] = -4
        elif keys[pygame.K_RIGHT]:
            self.v[0] = 4
        else:
            self.v[0] = 0

        ### 3.
        if keys[pygame.K_SPACE]:
            self.v[1] = -10
    
    def move(self):
        self.x += self.v[0]
        self.y += self.v[1]
        

        ## TODO 3: add jump
        self.v[1] += g
        if self.y > h-self.size[1]:
            self.y = h-self.size[1]
            self.v[1] = 0

def GameWindowUpdate(win, man, bg = None):
    
    if bg:
        win.blit(bg, (0, 0))
    else:
        win.fill((0, 0, 0))
    
    man.draw(win)
    pygame.display.update()

## initial the game
pygame.init()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption("First Game")
w = win.get_width()
h = win.get_height()

## TODO 1. add background image and music

bg = pygame.image.load('../imgs/bg.jpg')
bg = pygame.transform.scale(bg, (w, h))
print('type of img', type(bg))

## TODO 4. add bgm
pygame.mixer.music.load('../audio/music.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

## TODO 2. add player image
player_img = pygame.image.load('../imgs/stand.png')
r = 3
player_img = pygame.transform.scale(player_img, (player_img.get_width()*r, player_img.get_height()*r))

man = player(w//2, h-player_img.get_height(), player_img.get_size(), player_img)
run = True

while run:  ## main looop
    clock.tick(50)

    ### a. get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    ### b. update status
    if keys[pygame.K_q]:
        run = False
        break
    man.update(keys)
    man.move()
            
    ### c. draw on windows
    GameWindowUpdate(win, man, bg)

pygame.quit()