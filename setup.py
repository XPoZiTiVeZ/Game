import Game
import Screen
from Settings import Settings
from time import sleep

def clearall():
    for turtle in Screen.SnakeScreen().screen.turtles():
        turtle.penup()
        turtle.hideturtle()
        turtle.clear()
        turtle.home()

def getclickcoords(x, y):
    if x > -130 and x < 130 and y > 15 and y < 75:
        if Screen.screen_now == "menu":
            clearall()
            Screen.SnakeScreen().get_screen(fieldsize=Settings.fieldsize, type="game")
            Game.Game.game(Settings.fieldsize, Settings.delay, Settings.qstruct, Settings.superapple, Screen.SnakeScreen.screen)

    if ((x > -45 and x < 45 and y > -105 and y < -15) or (x > -45 and x < 45 and y > -85 and y < -35)):
        if Screen.screen_now == "menu":
            clearall()
            Screen.SnakeScreen().get_screen(type="settings")

    if x > -Settings.fieldsize//2-45 and x < -Settings.fieldsize//2+5 and y > Settings.fieldsize//2-10 and y < Settings.fieldsize//2+40:
        if Screen.screen_now == "game":
            clearall()
            Screen.SnakeScreen().get_screen(type="menu")

    if x > -Screen.SnakeScreen().settingsx//2-45 and x < -Screen.SnakeScreen().settingsx//2+5 and y > Screen.SnakeScreen().settingsy//2-10 and y < Screen.SnakeScreen().settingsy//2+40:
        if Screen.screen_now == "settings":
            clearall()
            Screen.SnakeScreen().get_screen(type="menu")

    if x > -95 and x < 95 and y > -285 and y < -245:
        if Screen.screen_now == "menu":
            clearall()
            Screen.SnakeScreen().screen.bye()

    if x > -170 and x < 170 and y > 60 and y < 100:
        if Screen.screen_now == "settings":
            clearall()
            if Settings.fieldsize == 400:
                Settings.fieldsize = 500
            elif Settings.fieldsize == 500:
                Settings.fieldsize = 600
            elif Settings.fieldsize == 600:
                Settings.fieldsize = 700
            else:
                Settings.fieldsize = 400
            Screen.SnakeScreen().get_screen(type="settings")

    if x > -170 and x < 170 and y > 10 and y < 50:
        if Screen.screen_now == "settings":
            clearall()
            if Settings.delay == 100:
                Settings.delay = 140
            elif Settings.delay == 140:
                Settings.delay = 130
            elif Settings.delay == 130:
                Settings.delay = 120
            elif Settings.delay == 120:
                Settings.delay = 110
            elif Settings.delay == 110:
                Settings.delay = 100
            else:
                Settings.delay = 100
            Screen.SnakeScreen().get_screen(type="settings")
    
    if x > -170 and x < 170 and y > -40 and y < 0:
        if Screen.screen_now == "settings":
            clearall()
            if Settings.qstruct == 0:
                Settings.qstruct = 10
            elif Settings.qstruct == 10:
                Settings.qstruct = 20
            elif Settings.qstruct == 20:
                Settings.qstruct = 30
            elif Settings.qstruct == 30:
                Settings.qstruct = 40
            elif Settings.qstruct == 40:
                Settings.qstruct = 50
            else:
                Settings.qstruct = 0
            Screen.SnakeScreen().get_screen(type="settings")

    if x > -170 and x < 170 and y > -90 and y < -50:
        if Screen.screen_now == "settings":
            clearall()
            if Settings.superapple:
                Settings.superapple = False
            else:
                Settings.superapple = True
            Screen.SnakeScreen().get_screen(type="settings")

try:
    if __name__ == "__main__":
        Screen.SnakeScreen().get_screen(type="menu")
        Screen.SnakeScreen().screen.listen()
        Screen.SnakeScreen().screen.onscreenclick(getclickcoords)
        Screen.SnakeScreen().screen.onkeypress(Game.Moving.goup, "Up")
        Screen.SnakeScreen().screen.onkeypress(Game.Moving.goleft, "Left")
        Screen.SnakeScreen().screen.onkeypress(Game.Moving.godown, "Down")
        Screen.SnakeScreen().screen.onkeypress(Game.Moving.goright, "Right")
        while True:
            Screen.SnakeScreen().screen.update()
except:
    pass