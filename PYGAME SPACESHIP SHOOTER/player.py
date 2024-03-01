import pygame
from settings import fly, ship_engine, health, ship_death, font2, level, boss_level

# GRACZ
class Player(object):
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.vel = 9 
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.hitbox = (self.x + 50, self.y + 50, 94, 94)
        self.is_alive = True
        self.death_frame = 0
        self.death_animation = 0
        self.engine_frame = 0
        self.engine_animation = 0

    def draw(self, win):
        #if self.left or self.right or self.up or self.down:
        if self.is_alive:
            self.hitbox = (self.x + 50, self.y + 50, 94, 94)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            current_time = pygame.time.get_ticks()

            if self.left or self.right or self.up or self.down:
                if self.engine_frame >= len(ship_engine):
                        self.engine_frame = 0

                if self.engine_animation == 0:
                    self.engine_animation = current_time
                    self.engine_frame = 0
                
                if current_time - self.engine_animation > 100:
                    self.engine_frame += 1
                    self.engine_animation = current_time

                if self.engine_frame < len(ship_engine):
                    win.blit(ship_engine[self.engine_frame], (self.x, self.y))

            win.blit(fly, (self.x, self.y))
        #else: 
            #win.blit(fly, (self.x, self.y))

            if self.health >= 500 and self.health <= 600:
                win.blit(health[0], (1700, 20))
                win.blit(health[0], (1750, 20))
                win.blit(health[0], (1800, 20))

            elif self.health >= 400 and self.health < 500:
                win.blit(health[0], (1700, 20))
                win.blit(health[0], (1750, 20))
                win.blit(health[1], (1800, 20))

            elif self.health >= 300 and self.health < 400:
                win.blit(health[0], (1700, 20))
                win.blit(health[0], (1750, 20))
                win.blit(health[2], (1800, 20))

            elif self.health >= 200 and self.health < 300:
                win.blit(health[0], (1700, 20))
                win.blit(health[1], (1750, 20))
                win.blit(health[2], (1800, 20))

            elif self.health >= 100 and self.health < 200:
                win.blit(health[0], (1700, 20))
                win.blit(health[2], (1750, 20))
                win.blit(health[2], (1800, 20))

            elif self.health > 0 and self.health < 100:
                win.blit(health[1], (1700, 20))
                win.blit(health[2], (1750, 20))
                win.blit(health[2], (1800, 20))

            elif self.health <= 0:
                win.blit(health[2], (1700, 20))
                win.blit(health[2], (1750, 20))
                win.blit(health[2], (1800, 20))
                self.is_alive = False
                

        elif self.is_alive == False and self.health <= 0:
            win.blit(health[2], (1700, 20))
            win.blit(health[2], (1750, 20))
            win.blit(health[2], (1800, 20))
            current_time = pygame.time.get_ticks()
            if self.death_animation == 0:
                self.death_animation = current_time
                self.death_frame = 0
            
            if current_time - self.death_animation > 100:
                self.death_frame += 1
                self.death_animation = current_time

            if self.death_frame < len(ship_death):
                win.blit(ship_death[self.death_frame], (self.x, self.y))
            else:
                #animacja konca gry
                text1 = font2.render('GAME OVER!', 1, (255,255,255))
                win.blit(text1, (400, 500))

    def hit(self):
        #print('Enemy hit!')
        if self.health > 0:
            if level % boss_level == 0:
                self.health -= 75
            else:
                self.health -= 40
        elif self.health <= 0:
            self.is_alive = False