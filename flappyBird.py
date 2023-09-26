import pygame
import neat
import time
import os 
import random

WIN_WIDTH = 500
WIN_HEIGHT = 800

BIRD1 = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png")))
BIRD2 = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png")))
BIRD3 = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))

BIRD_IMGS = [BIRD1, BIRD2, BIRD3, BIRD2]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))


class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20 #how much we rotate on each frame
    ANIMATION_TIME = 5 #how long we show each animation

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]
    
    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y
    
    def move(self):
        self.tick_count += 1

        #displacement
        d = self.vel*self.tick_count + 1.5*self.tick_count**2
        if d >= 16: 
            d = 16
        if d < 0:
            d -= 2
        self.y += d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL
    
    def draw(self, win):
        self.img_count += 1

        if self.img_count == self.ANIMATION_TIME*len(self.IMGS):
            self.img_count = 0
        self.img = self.IMGS[self.img_count // self.ANIMATION_TIME]

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

        # ANIMATION IMPLEMENTATION GIVEN IMGS[0-2]
        #1 2 3 4 // 5 6 7 8 9 // 10 11 12 13 14 // 15 16 17 18 19 // 21
        #0          1           2                   1               0
        
        # if self.img_count < self.ANIMATION_TIME:
        #     self.img = self.IMGS[0]
        # elif self.img_count < self.ANIMATION_TIME*2:
        #     self.img = self.IMGS[1]
        # elif self.img_count < self.ANIMATION_TIME*3:
        #     self.img = self.IMGS[2]
        # elif self.img_count < self.ANIMATION_TIME*4:
        #     self.img = self.IMGS[1]
        # elif self.img_count == self.ANIMATION_TIME*4 + 1:
        #     self.img = self.IMGS[0]
        #     self.image_count = 0 

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


def draw_window(win, bird):
    win.blit(BG_IMG, (0,0))
    bird.draw(win)
    pygame.display.update()

def main():
    bird = Bird(200,200)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(win, bird)

    pygame.quit()
    quit()

main()