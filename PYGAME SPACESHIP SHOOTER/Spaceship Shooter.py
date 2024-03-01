import pygame
import random
import math
from settings import screenWidth, screenHeight, boss_image, boss_death, boss_attack, enemy_ship_image, enemy_death, enemy_attack, level, boss_level, font, font2, font3, font4, font5
from player import Player
from projectile import Projectile

pygame.init()

fps = 60
win = pygame.display.set_mode((screenWidth, screenHeight))

game_start_time = None
game_pause_time = None
start_delay = 3

health_amount = 600
shootCount = 0
shootLoop = 0
score = 0
index = -2
game_paused = False

enemy_bullets = []
enemy_bullets_to_remove = []
bullets = []
bullets_to_remove = []

in_menu = 0
in_game = 1
in_pause = 2
in_controls = 3
game_state = in_menu
previous_game_state = None

pygame.display.set_caption("Spaceship Shooter")
bg = pygame.image.load('background.png')

clock = pygame.time.Clock()

# BOSS
class boss(object):
    fly = pygame.transform.scale(boss_image, (384, 384))
    
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.hitbox = (self.x + 70, self.y + 35, 240, 280)
        self.vel_x = 5
        self.vel_y = 5
        self.direction = 1
        self.shoot_delay = random.randint(5, 10) * 1000
        self.last_shot_time = 0
        self.is_alive = True
        self.removed = False
        self.death_frame = 0
        self.death_animation = 0
        self.engine_frame = 0
        self.engine_animation = 0

    def draw(self, win):
        if self.is_alive:
            win.blit(boss.fly, (self.x, self.y))
            self.hitbox = (self.x + 70, self.y + 35, 240, 290)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        if self.is_alive == False and self.health <= 5:
            current_time = pygame.time.get_ticks()
            if self.death_animation == 0:
                self.death_animation = current_time
                self.death_frame = 0
            
            if current_time - self.death_animation > 100:
                self.death_frame += 1
                self.death_animation = current_time

            if self.death_frame < len(boss_death):
                win.blit(boss_death[self.death_frame], (self.x, self.y))

            if self.health == 0 and self.death_frame >= len(boss_death):
                self.removed = True

    def death_animation_finished(self):
        return self.is_alive == False and self.death_frame >= len(boss_death)

    def update(self):
        self.x += self.vel_x * self.direction
        self.y += self.vel_y * math.sin(pygame.time.get_ticks() / 2000)
        if self.x <= 50 or self.x >= 1600:
            self.direction *= -1
        if self.y <= 50 or self.y >= 400:
            self.vel_y *= -1

    def try_to_shoot(self):
        if game_state == in_game:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot_time > self.shoot_delay:
                self.shoot()
                self.last_shot_time = current_time
                self.shoot_delay = random.randint(1,2) * 1000

    def shoot(self):
        new_bullet = boss_projectile(self.x + 70 + self.width//2, self.y + 35 + self.height)
        enemy_bullets.append(new_bullet)
        #print('Enemy shoots!')

    def hit(self):
        #print('Player Hit')
        if self.health > 0:
            self.health -= 10
        elif self.health <= 0:
            self.is_alive = False

# POCISKI BOSSA
class boss_projectile(object):
    def __init__(self, x, y):
        self.x = x + 65
        self.y = y + 160
        self.vel = 12
        self.hitbox = (self.x, self.y, 48, 64)
        self.projectile_animation = 0
        self.projectile_frame = 0
    
    def draw(self, win):
        #win.blit(enemy_attack, (self.x, self.y))
        self.hitbox = (self.x, self.y, 48, 64)
        current_time = pygame.time.get_ticks()
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) 

        if self.projectile_frame >= len(boss_attack):
            self.projectile_frame = 0

        if self.projectile_animation == 0:
            self.projectile_animation = current_time
            self.projectile_frame = 0
                
        if current_time - self.projectile_animation > 100:
            self.projectile_frame += 1
            self.projectile_animation = current_time

        if self.projectile_frame < len(boss_attack):
            win.blit(boss_attack[self.projectile_frame], (self.x, self.y))

# PRZECIWNIK
class enemy(object):
    fly = pygame.transform.scale(enemy_ship_image, (128, 128))
    
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.hitbox = (self.x + 30, self.y + 30, 66, 64)
        self.vel_x = random.randint(4,7)
        self.vel_y = random.randint(4,7)
        self.direction = 1
        self.shoot_delay = random.randint(3, 6) * 1000
        self.last_shot_time = 0
        self.is_alive = True
        self.removed = False
        self.death_frame = 0
        self.death_animation = 0
        self.engine_frame = 0
        self.engine_animation = 0

    def draw(self, win):
        if self.is_alive:
            win.blit(enemy.fly, (self.x, self.y))
            self.hitbox = (self.x + 30, self.y + 30, 66, 64) #dla podstawowego enemy //Fighter
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        if self.is_alive == False and self.health <= 5:
            current_time = pygame.time.get_ticks()
            if self.death_animation == 0:
                self.death_animation = current_time
                self.death_frame = 0
            
            if current_time - self.death_animation > 100:
                self.death_frame += 1
                self.death_animation = current_time

            if self.death_frame < len(enemy_death):
                win.blit(enemy_death[self.death_frame], (self.x, self.y))

            if self.health == 0 and self.death_frame >= len(enemy_death):
                self.removed = True
        
    def death_animation_finished(self):
        return self.is_alive == False and self.death_frame >= len(enemy_death)

    def update(self):
        self.x += self.vel_x * self.direction
        self.y += self.vel_y * math.sin(pygame.time.get_ticks() / 1000)
        if self.x <= 50 or self.x >= 1830:
            self.direction *= -1
        if self.y <= 50 or self.y >= 600:
            self.vel_y *= -1



    def try_to_shoot(self):
        if game_state == in_game:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot_time > self.shoot_delay:
                self.shoot()
                self.last_shot_time = current_time
                self.shoot_delay = random.randint(3,6) * 1000

    def shoot(self):
        new_bullet = enemy_projectile(self.x + 17 + self.width//2, self.y + 25 + self.height)
        enemy_bullets.append(new_bullet)
        #print('Enemy shoots!')

    def hit(self):
        #print('Player Hit')
        if self.health > 0:
            self.health -= 10
        elif self.health <= 0:
            self.is_alive = False

# POCISKI PRZECIWNIKA
class enemy_projectile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 18
        self.hitbox = (self.x, self.y, 32, 32)
        self.projectile_animation = 0
        self.projectile_frame = 0
    
    def draw(self, win):
        #win.blit(enemy_attack, (self.x, self.y))
        self.hitbox = (self.x, self.y, 32, 32)
        current_time = pygame.time.get_ticks()
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) 

        if self.projectile_frame >= len(enemy_attack):
            self.projectile_frame = 0

        if self.projectile_animation == 0:
            self.projectile_animation = current_time
            self.projectile_frame = 0
                
        if current_time - self.projectile_animation > 100:
            self.projectile_frame += 1
            self.projectile_animation = current_time

        if self.projectile_frame < len(enemy_attack):
            win.blit(enemy_attack[self.projectile_frame], (self.x, self.y))

# RYSOWANIE
def redraw_game_window():
    win.blit(bg, (0,0))
    text = font.render('SCORE ' + str(score), 1, (255,255,255))
    win.blit(text, (20, 20))
    ship.draw(win)

    if game_state == in_game:
        for bullet in bullets:
            bullet.draw(win)
        
        for enemy in enemies:
            enemy.update()
            enemy.draw(win)

        for bullet in enemy_bullets:
            bullet.draw(win)

    pygame.display.update()

# GAME RESET
def reset_game():
    global ship, enemies, bullets, enemy_bullets, score, health_amount, level
    score = 0
    level = 0
    ship = Player(860, 860, 64, 64, health_amount)
    enemies = []
    bullets = []
    enemy_bullets = []

# MAIN MENU
def main_menu():
    win.blit(bg, (0,0))
    text = font4.render('SPACESHIP SHOOTER!', 1, (255,255,255))
    if index == 0:
        text1 = font3.render('START NEW GAME', 1, (85,206,255))
    else:
        text1 = font3.render('START NEW GAME', 1, (255,255,255))

    if index == 1:    
        text2 = font3.render('CONTROLS', 1, (85,206,255))
    else:
        text2 = font3.render('CONTROLS', 1, (255, 255, 255))

    if index == 2:
        text3 = font3.render('EXIT', 1, (85,206,255))
    else:
        text3 = font3.render('EXIT', 1, (255,255,255))
    win.blit(text, (100, 300))
    win.blit(text1, (550, 500))   #OCEAN 85, 206, 255
    win.blit(text2, (730, 600))
    win.blit(text3, (870, 700))
    pygame.display.update()

# CONTROLS
def controls():
    win.blit(bg, (0,0))
    text1 = font5.render('ARROW KEYS - YOU CAN NAVIGATE YOUR SHIP', 1, (255,255,255))
    text2 = font5.render('SPACEBAR - SHOOTING ROCKETS', 1, (255, 255, 255))
    text3 = font5.render('ESCAPE - GO BACK TO THE PREVIOUS WINDOW', 1, (255,255,255))
    text4 = font5.render('          OR PAUSE THE GAME', 1, (255,255,255))
    win.blit(text1, (100, 300))
    win.blit(text2, (100, 400))
    win.blit(text3, (100, 500))
    win.blit(text4, (100, 600))
    pygame.display.update()

# PAUSE
def pause():
    win.blit(bg, (0,0))
    if index == 0:
        text1 = font5.render('RESUME THE GAME', 1, (85,206,255))
    else:
        text1 = font5.render('RESUME THE GAME', 1, (255,255,255))
    if index == 1:
        text2 = font5.render('CONTROLS', 1, (85,206,255))
    else: 
        text2 = font5.render('CONTROLS', 1, (255, 255, 255))
    if index == 2:
        text3 = font5.render('EXIT TO MAIN MENU', 1, (85,206,255))
    else:
        text3 = font5.render('EXIT TO MAIN MENU', 1, (255,255,255))
    win.blit(text1, (600, 400))   #OCEAN 85, 206, 255
    win.blit(text2, (760, 500))
    win.blit(text3, (575, 600))
    pygame.display.update()
    pass

#DIFFICULTY UPDATE
def update_difficulty(score, level):
    health_increase = score // 150

    return health_increase

#LEVEL CREATOR
def create_inf_levels(score, level):
    enemy_count = min(2 + round(level/5), 5)
    health_increase = update_difficulty(score, level)
    enemies = []
    if level % boss_level == 0:
        x = 860
        y = 300
        boss_enemy = boss(x, y, 64, 64, 200 + round(level/8) * 100)
        enemies.append(boss_enemy)
    else:
        for i in range(enemy_count):
            for j in range(enemy_count):
                x = random.randint(150, 1830)
                y = random.randint(100, 400)
                health = 10 + health_increase
                new_enemy = enemy(x, y, 64, 64, health)
                enemies.append(new_enemy)
    return enemies

#LEVEL TRANSITION
def level_transition():
    win.blit(bg, (0,0))
    if level % boss_level == 0:
        text = font2.render('BOSS DEFEATED!', True, (255, 255, 255))
        win.blit(text, (200,500))
    else:
        text = font2.render('NEXT LEVEL!', True, (255,255,255))
        win.blit(text, (350, 500))
    pygame.display.update()
    pygame.time.wait(2000)

# GAME LOOP
run = True
while run:
    clock.tick(fps)

    if game_state == in_menu:
        main_menu()
        #EVENT HANDLER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    index = (index + 1) % 3
                if event.key == pygame.K_UP:
                    index = (index - 1) % 3
                if event.key == pygame.K_RETURN:
                    if index == 0:
                        game_state = in_game
                        reset_game()
                    if index == 1:
                        game_state = in_controls
                        previous_game_state = in_menu
                    if index == 2:
                        run = False

    elif game_state == in_controls:
        controls()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state = previous_game_state

    elif game_state == in_pause:
        pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    index = (index + 1) % 3
                if event.key == pygame.K_UP:
                    index = (index - 1) % 3
                if event.key == pygame.K_RETURN:
                    if index == 0:
                        game_state = in_game
                    if index == 1:
                        game_state = in_controls
                        previous_game_state = in_pause
                    if index == 2:
                        game_state = in_menu
    
    elif game_state == in_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:   
                if event.key == pygame.K_ESCAPE:
                    game_state = in_pause

        # OPÓŹNIENIE W STRZELANIU GRACZA        #DODAC ZMIENNE OD ATTACK SPEEDU
        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 25 and score <= 200:
            shootLoop = 0
        if shootLoop > 15 and score > 200 and score <= 3000:
            shootLoop = 0
        if shootLoop > 7 and score > 3000:
            shootLoop = 0

        # FUNKCJA OBSŁUGUJĄCA TRAFIENIE W PRZECIWNIKA
        for bullet in bullets:
            bullet_hit = False

            for foe in enemies[:]:
                if foe.is_alive:
                    if bullet.y < foe.hitbox[1] + foe.hitbox[3] and bullet.y > foe.hitbox[1]:
                        if bullet.x < foe.hitbox[0] + foe.hitbox[2] and bullet.x > foe.hitbox[0]:
                            foe.hit()
                            if foe.is_alive == False:
                                score += 20
                            bullet_hit = True
                            break

                        elif bullet.x + bullet.hitbox[2] < foe.hitbox[0] + foe.hitbox[2] and bullet.x + bullet.hitbox[2] > foe.hitbox[0]:
                            foe.hit()
                            if foe.is_alive == False:
                                score += 20
                            bullet_hit = True
                            break

            if bullet_hit:
                bullets_to_remove.append(bullet)

            if bullet.y < screenHeight and bullet.y > 0:
                bullet.y -= bullet.vel
            else: 
                bullets.pop(bullets.index(bullet))

        for bullet in bullets_to_remove:
            if bullet in bullets:
                bullets.pop(bullets.index(bullet))

        all_enemies_dead = True
        for foe in enemies:
            if foe.is_alive or not foe.death_animation_finished():
                all_enemies_dead = False
                break

        # LEVEL TRANSITION
        if all_enemies_dead:
            if level == 0:
                level += 1
                ship.x = 860
                ship.y = 860
                enemies = create_inf_levels(score, level)
            else: 
                level_transition()
                level += 1
                ship.x = 860
                ship.y = 860
                enemies = create_inf_levels(score, level)

        # OBSŁUGA STRZAŁÓW PRZEZ PRZECIWNIKÓW
        for foe in enemies:
            if foe.is_alive:
                foe.try_to_shoot()

        for bullet in enemy_bullets:
            bullet_hit = False

            for foe in enemies:
                if bullet.y + bullet.hitbox[3] < ship.hitbox[1] + ship.hitbox[3] and bullet.y + bullet.hitbox[3] > ship.hitbox[1]:
                    if bullet.x < ship.hitbox[0] + ship.hitbox[2] and bullet.x > ship.hitbox[0]:
                        ship.hit()
                        bullet_hit = True
                        break
                    elif bullet.x + bullet.hitbox[2] < ship.hitbox[0] + ship.hitbox[2] and bullet.x + bullet.hitbox[2] > ship.hitbox[0]:
                        ship.hit()
                        bullet_hit = True
                        break

            if bullet_hit:
                enemy_bullets_to_remove.append(bullet)

            if bullet.y < screenHeight and bullet.y > 0:
                bullet.y += bullet.vel
            else:
                enemy_bullets.pop(enemy_bullets.index(bullet))

        for bullet in enemy_bullets_to_remove:
            if bullet in enemy_bullets:
                enemy_bullets.pop(enemy_bullets.index(bullet))

        # OBSŁUGA PRZYCISKÓW
        keys = pygame.key.get_pressed()

        if ship.is_alive:
            if keys[pygame.K_SPACE] and shootLoop == 0:
                if score <= 500:
                    bullets.append(Projectile(ship.x + 80, ship.y + ship.height//2)) #srodek
                
                elif score > 500 and score <= 2000:
                    bullets.append(Projectile(ship.x + 40, ship.y + ship.height//2)) #lewo
                    bullets.append(Projectile(ship.x + 120, ship.y + ship.height//2)) #prawo
                
                elif score > 2000 and score <= 5000:
                    bullets.append(Projectile(ship.x + 40, ship.y + ship.height//2)) #lewo
                    bullets.append(Projectile(ship.x + 80, ship.y + ship.height//2)) #srodek
                    bullets.append(Projectile(ship.x + 120, ship.y + ship.height//2)) #prawo
                
                elif score > 5000:
                    bullets.append(Projectile(ship.x + 40, ship.y + ship.height//2)) #lewo
                    bullets.append(Projectile(ship.x + 70, ship.y + ship.height//2)) #lewo-srodek
                    bullets.append(Projectile(ship.x + 95, ship.y + ship.height//2)) #prawo-srodek
                    bullets.append(Projectile(ship.x + 120, ship.y + ship.height//2)) #prawo
                shootLoop = 1
            
            ship.left = ship.right = ship.up = ship.down = False

            if keys[pygame.K_LEFT] and ship.x > ship.vel:
                ship.x -= ship.vel
                ship.left = True
                ship.right = False
            
            if keys[pygame.K_RIGHT] and ship.x < screenWidth - ship.width - ship.vel - 100:
                ship.x += ship.vel
                ship.left = False
                ship.right = True
            
            if keys[pygame.K_UP] and ship.y > ship.vel and ship.y > 600:
                ship.y -= ship.vel
                ship.up = True
                ship.down = False
            
            if keys[pygame.K_DOWN] and ship.y < screenHeight - ship.height - ship.vel - 100:
                ship.y += ship.vel
                ship.up = False
                ship.down = True

        bullets_to_remove = []
        redraw_game_window()

pygame.quit()