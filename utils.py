import pygame
from components.brick import Brick
from components.ball import Ball
from components.bullet import Bullet
from components.paddle import Paddle
from components.button import Button
from config import Config
import random

cfg = Config()
screen_scaler = cfg.SCREEN_SCALER
color_list = [cfg.RED, cfg.ORANGE, cfg.YELLOW, cfg.GREEN, cfg.WHITE, cfg.CYAN, cfg.LIGHTBLUE]


def display_message(message, screen):
    font = pygame.font.Font(None, 74)
    text = font.render(message, 1, cfg.WHITE)
    screen.blit(text, (200*screen_scaler[0],300*screen_scaler[1]))
    pygame.display.flip()
    pygame.time.wait(3000)

def build_bricks(color_list, brick_no):
    all_bricks = pygame.sprite.Group()
    for i in range(brick_no):
        # print(int(i / 7))
        brick = Brick(color_list[int(i / 7)],80*screen_scaler[0],30*screen_scaler[1])  # first seven bricks -> first color of list, next 7 bricks -> second color of list
        brick.rect.x = 60*screen_scaler[0] + (i% 7)* 100*screen_scaler[0]
        brick.rect.y = 20*screen_scaler[1] + (int(i / 7) + 1) * 40*screen_scaler[1]  #  # first seven bricks -> one line, next 7 bricks -> second line, ....
        # all_sprites_list.add(brick)
        all_bricks.add(brick)
    return all_bricks

def make_special_bricks(all_bricks, number_of_special_bricks):
    special_bricks = random.sample([brick for brick in all_bricks], number_of_special_bricks)
    # print(special_bricks)
    for brick in all_bricks:
        if brick in special_bricks:
            # print("yes")
            brick.change_color(cfg.WHITE)
    return all_bricks, special_bricks



def stage1(screen):
    """
    This is the first window. There are two buttons: Start game and Exit.
    """
    FPS = 5
    screen_scaler = cfg.SCREEN_SCALER
    # print(screen_scaler)
    button1 = Button((300*screen_scaler[0], 100*screen_scaler[1]), (200*screen_scaler[0], 100*screen_scaler[1]), (0, 137, 210), "Start Game")
    button2 = Button((300*screen_scaler[0], 300*screen_scaler[1]), (200*screen_scaler[0], 100*screen_scaler[1]), (0, 137, 210), "EXIT")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                # go to stage2
                main_stage(screen)
            if button2.is_clicked(event):
                # exit
                pygame.quit()
                exit()

        # - draws -

        screen.fill((32, 50, 56))    
        button1.draw(screen)
        button2.draw(screen)
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)



def main_stage(screen):
    """
    This is the main game function. 
    - Initialize the game component objects (Ball, paddle, bricks, bullet)
    - Initialize object positions
    - Start game loop
    - Handle key events
    - Implement game logic
    - Detect collisions
    - Update the screen
    """
    bg_image_path = cfg.BACKGROUND_IMAGE_PATH
    background = pygame.image.load(bg_image_path).convert()
    
    score = 0
    lives = cfg.LIFE

    screen_scaler = cfg.SCREEN_SCALER

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    #Create the Paddle
    paddle = Paddle(cfg.LIGHTBLUE, 100*screen_scaler[0], 10*screen_scaler[1])
    paddle.rect.x = 350*screen_scaler[0]
    paddle.rect.y = 560*screen_scaler[1]

    #Create the ball sprite
    ball = Ball(cfg.WHITE,10*screen_scaler[0],10*screen_scaler[1])
    ball.rect.x = 345*screen_scaler[0]
    ball.rect.y = 195*screen_scaler[1]

    balls_sprite_list = pygame.sprite.Group()
    balls_sprite_list.add(ball)

    bullet = Bullet(5*screen_scaler[0], 20*screen_scaler[1])
    bullet.rect.x = 386*screen_scaler[0]
    bullet.rect.y = 490*screen_scaler[1]
    check = False

    # bullet_sprite_group = pygame.sprite.Group()


    all_bricks = build_bricks(color_list, 30)
    # print(len(all_bricks))
    number_of_special_bricks = 2
    special_bricks = []
    all_bricks, special_bricks = make_special_bricks(all_bricks, number_of_special_bricks)

    # Add the paddle and the ball to the list of sprites
    all_sprites_list.add(paddle)

    # The loop will carry on until the user exits the game (e.g. clicks the close button).
    carryOn = True

    clock = pygame.time.Clock()

    count = 0
    brick_speed_divisor = 8


    # -------- Main Program Loop -----------

    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
                pygame.quit()
                exit()
                

        #Moving the paddle when the use uses the arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            paddle.moveRight(5)
        if keys[pygame.K_UP]:
            paddle.moveDown(5)
        if keys[pygame.K_DOWN]:
            paddle.moveUp(5)
        if keys[pygame.K_SPACE]:
                if check is False:
               
                    check=True
                    bullet.rect.x=paddle.rect.x*screen_scaler[0]
                    bullet.rect.y = paddle.rect.y*screen_scaler[1] - 16*screen_scaler[1]
                   
            
        # --- Game logic should go here
        all_sprites_list.update()
        balls_sprite_list.update()

        # to slow down the movement
        if count % brick_speed_divisor == 0:
            all_bricks.update()
        
        # game over if bricks are all the way down
        for brick in all_bricks:
            # print(brick.rect.y)
            if brick.rect.y > 560*screen_scaler[1]:
                display_message("Game Over", screen)
                #Stop the Game
                carryOn=False


        for ball in balls_sprite_list:
        #Check if the ball is bouncing against any of the 4 walls:
            if ball.rect.x>=790*screen_scaler[0]:
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.x<=0:
                ball.velocity[0] = -ball.velocity[0]

            # if ball drops    
            if ball.rect.y>560*screen_scaler[1]:
                ball.velocity[1] = -ball.velocity[1]
                lives -= 1
                if lives == 0:
                    display_message("Game Over", screen)
                    #Stop the Game
                    carryOn=False
                if len(balls_sprite_list) > 1:
                    ball.kill()

            if ball.rect.y<40*screen_scaler[1]:
                ball.velocity[1] = -ball.velocity[1]
 

        #Detect collisions between the ball and the paddles
        for ball in balls_sprite_list:
            if pygame.sprite.collide_mask(ball, paddle):
                # ball.rect.x -= ball.velocity[0]
                # ball.rect.y -= ball.velocity[1]
                # ball.bounce()
                ball.velocity[1] = -ball.velocity[1]

        #Check if there is the ball collides with any of bricks
        for ball in balls_sprite_list:
            brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
            for brick in brick_collision_list:
                if brick in special_bricks:
                    #Create the ball sprite
                    ball = Ball(cfg.WHITE,10,10)
                    ball.rect.x = 345*screen_scaler[0]
                    ball.rect.y = 195*screen_scaler[1]

                    # balls_sprite_list = pygame.sprite.Group()
                    balls_sprite_list.add(ball)
                ball.bounce()
                score += 1
                brick.kill()
                if len(all_bricks)==0:
                    #Display Level Complete Message for 3 seconds
                        display_message("Level Complete", screen)
                        #Stop the Game
                        carryOn=False
        brick_collision_list = pygame.sprite.spritecollide(paddle,all_bricks,False)
        if len(brick_collision_list) > 0:
            display_message("Game Over", screen)
            #Stop the Game
            carryOn=False
        # shooting. check if bullets collides with bricks
        
        brick_collision_list = pygame.sprite.spritecollide(bullet,all_bricks,False)
        if len(brick_collision_list) > 0:

            score += 1
            brick_collision_list[0].kill()
            bullet.kill()
            check = False
            bullet.rect.x = 386*screen_scaler[0]
            bullet.rect.y = 490*screen_scaler[1]
            if len(all_bricks)==0:

            #Display Level Complete Message for 3 seconds
                display_message("Level Complete", screen)

                #Stop the Game
                carryOn=False
        # --- Drawing code should go here
        # First, clear the screen to dark blue.

        
        
        # screen.fill(bg)
        screen.blit(background, (0, 0))
        pygame.draw.line(screen, cfg.WHITE, [0*screen_scaler[0], 38*screen_scaler[1]], [800*screen_scaler[0], 38*screen_scaler[1]], 2)

        #Display the score and the number of lives at the top of the screen
        font = pygame.font.Font(None, int(34*screen_scaler[0]))
        text = font.render("Score: " + str(score), 1, cfg.WHITE)
        screen.blit(text, (20*screen_scaler[0],10*screen_scaler[1]))
        text = font.render("Lives: " + str(lives), 1, cfg.WHITE)
        screen.blit(text, (650*screen_scaler[0],10*screen_scaler[1]))

        # if bullets crosses upper screen
        if bullet.rect.y<=0:
            bullet.rect.y=490*screen_scaler[1]
            check=False
        if check:
            screen.blit(bullet.image, bullet.rect)
            bullet.rect.y-=5*screen_scaler[1]

        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)
        all_bricks.draw(screen)
        balls_sprite_list.draw(screen)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

        count += 1



