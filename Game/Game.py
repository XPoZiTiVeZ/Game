from turtle import Turtle
from time import perf_counter, sleep
from Game.Operations import Operations
from Game.Field import Field

class Apples:
    apple = Turtle()
    apple.name = "apple"
    apple.hideturtle()
    
    superapple = Turtle()
    superapple.name = "superapple"
    superapple.hideturtle()

    def genapple(): # генерация яблока
        Apples.apple.speed(0)
        Apples.apple.shape('circle')
        Apples.apple.shapesize(0.6)
        Apples.apple.color('red')
        Apples.apple.penup()
        Apples.apple.showturtle()

    def gensuperapple(): # генерация особого яблока
        Apples.superapple.speed(0)
        Apples.superapple.shape('circle')
        Apples.superapple.shapesize(1)
        Apples.superapple.color('#8b00ff')
        Apples.superapple.penup()
        Apples.superapple.hideturtle()

    def regenapples(): # изменение положения яблока
        xy = Operations.checkcoord(Game.structs, Snake.snake, Game.fieldsize, Game.cell_size)
        x = xy[0]
        y = xy[1]
        Apples.apple.goto(x, y)

    def regensuperapples(): # изменение положения особого яблока
        xy = Operations.checkcoord(Game.structs, Snake.snake, Game.fieldsize, Game.cell_size)
        x = xy[0]
        y = xy[1]
        Apples.superapple.goto(x, y)

class Snake:
    head = Turtle()
    head.name = "head"
    head.hideturtle()

    body = Turtle()
    body.name = "body"
    body.hideturtle()
    body.number = 1

    snake = []
    bodies = []

    def genhead(): # генерация головы
        Snake.head.speed(0)
        Snake.head.shape('square')
        Snake.head.color('darkgreen')
        Snake.head.penup()
        Snake.head.direction = "stop"
        Snake.head.predirection = 0
        Snake.head.showturtle()
        Snake.snake.append(Snake.head)

    def gensnake(): # генерация тела змеи
        Snake.body.speed(0)
        Snake.body.shape("square")
        Snake.body.color("green")
        Snake.body.penup()
        Snake.bodies.append(Snake.body)
        for bodys in Snake.bodies:
            if len(Snake.snake) == bodys.number:
                bodys.showturtle()
                bodys.goto(Snake.snake[-1].pos()[0], Snake.snake[-1].pos()[1])
                Snake.snake.append(bodys)
                break
        else:
            newbody = Snake.body.clone()
            newbody.number = len(Snake.snake)
            newbody.showturtle()
            Snake.bodies.append(newbody)
            Snake.snake.append(newbody)

class Moving:
    def goup(): # изменение на движение вверх
        if Snake.snake[0].direction != "down" and Snake.snake[0].predirection == 0: # проверка на то, чтобы змея не поворачивалась в саму себя
            Snake.snake[0].direction = "up"
            Snake.snake[0].predirection = 1

    def godown(): # изменение на движение вниз
        if Snake.snake[0] .direction != "up" and Snake.snake[0].predirection == 0: # проверка на то, чтобы змея не поворачивалась в саму себя
            Snake.snake[0].direction = "down"
            Snake.snake[0].predirection = 1

    def goleft(): # изменение на движение влево
        if Snake.snake[0].direction != "right" and Snake.snake[0].predirection == 0: # проверка на то, чтобы змея не поворачивалась в саму себя
            Snake.snake[0].direction = "left"
            Snake.snake[0].predirection = 1

    def goright(): # изменение на движение вправо
        if Snake.snake[0].direction != "left" and Snake.snake[0].predirection == 0: # проверка на то, чтобы змея не поворачивалась в саму себя
            Snake.snake[0].direction = "right"
            Snake.snake[0].predirection = 1

    def move(cell_size): # само движение
        if Snake.snake[0].direction == "up": # проверка на то, чтобы если игрок быстро нажал 2 клавиши, то змейка не повернулось в сторону самой себя
            y = Snake.snake[0].ycor()
            print(Snake.snake[0].ycor(), 4)
            Snake.snake[0].sety(y+cell_size)
            Snake.snake[0].predirection = 0
        if Snake.snake[0].direction == "down":
            y = Snake.snake[0].ycor()
            Snake.snake[0].sety(y-cell_size)
            Snake.snake[0].predirection = 0
        if Snake.snake[0].direction == "left":
            x = Snake.snake[0].xcor()
            Snake.snake[0].setx(x-cell_size)
            Snake.snake[0].predirection = 0
        if Snake.snake[0].direction == "right":
            x = Snake.snake[0].xcor()
            Snake.snake[0].setx(x+cell_size)
            Snake.snake[0].predirection = 0

class Game:
    src = 0
    fieldsize = 0
    cell_size = 0
    delay = 0
    qstruct = 0
    sapple = 0
    appleseaten = 0
    timer = 0

    struct = Turtle()
    struct.name = "struct"
    struct.hideturtle()

    score = Turtle()
    score.name = "score"
    score.hideturtle()

    structs = []

    sc = 0
    hsc = 0


    def game(fieldsize, cell_cize, delay, qstruct, sapple, src): # активация всех стартовых функций
        Game.appleseaten = 0
        Game.sc = 0
        Game.hsc = 0
        Game.src = src
        Game.fieldsize = fieldsize
        Game.cell_size = cell_cize
        Game.delay = delay
        Game.qstruct = qstruct
        Game.sapple = sapple

        Game.structs = Field.genstruct(Game.struct, Game.qstruct, Game.structs,  Snake.snake, Game.fieldsize, Game.cell_size)
        Game.sc, Game.hsc = Field.genscore(Game.score, Game.fieldsize, Game.hsc, Game.sc)
        Apples.genapple()
        Apples.regenapples()
        if Game.sapple:
            Apples.gensuperapple()
        Snake.genhead()
        Game.nextframe()

    def nextframe(): # следующее движение змейки
        Game.check_collision(Game.fieldsize, Game.cell_size)
        Game.consumption()

        for index in range(len(Snake.snake)-1, 1, -1): # перемещение тела змеи
            x = Snake.snake[index-1].xcor()
            y = Snake.snake[index-1].ycor()
            Snake.snake[index].goto(x, y)
        
        if len(Snake.snake) > 1: # 1 кусочка змеи за головой
            x = Snake.snake[0].xcor()
            y = Snake.snake[0].ycor()
            Snake.snake[1].goto(x, y)

        if perf_counter() - Game.timer > Game.delay / 100 * 4 and Apples.superapple.isvisible(): # особое яблоко исчезает через определённое время, если игрок его не съедает
            Apples.superapple.hideturtle()

        Moving.move(Game.cell_size)
        Game.src.update()
        Game.src.ontimer(Game.nextframe, Game.delay) # повторение действия   
    
    def check_collision(fieldsize, cell_size): # проверка на столкновение
        # првоерка на столкновение с границей поля
        if (Snake.snake[0].xcor() == ((fieldsize//cell_size//2-1)*cell_size if fieldsize//cell_size % 2 == 0 else fieldsize//cell_size//2*cell_size) and Snake.snake[0].direction == "right") or (Snake.snake[0].xcor() ==  ((-fieldsize//cell_size//2+2)*cell_size if fieldsize//cell_size % 2 == 0 else (-fieldsize//cell_size//2+1)*cell_size) and Snake.snake[0].direction == "left") or (Snake.snake[0].ycor() == ((fieldsize//cell_size//2-1)*cell_size if fieldsize//cell_size % 2 == 0 else fieldsize//cell_size//2*cell_size) and Snake.snake[0].direction == "up") or (Snake.snake[0].ycor() == ((-fieldsize//cell_size//2+2)*cell_size if fieldsize//cell_size % 2 == 0 else (-fieldsize//cell_size//2+1)*cell_size) and Snake.snake[0].direction == "down"):
            Game.appleseaten = 0
            Game.sc, Game.hsc = Field.genscore(Game.score, Game.fieldsize, 0, Game.hsc)
            Apples.superapple.hideturtle()
            Apples.regenapples()
            sleep(1)
            Snake.snake[0].goto(0, 0)
            Snake.snake[0].direction = "Stop"
            for body in Snake.snake:
                body.hideturtle()
            Snake.snake = []
            Snake.genhead()

        # проверка на столкновение с стеной
        for struct in Game.structs:
            if (Snake.snake[0].xcor() == struct[0] - Game.cell_size and Snake.snake[0].ycor() == struct[1] and Snake.snake[0].direction == "right") or (Snake.snake[0].xcor() == struct[0] + Game.cell_size and Snake.snake[0].ycor() == struct[1] and Snake.snake[0].direction == "left") or (Snake.snake[0].ycor() == struct[1] - Game.cell_size and Snake.snake[0].xcor() == struct[0] and Snake.snake[0].direction == "up") or (Snake.snake[0].ycor() == struct[1] + Game.cell_size and Snake.snake[0].xcor() == struct[0] and Snake.snake[0].direction == "down"):
                Game.appleseaten = 0
                Game.sc, Game.hsc  = Field.genscore(Game.score, Game.fieldsize, 0, Game.hsc)
                Apples.superapple.hideturtle()
                Apples.regenapples()
                sleep(1)
                Snake.snake[0].goto(0, 0)
                Snake.snake[0].direction = "stop"
                for body in Snake.snake:
                    body.hideturtle()
                Snake.snake = []
                Snake.genhead()
        
        # проверка на столкновение с телом змеи
        for body in Snake.snake:
            if (Snake.snake[0].xcor() == body.pos()[0] - Game.cell_size and Snake.snake[0].ycor() == body.pos()[1] and Snake.snake[0].direction == "right") or (Snake.snake[0].xcor() == body.pos()[0] + Game.cell_size and Snake.snake[0].ycor() == body.pos()[1] and Snake.snake[0].direction == "left") or (Snake.snake[0].ycor() == body.pos()[1] - Game.cell_size and Snake.snake[0].xcor() == body.pos()[0] and Snake.snake[0].direction == "up") or (Snake.snake[0].ycor() == body.pos()[1] + Game.cell_size and Snake.snake[0].xcor() == body.pos()[0] and Snake.snake[0].direction == "down"):
                Game.appleseaten = 0
                Game.sc, Game.hsc  = Field.genscore(Game.score, Game.fieldsize, 0, Game.hsc)
                Apples.superapple.hideturtle()
                Apples.regenapples()
                sleep(1)
                Snake.snake[0].goto(0, 0)
                Snake.snake[0].direction = "stop"
                for body1 in Snake.snake:
                    body1.hideturtle()
                Snake.snake = []
                Snake.genhead()

    # поедание яблок
    def consumption():
        if Snake.snake[0].distance(Apples.apple) < Game.cell_size and Apples.apple.isvisible(): # проверка на расстояние между головой змеи и яблоком
            Game.appleseaten += 1
            Game.sc, Game.hsc = Field.genscore(Game.score, Game.fieldsize, Game.sc + 1, Game.hsc)
            Apples.regenapples()
            Snake.gensnake()

        if Game.sapple:
            if Snake.snake[0].distance(Apples.superapple) < Game.cell_size and Apples.superapple.isvisible(): # проверка на расстояние между головой змеи и особым яблоком и условия видимости особого яблока
                Game.appleseaten = 0
                Game.sc, Game.hsc = Field.genscore(Game.score, Game.fieldsize, Game.sc + 3, Game.hsc)
                Apples.superapple.hideturtle()
                Apples.regensuperapples()
                for _ in range(3):
                    Snake.gensnake()

            if Game.appleseaten % 5 == 0 and Game.appleseaten != 0: # условие появления особого яблока
                Game.appleseaten = 0
                Apples.superapple.showturtle()
                Game.timer = perf_counter()