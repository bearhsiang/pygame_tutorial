import pygame

class player(object):
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.v = [0, 0]

    def draw(self, win):

        pygame.draw.rect(win, (255, 0, 0), pygame.Rect(self.x, self.y, self.size[0], self.size[1]))


    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.v[0] = -4
        elif keys[pygame.K_RIGHT]:
            self.v[0] = 4
        else:
            self.v[0] = 0

    def move(self):
        self.x += self.v[0]
        self.y += self.v[1]

def GameWindowUpdate(win, man):
    win.fill((0, 0, 0))
    man.draw(win)
    pygame.display.update()

## initial the game
pygame.init()

win = pygame.display.set_mode((800, 600))
print('type of win:', type(win))
pygame.display.set_caption("First Game")
w = win.get_width()
h = win.get_height()

clock = pygame.time.Clock()

man = player(200, 410, (64,64))
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
    GameWindowUpdate(win, man)

pygame.quit()
