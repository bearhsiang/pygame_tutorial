import pygame

g = 3

class player(object):
    def __init__(self,x,y,width,height, imgs = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.v = [0, 0]
        self.imgs = imgs
        self.dir = 1


    def draw(self, win):
        if self.imgs:
            img = self.imgs[(count%(5*len(self.imgs)))//len(self.imgs)]
            if self.dir < 0:
                img = pygame.transform.flip(img, 1, 0)
            win.blit(img, (self.x, self.y))
        else:
            pygame.draw.rect(win, (255, 0, 0), pygame.Rect(self.x, self.y, self.width, self.height))


    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.dir = -1
            self.v[0] = -4
        elif keys[pygame.K_RIGHT]:
            self.dir = 1
            self.v[0] = 4
        else:
            self.v[0] = 0

        ### 3.
        if keys[pygame.K_SPACE]:
            self.v[1] = -10

    def move(self):
        self.x += self.v[0]
        self.y += self.v[1]
        
        self.v[1] += g
        if self.y > h-self.height:
            self.y = h-self.height
            self.v[1] = 0

def GameWindowUpdate(win, man, bg = None):
    
    if bg:
        win.blit(bg, (0, 0))
    else:
        print('no')
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
bg = pygame.Surface((w, h))
for i in range(1, 6):
    img = pygame.image.load('../Jungle Asset Pack/parallax background/plx-'+str(i)+'.png')
    img = pygame.transform.scale(img, (w, h))
    bg.blit(img, (0, 0))

pygame.mixer.music.load('audio/music.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

## TODO 2. add player image
player_imgs = []

for i in range(1, 11):
    img = pygame.image.load('../Jungle Asset Pack/Character/sprites/idle-'+str(i)+'.png')
    r = 2
    img = pygame.transform.scale(img, (img.get_width()*r, img.get_height()*r))
    player_imgs.append(img)

man = player(w//2, h-player_imgs[0].get_height(), player_imgs[0].get_width(), player_imgs[0].get_height(), player_imgs)
run = True

count = 0

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
    count += 1
pygame.quit()


