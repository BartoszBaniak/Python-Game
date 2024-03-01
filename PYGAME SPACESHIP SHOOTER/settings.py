import pygame

screenWidth = 1920
screenHeight = 1080

game_start_time = None
game_pause_time = None
start_delay = 3

pygame.font.init()
font = pygame.font.Font('04B_30__.ttf', 32)
font2 = pygame.font.Font('04B_30__.ttf', 128)
font3 = pygame.font.Font('04B_30__.ttf', 64)
font4 = pygame.font.Font('04B_30__.ttf', 110)
font5 = pygame.font.Font('04B_30__.ttf', 48)

boss_level = 4
level = 0
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



ship_death_image = [pygame.image.load('Nairan - Fighter - Destruction0.png'), pygame.image.load('Nairan - Fighter - Destruction1.png'), pygame.image.load('Nairan - Fighter - Destruction2.png'), pygame.image.load('Nairan - Fighter - Destruction3.png'), 
                    pygame.image.load('Nairan - Fighter - Destruction4.png'), pygame.image.load('Nairan - Fighter - Destruction5.png'), pygame.image.load('Nairan - Fighter - Destruction6.png'), pygame.image.load('Nairan - Fighter - Destruction7.png'), 
                    pygame.image.load('Nairan - Fighter - Destruction8.png'), pygame.image.load('Nairan - Fighter - Destruction9.png'), pygame.image.load('Nairan - Fighter - Destruction10.png'), pygame.image.load('Nairan - Fighter - Destruction11.png'), 
                    pygame.image.load('Nairan - Fighter - Destruction12.png'), pygame.image.load('Nairan - Fighter - Destruction13.png'), pygame.image.load('Nairan - Fighter - Destruction14.png'), pygame.image.load('Nairan - Fighter - Destruction15.png')]

ship_engine_image = [pygame.image.load('Nairan - Fighter - Engine0.png'), pygame.image.load('Nairan - Fighter - Engine1.png'), pygame.image.load('Nairan - Fighter - Engine2.png'), pygame.image.load('Nairan - Fighter - Engine3.png'),
                     pygame.image.load('Nairan - Fighter - Engine4.png'), pygame.image.load('Nairan - Fighter - Engine5.png'), pygame.image.load('Nairan - Fighter - Engine6.png'), pygame.image.load('Nairan - Fighter - Engine7.png')]

ship_engine = [pygame.transform.scale(ship_engine_image[0], (192, 192)), pygame.transform.scale(ship_engine_image[1], (192, 192)), pygame.transform.scale(ship_engine_image[2], (192, 192)), pygame.transform.scale(ship_engine_image[3], (192, 192)), 
               pygame.transform.scale(ship_engine_image[4], (192, 192)), pygame.transform.scale(ship_engine_image[5], (192, 192)), pygame.transform.scale(ship_engine_image[6], (192, 192)), pygame.transform.scale(ship_engine_image[7], (192, 192))]

ship_death = [pygame.transform.scale(ship_death_image[0], (192, 192)), pygame.transform.scale(ship_death_image[1], (192, 192)), pygame.transform.scale(ship_death_image[2], (192, 192)), pygame.transform.scale(ship_death_image[3], (192, 192)), 
                    pygame.transform.scale(ship_death_image[4], (192, 192)), pygame.transform.scale(ship_death_image[5], (192, 192)), pygame.transform.scale(ship_death_image[6], (192, 192)), pygame.transform.scale(ship_death_image[7], (192, 192)), 
                    pygame.transform.scale(ship_death_image[8], (192, 192)), pygame.transform.scale(ship_death_image[9], (192, 192)), pygame.transform.scale(ship_death_image[10], (192, 192)), pygame.transform.scale(ship_death_image[11], (192, 192)), 
                    pygame.transform.scale(ship_death_image[12], (192, 192)), pygame.transform.scale(ship_death_image[13], (192, 192)), pygame.transform.scale(ship_death_image[14], (192, 192)), pygame.transform.scale(ship_death_image[15], (192, 192))]

enemy_death_image = [pygame.image.load('Nautolan Ship - Fighter - Destruction0.png'), pygame.image.load('Nautolan Ship - Fighter - Destruction1.png'), pygame.image.load('Nautolan Ship - Fighter - Destruction2.png'), pygame.image.load('Nautolan Ship - Fighter - Destruction3.png'), 
                     pygame.image.load('Nautolan Ship - Fighter - Destruction4.png'), pygame.image.load('Nautolan Ship - Fighter - Destruction5.png'), pygame.image.load('Nautolan Ship - Fighter - Destruction6.png'), pygame.image.load('Nautolan Ship - Fighter - Destruction7.png')]

boss_death_image = [pygame.image.load('Nautolan Ship - Dreadnought0.png'), pygame.image.load('Nautolan Ship - Dreadnought1.png'), pygame.image.load('Nautolan Ship - Dreadnought2.png'), pygame.image.load('Nautolan Ship - Dreadnought3.png'), pygame.image.load('Nautolan Ship - Dreadnought4.png'), 
                    pygame.image.load('Nautolan Ship - Dreadnought5.png'), pygame.image.load('Nautolan Ship - Dreadnought6.png'), pygame.image.load('Nautolan Ship - Dreadnought7.png'), pygame.image.load('Nautolan Ship - Dreadnought8.png'), pygame.image.load('Nautolan Ship - Dreadnought9.png'), 
                    pygame.image.load('Nautolan Ship - Dreadnought10.png'), pygame.image.load('Nautolan Ship - Dreadnought11.png')]

enemy_death = [pygame.transform.scale(enemy_death_image[0], (128, 128)), pygame.transform.scale(enemy_death_image[1], (128, 128)), pygame.transform.scale(enemy_death_image[2], (128, 128)), pygame.transform.scale(enemy_death_image[3], (128, 128)), 
                  pygame.transform.scale(enemy_death_image[4], (128, 128)), pygame.transform.scale(enemy_death_image[5], (128, 128)), pygame.transform.scale(enemy_death_image[6], (128, 128)), pygame.transform.scale(enemy_death_image[7], (128, 128))]

boss_death = [pygame.transform.scale(boss_death_image[0], (384, 384)), pygame.transform.scale(boss_death_image[1], (384, 384)), pygame.transform.scale(boss_death_image[2], (384, 384)), pygame.transform.scale(boss_death_image[3], (384, 384)), pygame.transform.scale(boss_death_image[4], (384, 384)), 
              pygame.transform.scale(boss_death_image[5], (384, 384)), pygame.transform.scale(boss_death_image[6], (384, 384)), pygame.transform.scale(boss_death_image[7], (384, 384)), pygame.transform.scale(boss_death_image[8], (384, 384)), pygame.transform.scale(boss_death_image[9], (384, 384)), 
              pygame.transform.scale(boss_death_image[10], (384, 384)), pygame.transform.scale(boss_death_image[11], (384, 384))]

health_image = [pygame.image.load('Red Heart.png'), pygame.image.load('Red Damaged Heart.png'), pygame.image.load('Red Empty Heart.png')]
ship_image = pygame.image.load('Nairan - Fighter - Base.png')
enemy_ship_image = pygame.image.load('Nautolan Ship - Fighter - Base.png')
boss_image = pygame.image.load('Nautolan Ship - Dreadnought - Base.png')

projectile_image = [pygame.image.load('Nairan - Rocket0.png'), pygame.image.load('Nairan - Rocket1.png'), pygame.image.load('Nairan - Rocket2.png'), pygame.image.load('Nairan - Rocket3.png')]
enemy_projectile_image = [pygame.image.load('Nautolan - Bullet0.png'), pygame.image.load('Nautolan - Bullet1.png'), pygame.image.load('Nautolan - Bullet2.png'), pygame.image.load('Nautolan - Bullet3.png'), pygame.image.load('Nautolan - Bullet4.png'), pygame.image.load('Nautolan - Bullet5.png'),
                          pygame.image.load('Nautolan - Bullet6.png'), pygame.image.load('Nautolan - Bullet7.png')]
boss_projectile_image = [pygame.image.load('Nautolan - Ray0.png'), pygame.image.load('Nautolan - Ray1.png'), pygame.image.load('Nautolan - Ray2.png'), pygame.image.load('Nautolan - Ray3.png')]

health = [pygame.transform.scale(health_image[0], (48, 48)), pygame.transform.scale(health_image[1], (48, 48)), pygame.transform.scale(health_image[2], (48, 48))]
fly = pygame.transform.scale(ship_image, (192, 192))
attack = [pygame.transform.scale(projectile_image[0], (32, 32)), pygame.transform.scale(projectile_image[1], (32, 32)), pygame.transform.scale(projectile_image[2], (32, 32)), pygame.transform.scale(projectile_image[3], (32, 32))]
enemy_attack = [pygame.transform.scale(enemy_projectile_image[0], (32, 32)), pygame.transform.scale(enemy_projectile_image[1], (32, 32)), pygame.transform.scale(enemy_projectile_image[2], (32, 32)), pygame.transform.scale(enemy_projectile_image[3], (32, 32)), 
                pygame.transform.scale(enemy_projectile_image[4], (32, 32)), pygame.transform.scale(enemy_projectile_image[5], (32, 32)), pygame.transform.scale(enemy_projectile_image[6], (32, 32)), pygame.transform.scale(enemy_projectile_image[7], (32, 32))]
boss_attack = [pygame.transform.scale(boss_projectile_image[0], (64, 64)), pygame.transform.scale(boss_projectile_image[1], (64, 64)), pygame.transform.scale(boss_projectile_image[2], (64, 64)), pygame.transform.scale(boss_projectile_image[3], (64, 64))]
bg = pygame.image.load('background.png')

clock = pygame.time.Clock()