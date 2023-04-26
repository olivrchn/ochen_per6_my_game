WIDTH = 1300
HEIGHT = 900
PLAYER_ACC = 2
PLAYER_FRICTION = -0.4
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
MOB_ACC = 2
MOB_FRICTION = -0.3
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
GREEN = (50,255,0)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 15, (200,200,200), "bouncey"),
                 (125, HEIGHT - 350, 100, 15, (200,200,200), "disappearing "),
                 (350, 200, 100, 15, (200,200,200), "normal"),
                 (175, 100, 50, 15, (200,200,200), "normal"),
                 (200, 100, 60, 15, (200,200,200), "normal"),
                 (750, 500, 100, 15, (200,200,200), "normal"),
                 (900, 250, 100, 15, (200,200,200), "normal")]
#                (x point, y point , width of plat, thickness of palt, color)