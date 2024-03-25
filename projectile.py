import pygame
from settings import attack

# POCISKI GRACZA
class Projectile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 15
        self.hitbox = (self.x, self.y, 32, 32)
        self.projectile_frame = 0
        self.projectile_animation = 0
    
    def draw(self, win):
        #win.blit(attack, (self.x, self.y))
        self.hitbox = (self.x, self.y, 32, 32)
        current_time = pygame.time.get_ticks()
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        if self.projectile_frame >= len(attack):
            self.projectile_frame = 0

        if self.projectile_animation == 0:
            self.projectile_animation = current_time
            self.projectile_frame = 0
                
        if current_time - self.projectile_animation > 100:
            self.projectile_frame += 1
            self.projectile_animation = current_time

        if self.projectile_frame < len(attack):
            win.blit(attack[self.projectile_frame], (self.x, self.y))