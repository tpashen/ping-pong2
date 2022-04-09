#1

#2

#3
# Game Scene
from turtle import window_height


back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = True
clock = time.Clock()
FPS = 60

racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = GameSprite("tenis_ball.png", 200, 200, 4, 50, 50)

font.init()
font = font.Font("calibri.ttf", 35)
lose1 = font.render("PLAYER 1 LOSE!", True, (180, 0, 0))
lose2 = font.render("PLAYER 2 LOSE!", True, (180, 0, 0))
#4

#5
