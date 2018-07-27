# Karissa Bowser
# CPSC 386 FALL 2016
# Project 5 (Final Project)
# knb@csu.fullerton.edu
# Armada.py is a top-down space shooter game made using Python 3.4 and Pygame 1.9.


import sys, random, time, pygame
from   pygame.locals import *

# Colors
WHITE = (255, 255, 255)
BLACK = (0,   0,   0  )
RED   = (255, 0,   0  )
GREEN = (0,   255, 0  ) 

# Text color
TEXT_COLOR = WHITE

# Set up window size and FPS
GAME_WINDOW_WIDTH = 1400 
GAME_WINDOW_HEIGHT = 800 
FPS = 60

# Boss level
BOSS_LVL = random.randint(2,3)

# Alien Size, includes ALIEN1 and ALIEN2
ALIEN_SIZE = 70

# Alien Spawn Rate
# Increase this to make the spawn timer longer,
# Or decrease to make the aliens spawn quickly
ALIEN1_SPAWN_RATE = 60
ALIEN2_SPAWN_RATE = ALIEN1_SPAWN_RATE

# Keep track of the player, aliens, bullets, and reload speed
# Player Speed
PLAYER_SPEED = 15
# Alien Speed
ALIEN1_SPEED = 2
ALIEN2_SPEED = ALIEN1_SPEED / 2
BOSS_SPEED = ALIEN1_SPEED / 2
# Speed of the bullet, and reload speed
BULLET_SPEED = 10
ALIEN_BULLET_SPEED = 10
RELOAD_SPEED = 15

# Keep a list of all of the aliens and ammo
ALIEN1 = []
ALIEN2 = []
BULLETS = []
ALIEN_BULLETS = []

# Set up images for the game
# Player image
PLAYER_IMG  = pygame.image.load('player_ship.png')
PLAYER_RECT = PLAYER_IMG.get_rect()
# Alien images
ALIEN1_IMG = pygame.image.load('alien1.png')
ALIEN2_IMG = pygame.image.load('alien2.png')
BOSS_IMG   = pygame.image.load('boss.png')
BOSS_RECT  = BOSS_IMG.get_rect()
# Player ammo
BULLET_IMG = pygame.Surface([10, 2])
BULLET_IMG.fill(RED)
BULLET_RECT = BULLET_IMG.get_rect()
# Alien ammo
ALIEN_BULLET_IMG = pygame.Surface([10, 2])
ALIEN_BULLET_IMG.fill(GREEN)
ALIEN_BULLET_RECT = BULLET_IMG.get_rect()
# Explosion images
EXPLOSION_IMG     = pygame.image.load('explosion.png')
BIG_EXPLOSION_IMG = pygame.image.load('big_explosion.png')
# Title screen image
TITLE_IMG = pygame.image.load("title_screen.jpg")
#TITLE_IMG = pygame.transform.scale(TITLE_IMG, (GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
# Instructions screen image
INSTRUCTIONS_IMG = pygame.image.load('instructions_bg.jpg')
INSTRUCTIONS_IMG = pygame.transform.scale(INSTRUCTIONS_IMG, (GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
# In game background image
BACKGROUND_IMG = pygame.image.load('sky.jpg')
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))


# main() function
def main():
    global FPS_CLOCK, GAME_DISPLAY, SMALL_FONT, LRG_FONT, XTRA_LRG_FONT
    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    GAME_DISPLAY = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
    SMALL_FONT = pygame.font.SysFont('freesansbold.ttf', 30)
    LRG_FONT = pygame.font.SysFont('freesansbold.ttf', 60)
    XTRA_LRG_FONT = pygame.font.SysFont('freesansbold.ttf', 120)

    # There's no mouse input for this game, so don't show the pointer
    pygame.mouse.set_visible(False)

    # Play non in-game music
    pygame.mixer.music.load('death.mid')
    pygame.mixer.music.play(-1, 0.0)

    # Show the title screen
    GAME_DISPLAY.blit(TITLE_IMG, (0, 0))
    drawText('ARMADA', XTRA_LRG_FONT, GAME_DISPLAY, 0, 0 , TEXT_COLOR)
    drawText('Press Enter', LRG_FONT, GAME_DISPLAY, 600, 750, TEXT_COLOR)
    drawText('Game by K. Bowser', SMALL_FONT, GAME_DISPLAY, 1190, 780, TEXT_COLOR)
    pygame.display.update()
    getLoadingScreenInput()

    # Show the instructions screen
    GAME_DISPLAY.blit(INSTRUCTIONS_IMG, (0, 0))
    
    drawText('INSTRUCTIONS:', LRG_FONT, GAME_DISPLAY, 10 , 10, TEXT_COLOR) # Display at top left corner
    drawText('Defeat the mothership to win the game', SMALL_FONT, GAME_DISPLAY, 10 , 50, TEXT_COLOR)
    drawText('Don\'t let the mothership reach Earth. If you do, then it\'s Game Over', SMALL_FONT, GAME_DISPLAY, 10 , 70, TEXT_COLOR)
    drawText('Avoid all aliens, if an alien gets close enough to you, then it\'s Game Over', SMALL_FONT, GAME_DISPLAY, 10 , 90, TEXT_COLOR)
    drawText('If your HP falls to zero, then it\'s Game Over', SMALL_FONT, GAME_DISPLAY, 10 , 110, TEXT_COLOR)
    drawText('Each time an alien reaches Earth, the Earth\'s defense drops 5 percent', SMALL_FONT, GAME_DISPLAY, 10 , 130, TEXT_COLOR)
    drawText('If Earth\'s defense drops to 0 you lose the game (i.e., 20 aliens reaching Earth results in Game Over)', SMALL_FONT, GAME_DISPLAY, 10 , 150, TEXT_COLOR)
    
    drawText('CONTROLS:', LRG_FONT, GAME_DISPLAY, 10 , 210, TEXT_COLOR)
    drawText('To move: W,A,S,D or arrow keys', SMALL_FONT, GAME_DISPLAY, 10 , 250, TEXT_COLOR)
    drawText('To shoot: Spacebar', SMALL_FONT, GAME_DISPLAY, 10 , 270, TEXT_COLOR)
    drawText('To quit: Esc', SMALL_FONT, GAME_DISPLAY, 10 , 290, TEXT_COLOR)
    drawText('Press Enter', LRG_FONT, GAME_DISPLAY, 600, 750, TEXT_COLOR)
    
    pygame.display.update()
    getLoadingScreenInput()
    # Stop music
    pygame.mixer.music.stop() 
    # Limit to 60 frames per second
    FPS_CLOCK.tick(FPS)


    #################################
    #        main() GAME LOOP       #
    #################################
    while True:
       pygame.mixer.music.load('boss.mid')
       pygame.mixer.music.play(-1)
       runGame()
       pygame.mixer.music.stop()
       if (EARTH_DEFENSE <= 0):
         GAME_DISPLAY.blit(TITLE_IMG, (0, 0))
         drawText('DEFEAT', XTRA_LRG_FONT, GAME_DISPLAY, (GAME_WINDOW_WIDTH / 3) + 50, (GAME_WINDOW_HEIGHT / 3), RED)
         drawText('EARTH HAS BEEN DESTROYED', LRG_FONT, GAME_DISPLAY, (GAME_WINDOW_WIDTH / 3)- 130, (GAME_WINDOW_HEIGHT / 3) + 100, TEXT_COLOR)
         drawText('Press enter to play again or esc to quit', LRG_FONT, GAME_DISPLAY, 300, 750, TEXT_COLOR)
         pygame.display.update()
         getLoadingScreenInput()
         cleanUp(BULLETS,ALIEN1,ALIEN2) # Clear screen for the next game
        
        
       if playerCollision(PLAYER_RECT, ALIEN1) or playerCollision(PLAYER_RECT, ALIEN2) or PLAYER_RECT.colliderect(BOSS_RECT):
         GAME_DISPLAY.blit(TITLE_IMG, (0, 0))
         drawText('DEFEAT', XTRA_LRG_FONT, GAME_DISPLAY, (GAME_WINDOW_WIDTH / 3) + 50, (GAME_WINDOW_HEIGHT / 3), RED)
         drawText('YOU HAVE BEEN CAPTURED BY THE ALIENS', LRG_FONT, GAME_DISPLAY, (GAME_WINDOW_WIDTH / 3) - 230, (GAME_WINDOW_HEIGHT / 3) +100, TEXT_COLOR)
         drawText('Press enter to play again or esc to quit', LRG_FONT, GAME_DISPLAY, 300, 750, TEXT_COLOR)
         pygame.display.update()
         getLoadingScreenInput()
         cleanUp(BULLETS,ALIEN1,ALIEN2) # Clear screen for the next game


       if (PLAYER_WON == True):
         GAME_DISPLAY.blit(TITLE_IMG, (0, 0))
         drawText('VICTORY', XTRA_LRG_FONT, GAME_DISPLAY, (GAME_WINDOW_WIDTH / 3) + 50, (GAME_WINDOW_HEIGHT / 3), GREEN)
         drawText('THE ALIENS HAVE BEEN DEFEATED', LRG_FONT, GAME_DISPLAY, (GAME_WINDOW_WIDTH / 3) - 130, (GAME_WINDOW_HEIGHT / 3) +100, TEXT_COLOR)
         drawText('Press enter to play again or esc to quit', LRG_FONT, GAME_DISPLAY, 300, 750, TEXT_COLOR)
         pygame.display.update()
         getLoadingScreenInput()
         cleanUp(BULLETS,ALIEN1,ALIEN2) # Clear screen for the next game
       

def runGame():
    # Set up the start of the game
    global EARTH_DEFENSE, PLAYER_HP, BOSS_HP, SCORE, PLAYER_WON
    PLAYER_WON = False
    EARTH_DEFENSE = 100  # If this reaches 0, game over
    PLAYER_HP = 100 # If this reaches 0, game over
    BOSS_HP = 100 # If the player defeats the boss they win
    # Set the score, lvl, and frequency at which the alien moves
    SCORE = 0
    lvl, ALIEN1_SPEED = calcLvlAndAlienSpeed(SCORE) # Note: only change speed of Alien1
    PLAYER_RECT.topleft = (50, GAME_WINDOW_HEIGHT /2)
    #Put boss rect off the screen to start with
    BOSS_RECT.topright = (1600, GAME_WINDOW_HEIGHT /2)
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False
    shoot = False

    alien1_spawn_counter = 0
    alien2_spawn_counter = 0
    player_bullet_spawn_rate = 40
    alien_bullet_spawn_rate = 40

    effect = pygame.mixer.Sound('laser_fire.wav')

    #################################
    #     runGame() GAME LOOP       #
    #################################
    while True: # the game loop runs while the game part is playing
        
        # Calculate level and enemy speed,
        if lvl != BOSS_LVL:
            lvl, ALIEN1_SPEED = calcLvlAndAlienSpeed(SCORE) # Note: only change speed of Alien1
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            # Check if the key was pressed down 
            elif event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                    moveRight = False
                    moveLeft = False
                elif event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True
                    moveRight = False
                    moveLeft = False
                elif event.key == K_RIGHT or event.key == K_d:
                    moveUp = False
                    moveDown = False
                    moveRight = True
                    moveLeft = False
                elif event.key == K_LEFT or event.key == K_a:
                    moveUp = False
                    moveDown = False
                    moveRight = False
                    moveLeft = True
                elif event.key == K_SPACE:
                    shoot = True
            
                    
            # Check if the key was released
            # If you release the key, you are no longer moving
            # Set vars to false and terminate game if player last hit esc
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                        terminate()
                elif event.key == K_UP or event.key == K_w:
                    moveUp = False
                elif event.key == K_DOWN or event.key == K_s:
                    moveDown = False
                elif event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                elif event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                elif event.key == K_SPACE:
                    shoot = False

        # Add new ALIEN1 at the top of the screen, if needed.
        alien1_spawn_counter += 1
        if alien1_spawn_counter == ALIEN1_SPAWN_RATE:
            alien1_spawn_counter = 0
            ALIEN1_SIZE = ALIEN_SIZE
            rand_y1 = random.randint(10,GAME_WINDOW_HEIGHT-ALIEN1_SIZE-10)
            while rand_y1 == GAME_WINDOW_HEIGHT /2:
                rand_y1 = random.randint(10,GAME_WINDOW_HEIGHT-ALIEN1_SIZE-10)
            newAlien1 = {'rect': pygame.Rect(GAME_WINDOW_WIDTH, rand_y1, ALIEN1_SIZE, ALIEN1_SIZE),
                        'surface':pygame.transform.scale(ALIEN1_IMG, (ALIEN1_SIZE, ALIEN1_SIZE))}
            ALIEN1.append(newAlien1)

        # Add new ALIEN2 at the top of the screen, if needed.
        alien2_spawn_counter += 1
        if alien2_spawn_counter == ALIEN2_SPAWN_RATE:
            alien2_spawn_counter = 0
            ALIEN2_SIZE = ALIEN_SIZE
            rand_y2 = random.randint(10,GAME_WINDOW_HEIGHT-ALIEN2_SIZE-10)
            while rand_y2 == GAME_WINDOW_HEIGHT /2:
                rand_y1 = random.randint(10,GAME_WINDOW_HEIGHT-ALIEN1_SIZE-10)
            newAlien2 = {'rect': pygame.Rect(GAME_WINDOW_WIDTH, rand_y2, ALIEN2_SIZE, ALIEN2_SIZE),
                        'surface':pygame.transform.scale(ALIEN2_IMG, (ALIEN2_SIZE, ALIEN2_SIZE))} 
            ALIEN2.append(newAlien2)
            
        # add new bullet
        player_bullet_spawn_rate += 1
        if player_bullet_spawn_rate >= RELOAD_SPEED * 2 and shoot == True:
            player_bullet_spawn_rate = 0
            newBullet1 = {'rect':pygame.Rect(PLAYER_RECT.centerx+10, PLAYER_RECT.centery-25, BULLET_RECT.width, BULLET_RECT.height),
			 'surface':pygame.transform.scale(BULLET_IMG, (BULLET_RECT.width, BULLET_RECT.height))}
            newBullet2 = {'rect':pygame.Rect(PLAYER_RECT.centerx+10, PLAYER_RECT.centery+25, BULLET_RECT.width, BULLET_RECT.height),
			 'surface':pygame.transform.scale(BULLET_IMG, (BULLET_RECT.width, BULLET_RECT.height))}
            BULLETS.append(newBullet1)
            BULLETS.append(newBullet2)
            effect.play(1)

        # Move the player around.
        if moveLeft and PLAYER_RECT.left > 0:
            PLAYER_RECT.move_ip(-1 * PLAYER_SPEED, 0)
        if moveRight and PLAYER_RECT.right < GAME_WINDOW_WIDTH-10:
            PLAYER_RECT.move_ip(PLAYER_SPEED, 0)
        if moveUp and PLAYER_RECT.top > 30:
            
            PLAYER_RECT.move_ip(0, -1 * PLAYER_SPEED)
        if moveDown and PLAYER_RECT.bottom < GAME_WINDOW_HEIGHT-10:
            PLAYER_RECT.move_ip(0, PLAYER_SPEED)

        # Move the ALIEN1 down and add the bullets
        for a1 in ALIEN1:
            a1['rect'].move_ip(-1*ALIEN1_SPEED, 0)
            # add new alien1 bullets 
            alien_bullet_spawn_rate +=1
            if alien_bullet_spawn_rate >= RELOAD_SPEED * 30: # Include multiplier to slow reload speed
                alien_bullet_spawn_rate = 0
                alienBullet = {'rect':pygame.Rect(a1['rect'].centerx, a1['rect'].centery, ALIEN_BULLET_RECT.width, ALIEN_BULLET_RECT.height),
                             'surface':pygame.transform.scale(ALIEN_BULLET_IMG, (ALIEN_BULLET_RECT.width, ALIEN_BULLET_RECT.height))}
                ALIEN_BULLETS.append(alienBullet)

        # Move the ALIEN2 down and add the bullets
        for a2 in ALIEN2:
            a2['rect'].move_ip(-1*ALIEN2_SPEED,0)
            # add new alien1 bullets 
            alien_bullet_spawn_rate +=1
            if alien_bullet_spawn_rate >= RELOAD_SPEED * 30: # Include multiplier to slow reload speed
                alien_bullet_spawn_rate = 0
                alienBullet = {'rect':pygame.Rect(a2['rect'].centerx, a2['rect'].centery, ALIEN_BULLET_RECT.width, ALIEN_BULLET_RECT.height),
                             'surface':pygame.transform.scale(ALIEN_BULLET_IMG, (ALIEN_BULLET_RECT.width, ALIEN_BULLET_RECT.height))}
                ALIEN_BULLETS.append(alienBullet)

        # Move the boss around.
        if lvl == BOSS_LVL:
            if BOSS_RECT.left > 0:
                BOSS_RECT.move_ip(-1 * BOSS_SPEED, 0)   
            # add new boss bullets 
            alien_bullet_spawn_rate += 1
            if alien_bullet_spawn_rate >= RELOAD_SPEED * 20: # Include multiplier to slow reload speed
                alien_bullet_spawn_rate = 0
                alienBullet = {'rect':pygame.Rect(BOSS_RECT.centerx, BOSS_RECT.centery, ALIEN_BULLET_RECT.width, ALIEN_BULLET_RECT.height),
                             'surface':pygame.transform.scale(ALIEN_BULLET_IMG, (ALIEN_BULLET_RECT.width, ALIEN_BULLET_RECT.height))}
                ALIEN_BULLETS.append(alienBullet)

        # move the player bullet
        for b in BULLETS:
            b['rect'].move_ip(1 * BULLET_SPEED, 0)

        # move the alien bullet
        for b2 in ALIEN_BULLETS:
            b2['rect'].move_ip(-1 * ALIEN_BULLET_SPEED, 0)

        # If boss reaches Earth, game over
        if BOSS_RECT.left < 20:
            EARTH_DEFENSE = 0
            break

        # Delete ALIEN1 that continued past the screen.
        for a1 in ALIEN1[:]:
            if a1['rect'].left < 0:
                ALIEN1.remove(a1)
                EARTH_DEFENSE -= 5

        # Delete ALIEN2 that continued past the screen.
        for a2 in ALIEN2[:]:
            if a2['rect'].left < 0:
                ALIEN2.remove(a2)
                EARTH_DEFENSE -= 5
                        
        # Delete all player bullets that continued past the screen
        for b in BULLETS[:]:
                    if b['rect'].right>GAME_WINDOW_WIDTH:
                        BULLETS.remove(b)

        # Check if the alien bullet hit the player
        if hitPlayer(ALIEN_BULLETS, PLAYER_RECT):
            PLAYER_HP -= 5
            if (PLAYER_HP <= 0):
                    EARTH_DEFENSE = 0 # The game ends because player died
                    break

        # Check if the player bullet hit the boss
        if lvl == BOSS_LVL:
           if hitBoss(BULLETS, BOSS_RECT):
             BOSS_HP -= 5
             if (BOSS_HP <= 0):
                PLAYER_WON = True
                GAME_DISPLAY.blit(BIG_EXPLOSION_IMG, BOSS_RECT)
                pygame.display.update(BOSS_RECT)
                # Limit to 60 frames per second
                FPS_CLOCK.tick(FPS)
                pygame.time.delay(30)
                break

        # Check if the player bullet hit the aliens
        for a1 in ALIEN1:
            if hitAlien1(BULLETS, ALIEN1, a1):
                SCORE += 1
                GAME_DISPLAY.blit(EXPLOSION_IMG, a1['rect'])
                pygame.display.update(a1['rect'])
                # Limit to 60 frames per second
                FPS_CLOCK.tick(FPS)
                ALIEN1.remove(a1)
    
        for a2 in ALIEN2:
            if hitAlien2(BULLETS, ALIEN2, a2):
                SCORE += 1
                GAME_DISPLAY.blit(EXPLOSION_IMG, a2['rect'])
                pygame.display.update(a2['rect'])
                # Limit to 60 frames per second
                FPS_CLOCK.tick(FPS)
                ALIEN2.remove(a2)      

        # Display the background in-game image
        GAME_DISPLAY.blit(BACKGROUND_IMG, (0, 0))

        # Draw the player
        GAME_DISPLAY.blit(PLAYER_IMG, PLAYER_RECT)

        # Check if we need to draw the boss and bullets
        if lvl == BOSS_LVL: 
            # Draw the boss
            GAME_DISPLAY.blit(BOSS_IMG, BOSS_RECT)

        # Draw each alien
        for a1 in ALIEN1:
            GAME_DISPLAY.blit(a1['surface'], a1['rect'])

        for a2 in ALIEN2:
            GAME_DISPLAY.blit(a2['surface'], a2['rect'])

        # Draw each bullet
        for b in BULLETS:
            GAME_DISPLAY.blit(b['surface'], b['rect'])

        # Draw each bullet
        for b2 in ALIEN_BULLETS:
            GAME_DISPLAY.blit(b2['surface'], b2['rect'])

        # Draw the score and how many Aliens got past your defenses
        drawText('Earth Defense: %s percent' % (EARTH_DEFENSE), SMALL_FONT, GAME_DISPLAY, 290, 20, TEXT_COLOR)
        drawText('Aliens eliminated: %s' % (SCORE), SMALL_FONT, GAME_DISPLAY, 625, 20, TEXT_COLOR)
        drawText('Level: %s' % (lvl), SMALL_FONT, GAME_DISPLAY, 895, 20, TEXT_COLOR)
        drawText('HP: %s' % (PLAYER_HP), SMALL_FONT, GAME_DISPLAY, 1050, 20, TEXT_COLOR)
        drawText('_______________________________________________________________________________________________________________________________',
                 SMALL_FONT, GAME_DISPLAY, 0, 30, TEXT_COLOR)

        # update the display
        pygame.display.update()
            
        # Check if any of the aliens ran into the player.
        if playerCollision(PLAYER_RECT, ALIEN1):
            break
        
        if playerCollision(PLAYER_RECT, ALIEN2):
           break

        if PLAYER_RECT.colliderect(BOSS_RECT):
            break
        
        # check if Earth's defense is depleted, resulting in game over
        if EARTH_DEFENSE <= 0:
            break
        
        FPS_CLOCK.tick(FPS)

# Calculate the level and the alien speed
def calcLvlAndAlienSpeed(SCORE):
    # Based on the score, return the level the player is on and
    # how many seconds pass until a enemy moves one space.
    lvl = int(SCORE / 50) + 1
    alien_speed = ALIEN1_SPEED + (lvl * 0.5)
    return lvl, alien_speed

# Clean up aliens and bullets
def cleanUp(BULLETS, ALIEN1, ALIEN2):
   for i in range(GAME_WINDOW_WIDTH): 
     for b in BULLETS:
         BULLETS.remove(b)
     for b2 in ALIEN_BULLETS:
         ALIEN_BULLETS.remove(b2)
     for a1 in ALIEN1:
         ALIEN1.remove(a1)
     for a2 in ALIEN2:
         ALIEN2.remove(a2)

# Draw text on the screen
def drawText(text, font, surface, width, height, text_color):
    txt_obj = font.render(text, True, text_color)
    txt_rect = txt_obj.get_rect()
    txt_rect.topleft = (width, height)
    surface.blit(txt_obj, txt_rect)

# Get user input when not in game
def getLoadingScreenInput():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing esc quits
                    terminate()
                if event.key == K_RETURN:
                    return

# Check to see if  the player hit the boss
def hitBoss(BULLETS, BOSS_RECT):
    for b in BULLETS:
        if b['rect'].colliderect(BOSS_RECT):
            BULLETS.remove(b)
            return True
    return False

# Check to see if the player hit alien1
def hitAlien1(BULLETS, ALIEN1, a1):
    for b in BULLETS:
        if b['rect'].colliderect(a1['rect']):
            BULLETS.remove(b)
            return True
    return False

# Check to see if the player hit alien2
def hitAlien2(BULLETS, ALIEN2, a2):
    for b in BULLETS:
        if b['rect'].colliderect(a2['rect']):
            BULLETS.remove(b)
            return True
    return False

# Check if the player was hit by an enemy bullet
def hitPlayer(ALIEN_BULLETS, PLAYER_RECT):
    for b2 in ALIEN_BULLETS:
        if b2['rect'].colliderect(PLAYER_RECT):
            ALIEN_BULLETS.remove(b2)
            return True
    return False

# Check to see if the player collided into an alien
def playerCollision(PLAYER_RECT, Alien):
    for i in Alien:
        if PLAYER_RECT.colliderect(i['rect']):
            return True
    return False

def terminate():
    pygame.quit()
    sys.exit()

# Call the main function, start up the game
if __name__ == '__main__':
    main()
