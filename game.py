from pygame import *
from random import randint

width = 1000
height = 800
window = display.set_mode((width,height))
window.fill((66, 140, 32))
clock = time.Clock()
FPS = 60
color = (0,0,255)


class GameSprite(sprite.Sprite):
    def __init__(self,x_coor,y_coor,width,length,image=none,step):
        super().__init__()
        self.x = x_coor
        self.y = y_coor
        self.w = width
        self.l = length
        self.step = step
        self.body = image
        if self.body == None:
            self.rect = Rect(self.x,self.y,self.w,self.l)
        else:  
            self.persona = transform.scale(image.load(self.body),(self.w,self.l))
            self.rect = self.persona.get_rect()
    
    def resert(self):
        if self.body == None:
            draw.rect(window,color,self.rect)
        else:
            window.blit(self.persona,(self.x,self.y))

class player(GameSprite):
    def update_type_one(self):
        if going[K_UP] and self.y > 0:
            self.y -= self.step
        if going[K_DOWN] and self.y < height-self.w:
            self.y += self.step
    def update_type_one(self):
        if going[K_w] and self.y > 0:
            self.y -= self.step
        if going[K_s] and self.y < height-self.w:
            self.y += self.step



board_one = player()



game = True
stutus = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == MOUSEBUTTONDOWN:
            x,y = i.pos
            print(x,y)
    going = key.get_pressed()


    if stutus == True:
        pass


    else:
        window.fill(255,0,0)
    
    clock.tick(FPS)
    display.update()
