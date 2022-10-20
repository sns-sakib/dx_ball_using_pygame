# The Breakout Game
- Implementation of the breakout game using the Pygame library

## Project Structure:
```bash
│   button.py
│   config.py
│   main.py
│   README.md
│   utils.py
│
├───components
│      ball.py
│      brick.py
│      bullet.py
│      paddle.py
│
│
├───static_files
│       background.jpg
│       bullet.png
```
# Environment Setup
- Setup Pygame library
```bash
pip install pygame
```

## How to play
### step 1:
- Run the main.py file
```bash
python main.py
```
### step 2: 
- Click start game to play.
### step 3:
- Then comes the game window. Move the paddle up (arrow key up), down (arrow key down), left (arrow key left), right (arrow key right). Dont drop the ball. Try to hit the bricks.  If ball drops, one life is lost.
- Shoot the bricks with Spacebar.
- Level complete if all the bricks are hit. 
- Game over if all lives are lost, or bricks touch the paddle.

### step 4:
- Click exit button/ close to exit the game. 


## Modification
- Modify the game parameters in the config.py file
```python
    # colors
    WHITE = (255,255,255)
    DARKBLUE = (36,90,190)
    LIGHTBLUE = (0,176,240)
    RED = (255,0,0)
    ORANGE = (255,100,0)
    YELLOW = (255,255,0)
    GREEN = (0, 255, 0)
    CYAN = (0,255,255)

    SIZE = (800, 600) # screen size

    SCREEN_SCALER =(SIZE[0]/800, SIZE[1]/600)  # helps to scale game objects according to size
    LIFE = 100 # how many lives

    NO_OF_BRICKS = 35 # How many bricks in the game. multiple of 7

    BACKGROUND_IMAGE_PATH = "static_files\\background.jpg"
    BULLET_IMAGE_PATH = "static_files\\bullet.png"
```

## Game features
- Multiple screen( includes introductory screen)
- Game window size can be changed. Game objects are responsive to size.
- Paddle can shoot the bricks
- Paddle can move up, down, left right
- Bricks keep going down after some frames interval
- Balls are doubled if hit some special surprise bricks

## Features that can be implemented
- Choose difficulty level at the start
- Build an AI bot to play the game using Q learning
  
