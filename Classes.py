from turtle import Turtle, Screen
import time
from random import randint

class Settings:
    width= 600
    height= 600
    cell_size = 21
    qstruct = 20
    delay = 125

class Operations:
    def coord(num): # генерация случайного числа
        return randint(-num / 2 + Settings.cell_size // 2, num // 2 - Settings.cell_size // 2)

    def round_coord(num): # округление числа до делимости на ширину змеи
        if num < 0:
            num1 = -num % Settings.cell_size
            num = num + num1
            return num
        else:
            num1 = num % Settings.cell_size
            num = num - num1
            return num
    
    def checkcoord(): # проверка не совпадают ли сгенерированные координаты с координатами уже существующих объектов
        x = Operations.round_coord(Operations.coord(Settings.width))
        y = Operations.round_coord(Operations.coord(Settings.height))
        posx = []
        posy = []
        for struct in structs:
            posx.append(struct.pos()[0])
            posy.append(struct.pos()[1])
        for body in snake:
            posx.append(body.pos()[0])
            posy.append(body.pos()[1])
        if apples[0] != "":
            posx.append(apples[0].pos()[0])
            posx.append(apples[0].pos()[1])
        while ((x >= -Settings.cell_size * 2 and x <= Settings.cell_size * 2) and (y >= -Settings.cell_size * 2 and y <= Settings.cell_size * 2)) or (x in posx and y in posy):
            x = Operations.round_coord(Operations.coord(Settings.width))
            y = Operations.round_coord(Operations.coord(Settings.height))
        return x, y

class Field:
    def genfield(): # обводка поля + закрашивание внутренней части
        field = Turtle()
        field.speed(3)
        field.color("black", "#24db91")
        field.penup()
        field.goto(Settings.width// 2 // Settings.cell_size * Settings.cell_size - Settings.cell_size // 2, -Settings.height // 2 // Settings.cell_size * Settings.cell_size + Settings.cell_size // 2)
        field.pendown()
        field.begin_fill()
        field.goto(Settings.width// 2 // Settings.cell_size * Settings.cell_size - Settings.cell_size // 2, Settings.height // 2 // Settings.cell_size * Settings.cell_size - Settings.cell_size // 2)
        field.goto(-Settings.width// 2 // Settings.cell_size * Settings.cell_size + Settings.cell_size // 2, Settings.height // 2 // Settings.cell_size * Settings.cell_size - Settings.cell_size // 2)
        field.goto(-Settings.width// 2 // Settings.cell_size * Settings.cell_size + Settings.cell_size // 2, -Settings.height // 2 // Settings.cell_size * Settings.cell_size + Settings.cell_size // 2)
        field.goto(Settings.width// 2 // Settings.cell_size * Settings.cell_size - Settings.cell_size // 2, -Settings.height // 2 // Settings.cell_size * Settings.cell_size + Settings.cell_size // 2)
        field.end_fill()
        field.hideturtle()

    def genstruct(): # генерация стен
        for _ in range(Settings.qstruct):
            xy = Operations.checkcoord()
            x = xy[0]
            y = xy[1]
            struct = Turtle()
            struct.speed(0)
            struct.shape('square')
            struct.color('black')
            struct.penup()
            struct.goto(x, y)
            structs.append(struct)

class Apples:
    def genapple(): # генерация яблока
        apple = Turtle()
        apple.speed(0)
        apple.shape('circle')
        apple.shapesize(0.6)
        apple.color('red')
        apple.penup()
        apple.hideturtle()
        apples[0] = apple

    def regenapples(): # изменение положения яблока
        xy = Operations.checkcoord()
        x = xy[0]
        y = xy[1]
        apples[0].goto(x, y)
        apples[0].showturtle()

class Snake: 
    def genhead(): # генерация головы
        head = Turtle()
        head.speed(0)
        head.shape('square')
        head.color('darkgreen')
        head.penup()
        head.direction = "stop"
        head.predirection = 0
        snake.append(head)

    def gensnake(): # генерация тела змеи
        body = Turtle()
        body.speed(0)
        body.shape("square")
        body.color("green")
        body.penup()
        if len(snake) != 0:
            body.goto(snake[-1].pos()[0], snake[-1].pos()[1])
        else:
            body.goto(snake[0].pos()[0], snake[0].pos()[1])
        snake.append(body)

class Moving:
    def goup(): # изменение на движение вверх
        if snake[0].direction != "down" and snake[0].predirection == 0: # проверка на то, чтобы змея не поворачивалась в саму себя
            snake[0].direction = "up"
            snake[0].predirection = 1

    def godown(): # изменение на движение вниз
        if snake[0] .direction != "up" and snake[0].predirection == 0: # проверка на то, чтобы змея не поворачивалась в саму себя
            snake[0].direction = "down"
            snake[0].predirection = 1

    def goleft(): # изменение на движение влево
        if snake[0].direction != "right" and snake[0].predirection == 0: # проверка на то, чтобы змея не поворачивалась в саму себя
            snake[0].direction = "left"
            snake[0].predirection = 1

    def goright(): # изменение на движение вправо
        if snake[0].direction != "left" and snake[0].predirection == 0: # проверка на то, чтобы змея не поворачивалась в саму себя
            snake[0].direction = "right"
            snake[0].predirection = 1

    def move(): # само движение
        if snake[0].direction == "up": # проверка на то, чтобы если игрок быстро нажал 2 клавиши, то змейка не повернулось в сторону самой себя
            y = snake[0].ycor()
            snake[0].sety(y+21)
            snake[0].predirection = 0
        if snake[0].direction == "down":
            y = snake[0].ycor()
            snake[0].sety(y-21)
            snake[0].predirection = 0
        if snake[0].direction == "left":
            x = snake[0].xcor()
            snake[0].setx(x-21)
            snake[0].predirection = 0
        if snake[0].direction == "right":
            x = snake[0].xcor()
            snake[0].setx(x+21)
            snake[0].predirection = 0

class Game:
    def game(scr): # активация всех стартовых функций
        global screen, structs, apples, snake
        screen = scr

        structs = []
        apples = ['']
        snake = []

        Field.genfield()
        Field.genstruct()
        Apples.genapple()
        Apples.regenapples()
        Snake.genhead()
        screen.ontimer(Game.nextframe, Settings.delay)

    def nextframe(): # следующее движение змейки
        screen.update()
        Game.check_collision()
        Game.consumption()

        for index in range(len(snake)-1, 1, -1): # перемещение тела змеи
            x = snake[index-1].xcor()
            y = snake[index-1].ycor()
            snake[index].goto(x, y)

        if len(snake) > 1: # 1 кусочка змеи за головой
            x = snake[0].xcor()
            y = snake[0].ycor()
            snake[1].goto(x, y)

        Moving.move()

        screen.ontimer(Game.nextframe, Settings.delay) # повторение действия   
    
    def check_collision(): # проверка на столкновение
        global snake

        # првоерка на столкновение с границей поля
        if (snake[0].xcor() == (Settings.width// 2 // 21 - 1) * 21 and snake[0].direction == "right") or (snake[0].xcor() == (-Settings.width// 2 // 21 + 1) * 21 and snake[0].direction == "left") or (snake[0].ycor() == (Settings.height// 2 // 21 - 1) * 21 and snake[0].direction == "up") or (snake[0].ycor() == (-Settings.height// 2 // 21 + 1) * 21 and snake[0].direction == "down"):
            time.sleep(1)
            snake[0].goto(0, 0)
            snake[0].direction = "Stop"
            for body in snake:
                body.hideturtle()
            snake = []
            Snake.genhead()

        # проверка на столкновение с стеной
        for struct in structs:
            if (snake[0].xcor() == struct.pos()[0] - Settings.cell_size and snake[0].ycor() == struct.pos()[1] and snake[0].direction == "right") or (snake[0].xcor() == struct.pos()[0] + Settings.cell_size and snake[0].ycor() == struct.pos()[1] and snake[0].direction == "left") or (snake[0].ycor() == struct.pos()[1] - Settings.cell_size and snake[0].xcor() == struct.pos()[0] and snake[0].direction == "up") or (snake[0].ycor() == struct.pos()[1] + Settings.cell_size and snake[0].xcor() == struct.pos()[0] and snake[0].direction == "down"):
                time.sleep(1)
                snake[0].goto(0, 0)
                snake[0].direction = "stop"
                for body in snake:
                    body.hideturtle()
                snake = []
                Snake.genhead()
        
        # проверка на столкновение с телом змеи
        for body in snake:
            if (snake[0].xcor() == body.pos()[0] - Settings.cell_size and snake[0].ycor() == body.pos()[1] and snake[0].direction == "right") or (snake[0].xcor() == body.pos()[0] + Settings.cell_size and snake[0].ycor() == body.pos()[1] and snake[0].direction == "left") or (snake[0].ycor() == body.pos()[1] - Settings.cell_size and snake[0].xcor() == body.pos()[0] and snake[0].direction == "up") or (snake[0].ycor() == body.pos()[1] + Settings.cell_size and snake[0].xcor() == body.pos()[0] and snake[0].direction == "down"):
                time.sleep(1)
                snake[0].goto(0, 0)
                snake[0].direction = "stop"
                for body1 in snake:
                    body1.hideturtle()
                snake = []
                Snake.genhead()

    # поедание яблок
    def consumption():
        if apples[0] != "" and snake[0].distance(apples[0]) < Settings.cell_size: # проверка на расстояние между головой змеи и яблоком
            apples[0].hideturtle()
            Apples.regenapples()
            Snake.gensnake()