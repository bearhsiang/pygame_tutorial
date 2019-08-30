import pygame

g = 1

class player(object):
    def __init__(self,x,y,size, imgs = None):
        self.x = x
        self.y = y
        self.size = size
        self.v = [0, 0]
        self.imgs = imgs
        self.clock = 0

    def draw(self, win):
        if self.imgs:

            if self.v[0] == 0:
                img = self.get_img('idle')
            else:
                img = self.get_img('run')

            ### 2.
            if self.v[0] < 0:
                img = pygame.transform.flip(img, 1, 0)
            win.blit(img, (self.x, self.y))
        else:
            pygame.draw.rect(win, (255, 0, 0), pygame.Rect(self.x, self.y, self.size[0], self.size[1]))

    def get_img(self, key):
        index = (self.clock%(3*len(self.imgs[key])))//len(self.imgs[key])
        return self.imgs[key][index]

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

        self.clock += 1

def GameWindowUpdate(win, man, bg = None):
    
    if bg:
        win.blit(bg, (0, 0))
    else:
        win.fill((0, 0, 0))
    
    man.draw(win)
    pygame.display.update()

def load_imgs(prefix, N, r):
    imgs = []
    for i in range(N):
        img = pygame.image.load(prefix+str(i)+'.png')
        img = pygame.transform.scale(img, (img.get_width()*r, img.get_height()*r))
        imgs.append(img)

    return imgs

## initial the game
pygame.init()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption("First Game")
w = win.get_width()
h = win.get_height()

## TODO 1. add background image and music
bg = pygame.Surface((w, h))
for i in range(1, 6):
    img = pygame.image.load('../imgs/multi-bg/plx-'+str(i)+'.png')
    img = pygame.transform.scale(img, (w, h))
    bg.blit(img, (0, 0))
# bg = pygame.image.load('../imgs/bg.jpg')
print('type of img', type(bg))

## TODO 4. add bgm
pygame.mixer.music.load('../audio/music.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

## TODO 2. add player image
# player_imgs = []
# for i in range(11):
#     player_img = pygame.image.load('../sprites/idle-'+str(i)+'.png')
#     r = 3
#     player_img = pygame.transform.scale(player_img, (player_img.get_width()*r, player_img.get_height()*r))
#     player_imgs.append(player_img)

player_imgs = {
    'idle': load_imgs('../sprites/idle-', 12, 3),
    'run':  load_imgs('../sprites/run-', 8, 3)
}

man = player(w//2, h-player_imgs['idle'][0].get_height(), player_imgs['idle'][0].get_size(), player_imgs)
run = True

while run:  ## main loop
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