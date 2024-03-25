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

boss_level = 5
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


#PLAYER IMAGES
ship_image = pygame.image.load('Player/Nairan - Fighter - Base.png')

projectile_image = [pygame.image.load('Player/Nairan - Rocket0.png'), pygame.image.load('Player/Nairan - Rocket1.png'), pygame.image.load('Player/Nairan - Rocket2.png'), pygame.image.load('Player/Nairan - Rocket3.png')]

ship_death_image = [pygame.image.load('Player/Nairan - Fighter - Destruction0.png'), pygame.image.load('Player/Nairan - Fighter - Destruction1.png'), pygame.image.load('Player/Nairan - Fighter - Destruction2.png'), pygame.image.load('Player/Nairan - Fighter - Destruction3.png'), 
                    pygame.image.load('Player/Nairan - Fighter - Destruction4.png'), pygame.image.load('Player/Nairan - Fighter - Destruction5.png'), pygame.image.load('Player/Nairan - Fighter - Destruction6.png'), pygame.image.load('Player/Nairan - Fighter - Destruction7.png'), 
                    pygame.image.load('Player/Nairan - Fighter - Destruction8.png'), pygame.image.load('Player/Nairan - Fighter - Destruction9.png'), pygame.image.load('Player/Nairan - Fighter - Destruction10.png'), pygame.image.load('Player/Nairan - Fighter - Destruction11.png'), 
                    pygame.image.load('Player/Nairan - Fighter - Destruction12.png'), pygame.image.load('Player/Nairan - Fighter - Destruction13.png'), pygame.image.load('Player/Nairan - Fighter - Destruction14.png'), pygame.image.load('Player/Nairan - Fighter - Destruction15.png')]

ship_engine_image = [pygame.image.load('Player/Nairan - Fighter - Engine0.png'), pygame.image.load('Player/Nairan - Fighter - Engine1.png'), pygame.image.load('Player/Nairan - Fighter - Engine2.png'), pygame.image.load('Player/Nairan - Fighter - Engine3.png'),
                     pygame.image.load('Player/Nairan - Fighter - Engine4.png'), pygame.image.load('Player/Nairan - Fighter - Engine5.png'), pygame.image.load('Player/Nairan - Fighter - Engine6.png'), pygame.image.load('Player/Nairan - Fighter - Engine7.png')]

ship_engine = [pygame.transform.scale(ship_engine_image[0], (192, 192)), pygame.transform.scale(ship_engine_image[1], (192, 192)), pygame.transform.scale(ship_engine_image[2], (192, 192)), pygame.transform.scale(ship_engine_image[3], (192, 192)), 
               pygame.transform.scale(ship_engine_image[4], (192, 192)), pygame.transform.scale(ship_engine_image[5], (192, 192)), pygame.transform.scale(ship_engine_image[6], (192, 192)), pygame.transform.scale(ship_engine_image[7], (192, 192))]

ship_death = [pygame.transform.scale(ship_death_image[0], (192, 192)), pygame.transform.scale(ship_death_image[1], (192, 192)), pygame.transform.scale(ship_death_image[2], (192, 192)), pygame.transform.scale(ship_death_image[3], (192, 192)), 
                    pygame.transform.scale(ship_death_image[4], (192, 192)), pygame.transform.scale(ship_death_image[5], (192, 192)), pygame.transform.scale(ship_death_image[6], (192, 192)), pygame.transform.scale(ship_death_image[7], (192, 192)), 
                    pygame.transform.scale(ship_death_image[8], (192, 192)), pygame.transform.scale(ship_death_image[9], (192, 192)), pygame.transform.scale(ship_death_image[10], (192, 192)), pygame.transform.scale(ship_death_image[11], (192, 192)), 
                    pygame.transform.scale(ship_death_image[12], (192, 192)), pygame.transform.scale(ship_death_image[13], (192, 192)), pygame.transform.scale(ship_death_image[14], (192, 192)), pygame.transform.scale(ship_death_image[15], (192, 192))]

attack = [pygame.transform.scale(projectile_image[0], (32, 32)), pygame.transform.scale(projectile_image[1], (32, 32)), pygame.transform.scale(projectile_image[2], (32, 32)), pygame.transform.scale(projectile_image[3], (32, 32))]

#ENEMY IMAGES
enemy_ship_image = pygame.image.load('Enemy/Nautolan Ship - Fighter - Base.png')

enemy_projectile_image = [pygame.image.load('Enemy/Nautolan - Bullet0.png'), pygame.image.load('Enemy/Nautolan - Bullet1.png'), pygame.image.load('Enemy/Nautolan - Bullet2.png'), 
                          pygame.image.load('Enemy/Nautolan - Bullet3.png'), pygame.image.load('Enemy/Nautolan - Bullet4.png'), pygame.image.load('Enemy/Nautolan - Bullet5.png'), 
                          pygame.image.load('Enemy/Nautolan - Bullet6.png'), pygame.image.load('Enemy/Nautolan - Bullet7.png')]

enemy_engine_image = [pygame.image.load('Enemy/Nautolan Ship - Fighter - Engine Effect0.png'), pygame.image.load('Enemy/Nautolan Ship - Fighter - Engine Effect1.png'), pygame.image.load('Enemy/Nautolan Ship - Fighter - Engine Effect2.png'), 
                      pygame.image.load('Enemy/Nautolan Ship - Fighter - Engine Effect3.png'), pygame.image.load('Enemy/Nautolan Ship - Fighter - Engine Effect4.png'), pygame.image.load('Enemy/Nautolan Ship - Fighter - Engine Effect5.png'), 
                      pygame.image.load('Enemy/Nautolan Ship - Fighter - Engine Effect6.png'), pygame.image.load('Enemy/Nautolan Ship - Fighter - Engine Effect7.png')]

enemy_engine = [pygame.transform.scale(enemy_engine_image[0], (128, 128)), pygame.transform.scale(enemy_engine_image[1], (128, 128)), pygame.transform.scale(enemy_engine_image[2], (128, 128)), pygame.transform.scale(enemy_engine_image[3], (128, 128)), 
                pygame.transform.scale(enemy_engine_image[4], (128, 128)), pygame.transform.scale(enemy_engine_image[5], (128, 128)), pygame.transform.scale(enemy_engine_image[6], (128, 128)), pygame.transform.scale(enemy_engine_image[7], (128, 128))]

enemy_death_image = [pygame.image.load('Enemy/Nautolan Ship - Fighter - Destruction0.png'), pygame.image.load('Enemy/Nautolan Ship - Fighter - Destruction1.png'), pygame.image.load('Enemy/Nautolan Ship - Fighter - Destruction2.png'), 
                     pygame.image.load('Enemy/Nautolan Ship - Fighter - Destruction3.png'), pygame.image.load('Enemy/Nautolan Ship - Fighter - Destruction4.png'), pygame.image.load('Enemy/Nautolan Ship - Fighter - Destruction5.png'), 
                     pygame.image.load('Enemy/Nautolan Ship - Fighter - Destruction6.png'), pygame.image.load('Enemy/Nautolan Ship - Fighter - Destruction7.png')]

enemy_death = [pygame.transform.scale(enemy_death_image[0], (128, 128)), pygame.transform.scale(enemy_death_image[1], (128, 128)), pygame.transform.scale(enemy_death_image[2], (128, 128)), pygame.transform.scale(enemy_death_image[3], (128, 128)), 
               pygame.transform.scale(enemy_death_image[4], (128, 128)), pygame.transform.scale(enemy_death_image[5], (128, 128)), pygame.transform.scale(enemy_death_image[6], (128, 128)), pygame.transform.scale(enemy_death_image[7], (128, 128))]

enemy_attack = [pygame.transform.scale(enemy_projectile_image[0], (32, 32)), pygame.transform.scale(enemy_projectile_image[1], (32, 32)), pygame.transform.scale(enemy_projectile_image[2], (32, 32)), pygame.transform.scale(enemy_projectile_image[3], (32, 32)), 
                pygame.transform.scale(enemy_projectile_image[4], (32, 32)), pygame.transform.scale(enemy_projectile_image[5], (32, 32)), pygame.transform.scale(enemy_projectile_image[6], (32, 32)), pygame.transform.scale(enemy_projectile_image[7], (32, 32))]

#ENEMY1
enemy1_ship_image = pygame.image.load('Enemy/Nautolan Ship - Bomber - Base.png')

enemy1_projectile_image = [pygame.image.load('Enemy/Nautolan - Bomb0.png'), pygame.image.load('Enemy/Nautolan - Bomb1.png'), pygame.image.load('Enemy/Nautolan - Bomb2.png'), pygame.image.load('Enemy/Nautolan - Bomb3.png'), pygame.image.load('Enemy/Nautolan - Bomb4.png'), 
                           pygame.image.load('Enemy/Nautolan - Bomb5.png'), pygame.image.load('Enemy/Nautolan - Bomb6.png'), pygame.image.load('Enemy/Nautolan - Bomb7.png'), pygame.image.load('Enemy/Nautolan - Bomb8.png'), pygame.image.load('Enemy/Nautolan - Bomb9.png'), 
                           pygame.image.load('Enemy/Nautolan - Bomb10.png'), pygame.image.load('Enemy/Nautolan - Bomb11.png'), pygame.image.load('Enemy/Nautolan - Bomb12.png'), pygame.image.load('Enemy/Nautolan - Bomb13.png'), pygame.image.load('Enemy/Nautolan - Bomb14.png'),
                           pygame.image.load('Enemy/Nautolan - Bomb15.png')]

enemy1_engine_image = [pygame.image.load('Enemy/Nautolan Ship - Bomber - Engine Effect0.png'), pygame.image.load('Enemy/Nautolan Ship - Bomber - Engine Effect1.png'), pygame.image.load('Enemy/Nautolan Ship - Bomber - Engine Effect2.png'), 
                      pygame.image.load('Enemy/Nautolan Ship - Bomber - Engine Effect3.png'), pygame.image.load('Enemy/Nautolan Ship - Bomber - Engine Effect4.png'), pygame.image.load('Enemy/Nautolan Ship - Bomber - Engine Effect5.png'), 
                      pygame.image.load('Enemy/Nautolan Ship - Bomber - Engine Effect6.png'), pygame.image.load('Enemy/Nautolan Ship - Bomber - Engine Effect7.png')]

enemy1_engine = [pygame.transform.scale(enemy1_engine_image[0], (128, 128)), pygame.transform.scale(enemy1_engine_image[1], (128, 128)), pygame.transform.scale(enemy1_engine_image[2], (128, 128)), pygame.transform.scale(enemy1_engine_image[3], (128, 128)), 
                 pygame.transform.scale(enemy1_engine_image[4], (128, 128)), pygame.transform.scale(enemy1_engine_image[5], (128, 128)), pygame.transform.scale(enemy1_engine_image[6], (128, 128)), pygame.transform.scale(enemy1_engine_image[7], (128, 128))]

enemy1_death_image = [pygame.image.load('Enemy/Nautolan Ship - Bomber0.png'), pygame.image.load('Enemy/Nautolan Ship - Bomber1.png'), pygame.image.load('Enemy/Nautolan Ship - Bomber3.png'), 
                      pygame.image.load('Enemy/Nautolan Ship - Bomber3.png'), pygame.image.load('Enemy/Nautolan Ship - Bomber4.png'), pygame.image.load('Enemy/Nautolan Ship - Bomber5.png'), 
                      pygame.image.load('Enemy/Nautolan Ship - Bomber6.png'), pygame.image.load('Enemy/Nautolan Ship - Bomber7.png'), pygame.image.load('Enemy/Nautolan Ship - Bomber8.png'),
                      pygame.image.load('Enemy/Nautolan Ship - Bomber9.png')]

enemy1_death = [pygame.transform.scale(enemy1_death_image[0], (128, 128)), pygame.transform.scale(enemy1_death_image[1], (128, 128)), pygame.transform.scale(enemy1_death_image[2], (128, 128)), pygame.transform.scale(enemy1_death_image[3], (128, 128)), 
                pygame.transform.scale(enemy1_death_image[4], (128, 128)), pygame.transform.scale(enemy1_death_image[5], (128, 128)), pygame.transform.scale(enemy1_death_image[6], (128, 128)), pygame.transform.scale(enemy1_death_image[7], (128, 128)), 
                pygame.transform.scale(enemy1_death_image[8], (128, 128)), pygame.transform.scale(enemy1_death_image[9], (128, 128))]

enemy1_attack = [pygame.transform.scale(enemy1_projectile_image[0], (32, 32)), pygame.transform.scale(enemy1_projectile_image[1], (32, 32)), pygame.transform.scale(enemy1_projectile_image[2], (32, 32)), pygame.transform.scale(enemy1_projectile_image[3], (32, 32)), 
                 pygame.transform.scale(enemy1_projectile_image[4], (32, 32)), pygame.transform.scale(enemy1_projectile_image[5], (32, 32)), pygame.transform.scale(enemy1_projectile_image[6], (32, 32)), pygame.transform.scale(enemy1_projectile_image[7], (32, 32)),
                 pygame.transform.scale(enemy1_projectile_image[8], (32, 32)), pygame.transform.scale(enemy1_projectile_image[9], (32, 32)), pygame.transform.scale(enemy1_projectile_image[10], (32, 32)), pygame.transform.scale(enemy1_projectile_image[11], (32, 32)),
                 pygame.transform.scale(enemy1_projectile_image[12], (32, 32)), pygame.transform.scale(enemy1_projectile_image[13], (32, 32)), pygame.transform.scale(enemy1_projectile_image[14], (32, 32)), pygame.transform.scale(enemy1_projectile_image[15], (32, 32))]

#ENEMY2
enemy2_ship_image = pygame.image.load('Enemy/Nautolan Ship - Scout - Base.png')

enemy2_projectile_image = [pygame.image.load('Enemy/Nautolan - Spinning Bullet0.png'), pygame.image.load('Enemy/Nautolan - Spinning Bullet1.png'), pygame.image.load('Enemy/Nautolan - Spinning Bullet2.png'), pygame.image.load('Enemy/Nautolan - Spinning Bullet3.png'),
                           pygame.image.load('Enemy/Nautolan - Spinning Bullet4.png'), pygame.image.load('Enemy/Nautolan - Spinning Bullet5.png'), pygame.image.load('Enemy/Nautolan - Spinning Bullet6.png'), pygame.image.load('Enemy/Nautolan - Spinning Bullet7.png')]

enemy2_engine_image = [pygame.image.load('Enemy/Nautolan Ship - Scout - Engine Effect0.png'), pygame.image.load('Enemy/Nautolan Ship - Scout - Engine Effect1.png'), pygame.image.load('Enemy/Nautolan Ship - Scout - Engine Effect2.png'), 
                       pygame.image.load('Enemy/Nautolan Ship - Scout - Engine Effect3.png'), pygame.image.load('Enemy/Nautolan Ship - Scout - Engine Effect4.png'), pygame.image.load('Enemy/Nautolan Ship - Scout - Engine Effect5.png'), 
                       pygame.image.load('Enemy/Nautolan Ship - Scout - Engine Effect6.png'), pygame.image.load('Enemy/Nautolan Ship - Scout - Engine Effect7.png')]

enemy2_engine = [pygame.transform.scale(enemy2_engine_image[0], (128, 128)), pygame.transform.scale(enemy2_engine_image[1], (128, 128)), pygame.transform.scale(enemy2_engine_image[2], (128, 128)), pygame.transform.scale(enemy2_engine_image[3], (128, 128)), 
                 pygame.transform.scale(enemy2_engine_image[4], (128, 128)), pygame.transform.scale(enemy2_engine_image[5], (128, 128)), pygame.transform.scale(enemy2_engine_image[6], (128, 128)), pygame.transform.scale(enemy2_engine_image[7], (128, 128))]

enemy2_death_image = [pygame.image.load('Enemy/Nautolan Ship - Scout0.png'), pygame.image.load('Enemy/Nautolan Ship - Scout1.png'), pygame.image.load('Enemy/Nautolan Ship - Scout3.png'), 
                      pygame.image.load('Enemy/Nautolan Ship - Scout3.png'), pygame.image.load('Enemy/Nautolan Ship - Scout4.png'), pygame.image.load('Enemy/Nautolan Ship - Scout5.png'), 
                      pygame.image.load('Enemy/Nautolan Ship - Scout6.png'), pygame.image.load('Enemy/Nautolan Ship - Scout7.png'), pygame.image.load('Enemy/Nautolan Ship - Scout8.png')]

enemy2_death = [pygame.transform.scale(enemy2_death_image[0], (128, 128)), pygame.transform.scale(enemy2_death_image[1], (128, 128)), pygame.transform.scale(enemy2_death_image[2], (128, 128)), 
                pygame.transform.scale(enemy2_death_image[3], (128, 128)), pygame.transform.scale(enemy2_death_image[4], (128, 128)), pygame.transform.scale(enemy2_death_image[5], (128, 128)), 
                pygame.transform.scale(enemy2_death_image[6], (128, 128)), pygame.transform.scale(enemy2_death_image[7], (128, 128)), pygame.transform.scale(enemy2_death_image[8], (128, 128))]

enemy2_attack = [pygame.transform.scale(enemy2_projectile_image[0], (16, 16)), pygame.transform.scale(enemy2_projectile_image[1], (16, 16)), pygame.transform.scale(enemy2_projectile_image[2], (16, 16)), pygame.transform.scale(enemy2_projectile_image[3], (16, 16)), 
                 pygame.transform.scale(enemy2_projectile_image[4], (16, 16)), pygame.transform.scale(enemy2_projectile_image[5], (16, 16)), pygame.transform.scale(enemy2_projectile_image[6], (16, 16)), pygame.transform.scale(enemy2_projectile_image[7], (16, 16))]

#BOSS IMAGES
boss_image = pygame.image.load('Boss/Nautolan Ship - Dreadnought - Base.png')

boss_engine_image = [pygame.image.load('Boss/Nautolan Ship - Dreadnought - Engine Effect0.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought - Engine Effect1.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought - Engine Effect2.png'), 
                     pygame.image.load('Boss/Nautolan Ship - Dreadnought - Engine Effect3.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought - Engine Effect4.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought - Engine Effect5.png'), 
                     pygame.image.load('Boss/Nautolan Ship - Dreadnought - Engine Effect6.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought - Engine Effect7.png'), ]

boss_engine = [pygame.transform.scale(boss_engine_image[0], (384, 384)), pygame.transform.scale(boss_engine_image[1], (384, 384)), pygame.transform.scale(boss_engine_image[2], (384, 384)), pygame.transform.scale(boss_engine_image[3], (384, 384)), 
               pygame.transform.scale(boss_engine_image[4], (384, 384)), pygame.transform.scale(boss_engine_image[5], (384, 384)), pygame.transform.scale(boss_engine_image[6], (384, 384)), pygame.transform.scale(boss_engine_image[7], (384, 384)), ]

boss_death_image = [pygame.image.load('Boss/Nautolan Ship - Dreadnought0.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought1.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought2.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought3.png'), 
                    pygame.image.load('Boss/Nautolan Ship - Dreadnought4.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought5.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought6.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought7.png'), 
                    pygame.image.load('Boss/Nautolan Ship - Dreadnought8.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought9.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought10.png'), pygame.image.load('Boss/Nautolan Ship - Dreadnought11.png')]

boss_death = [pygame.transform.scale(boss_death_image[0], (384, 384)), pygame.transform.scale(boss_death_image[1], (384, 384)), pygame.transform.scale(boss_death_image[2], (384, 384)), pygame.transform.scale(boss_death_image[3], (384, 384)), 
              pygame.transform.scale(boss_death_image[4], (384, 384)), pygame.transform.scale(boss_death_image[5], (384, 384)), pygame.transform.scale(boss_death_image[6], (384, 384)), pygame.transform.scale(boss_death_image[7], (384, 384)), 
              pygame.transform.scale(boss_death_image[8], (384, 384)), pygame.transform.scale(boss_death_image[9], (384, 384)), pygame.transform.scale(boss_death_image[10], (384, 384)), pygame.transform.scale(boss_death_image[11], (384, 384))]

boss_projectile_image = [pygame.image.load('Boss/Nautolan - Ray0.png'), pygame.image.load('Boss/Nautolan - Ray1.png'), pygame.image.load('Boss/Nautolan - Ray2.png'), pygame.image.load('Boss/Nautolan - Ray3.png')]
boss_attack = [pygame.transform.scale(boss_projectile_image[0], (64, 64)), pygame.transform.scale(boss_projectile_image[1], (64, 64)), pygame.transform.scale(boss_projectile_image[2], (64, 64)), pygame.transform.scale(boss_projectile_image[3], (64, 64))]

#BOSS1
boss1_image = pygame.image.load('Boss/Nautolan Ship - Battlecruiser - Base.png')

boss1_engine_image = [pygame.image.load('Boss/Nautolan Ship - Battlecruiser - Engine Effect0.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser - Engine Effect1.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser - Engine Effect2.png'), 
                     pygame.image.load('Boss/Nautolan Ship - Battlecruiser - Engine Effect3.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser - Engine Effect4.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser - Engine Effect5.png'), 
                     pygame.image.load('Boss/Nautolan Ship - Battlecruiser - Engine Effect6.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser - Engine Effect7.png'), ]

boss1_engine = [pygame.transform.scale(boss1_engine_image[0], (384, 384)), pygame.transform.scale(boss1_engine_image[1], (384, 384)), pygame.transform.scale(boss1_engine_image[2], (384, 384)), pygame.transform.scale(boss1_engine_image[3], (384, 384)), 
               pygame.transform.scale(boss1_engine_image[4], (384, 384)), pygame.transform.scale(boss1_engine_image[5], (384, 384)), pygame.transform.scale(boss1_engine_image[6], (384, 384)), pygame.transform.scale(boss1_engine_image[7], (384, 384)), ]

boss1_death_image = [pygame.image.load('Boss/Nautolan Ship - Battlecruiser0.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser1.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser2.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser3.png'), 
                    pygame.image.load('Boss/Nautolan Ship - Battlecruiser4.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser5.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser6.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser7.png'), 
                    pygame.image.load('Boss/Nautolan Ship - Battlecruiser8.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser9.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser10.png'), pygame.image.load('Boss/Nautolan Ship - Battlecruiser11.png'),
                    pygame.image.load('Boss/Nautolan Ship - Battlecruiser12.png')]

boss1_death = [pygame.transform.scale(boss1_death_image[0], (384, 384)), pygame.transform.scale(boss1_death_image[1], (384, 384)), pygame.transform.scale(boss1_death_image[2], (384, 384)), pygame.transform.scale(boss1_death_image[3], (384, 384)), 
              pygame.transform.scale(boss1_death_image[4], (384, 384)), pygame.transform.scale(boss1_death_image[5], (384, 384)), pygame.transform.scale(boss1_death_image[6], (384, 384)), pygame.transform.scale(boss1_death_image[7], (384, 384)), 
              pygame.transform.scale(boss1_death_image[8], (384, 384)), pygame.transform.scale(boss1_death_image[9], (384, 384)), pygame.transform.scale(boss1_death_image[10], (384, 384)), pygame.transform.scale(boss1_death_image[11], (384, 384)),
              pygame.transform.scale(boss1_death_image[12], (384, 384))]

boss1_projectile_image = [pygame.image.load('Boss/Nautolan - Wave0.png'), pygame.image.load('Boss/Nautolan - Wave1.png'), pygame.image.load('Boss/Nautolan - Wave2.png'), 
                          pygame.image.load('Boss/Nautolan - Wave3.png'), pygame.image.load('Boss/Nautolan - Wave4.png'), pygame.image.load('Boss/Nautolan - Wave5.png')]

boss1_attack = [pygame.transform.scale(boss1_projectile_image[0], (192, 192)), pygame.transform.scale(boss1_projectile_image[1], (192, 192)), pygame.transform.scale(boss1_projectile_image[2], (192, 192)), 
                pygame.transform.scale(boss1_projectile_image[3], (192, 192)), pygame.transform.scale(boss1_projectile_image[4], (192, 192)), pygame.transform.scale(boss1_projectile_image[5], (192, 192))]


health_image = [pygame.image.load('Red Heart.png'), pygame.image.load('Red Damaged Heart.png'), pygame.image.load('Red Empty Heart.png')]
health = [pygame.transform.scale(health_image[0], (48, 48)), pygame.transform.scale(health_image[1], (48, 48)), pygame.transform.scale(health_image[2], (48, 48))]
fly = pygame.transform.scale(ship_image, (192, 192))
bg = pygame.image.load('background.png')

clock = pygame.time.Clock()