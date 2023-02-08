from turtle import Screen, Turtle
from Settings import Settings

screen_now = "menu"

class SnakeScreen:
    screen = Screen()
    drawer = Turtle()
    drawer.name = "drawer"
    setsize = Turtle()
    setsize.name = "setsize"
    setsize.hideturtle()
    setspeed = Turtle()
    setspeed.name = "setspeed"
    setspeed.hideturtle()
    setqstruct = Turtle()
    setqstruct.name = "setqstruct"
    setqstruct.hideturtle()
    setsapple = Turtle()
    setsapple.name = "setsapple"
    setsapple.hideturtle()

    fieldx = Settings.fieldsize
    fieldy = Settings.fieldsize

    def __init__(self, width=Settings.screenx, height=Settings.screeny, settingsx=300, settingsy=300):
        self.width = width
        self.height = height
        self.settingsx = settingsx
        self.settingsy = settingsy
        self.screen.bgcolor("lightgreen")
        self.screen.title("Snake Game")
        self.screen.setup(width=self.width, height=self.height)
        self.screen.tracer(0)

    def get_screen(self, fieldsize=Settings.fieldsize, type="menu", cell_size=Settings.cell_size):
        global screen_now

        if type == "menu":
            screen_now = "menu"
            self.drawer.hideturtle()
            self.drawer.fillcolor("green")
            self.drawer.penup()
            self.drawer.goto(0, self.drawer.ycor()+75)
            self.drawer.pendown()
            self.drawer.begin_fill()
            self.drawer.goto(self.drawer.xcor()-100, self.drawer.ycor())
            self.drawer.seth(180)
            self.drawer.circle(30, 180)
            self.drawer.goto(self.drawer.xcor()+200, self.drawer.ycor())
            self.drawer.seth(0)
            self.drawer.circle(30, 180)
            self.drawer.goto(self.drawer.xcor()-100, self.drawer.ycor())
            self.drawer.end_fill()
            self.drawer.penup()
            self.drawer.goto(self.drawer.xcor(), self.drawer.ycor()-50)
            self.drawer.write("Играть", align="center", font=("Arial", 30, "normal"))
            
            self.drawer.fillcolor("gray")
            self.drawer.begin_fill()
            self.drawer.goto(0, self.drawer.ycor()-40)
            self.drawer.pendown()
            self.drawer.setx(self.drawer.xcor()-25)
            self.drawer.seth(180)
            self.drawer.circle(20, 90)
            self.drawer.sety(self.drawer.ycor()-50)
            self.drawer.seth(270)
            self.drawer.circle(20, 90)
            self.drawer.setx(self.drawer.xcor()+50)
            self.drawer.seth(0)
            self.drawer.circle(20, 90)
            self.drawer.sety(self.drawer.ycor()+50)
            self.drawer.seth(90)
            self.drawer.circle(20, 90)
            self.drawer.setx(self.drawer.xcor()-25)
            self.drawer.end_fill()

            self.drawer.penup()
            self.drawer.goto(0, self.drawer.ycor()-30)
            self.drawer.fillcolor("lightgray")
            self.drawer.begin_fill()
            self.drawer.penup()
            self.drawer.sety(self.drawer.ycor()+20)
            self.drawer.begin_fill()
            self.drawer.pendown()
            self.drawer.circle(25, 15)
            self.drawer.sety(self.drawer.ycor()-10)
            self.drawer.circle(25, 15)
            self.drawer.goto(self.drawer.xcor()-5, self.drawer.ycor()+5)
            self.drawer.circle(25, 30)
            self.drawer.goto(self.drawer.xcor()+5, self.drawer.ycor()-5)
            self.drawer.circle(25, 15)
            self.drawer.setx(self.drawer.xcor()-10)
            self.drawer.circle(25, 30)
            self.drawer.setx(self.drawer.xcor()+10)
            self.drawer.circle(25, 15)
            self.drawer.goto(self.drawer.xcor()-5, self.drawer.ycor()-5)
            self.drawer.circle(25, 30)
            self.drawer.goto(self.drawer.xcor()+5, self.drawer.ycor()+5)
            self.drawer.circle(25, 15)
            self.drawer.sety(self.drawer.ycor()-10)
            self.drawer.circle(25, 30)
            self.drawer.sety(self.drawer.ycor()+10)
            self.drawer.circle(25, 15)
            self.drawer.goto(self.drawer.xcor()+5, self.drawer.ycor()-5)
            self.drawer.circle(25, 30)
            self.drawer.goto(self.drawer.xcor()-5, self.drawer.ycor()+5)
            self.drawer.circle(25, 15)
            self.drawer.setx(self.drawer.xcor()+10)
            self.drawer.circle(25, 30)
            self.drawer.setx(self.drawer.xcor()-10)
            self.drawer.circle(25, 15)
            self.drawer.goto(self.drawer.xcor()+5, self.drawer.ycor()+5)
            self.drawer.circle(25, 30)
            self.drawer.goto(self.drawer.xcor()-5, self.drawer.ycor()-5)
            self.drawer.circle(25, 15)
            self.drawer.sety(self.drawer.ycor()+10)
            self.drawer.circle(25, 15)
            self.drawer.end_fill()

            self.drawer.penup()
            self.drawer.goto(0, self.drawer.ycor()-20)
            self.drawer.pendown()
            self.drawer.fillcolor("gray")
            self.drawer.begin_fill()
            self.drawer.circle(15)
            self.drawer.end_fill()

            self.drawer.penup()
            self.drawer.goto(0, self.drawer.ycor()-200)
            self.drawer.pendown()
            self.drawer.fillcolor("red")
            self.drawer.begin_fill()
            self.drawer.goto(self.drawer.xcor()-75, self.drawer.ycor())
            self.drawer.seth(180)
            self.drawer.circle(20, 180)
            self.drawer.goto(self.drawer.xcor()+150, self.drawer.ycor())
            self.drawer.seth(0)
            self.drawer.circle(20, 180)
            self.drawer.goto(self.drawer.xcor()-75, self.drawer.ycor())
            self.drawer.end_fill()
            self.drawer.penup()
            self.drawer.goto(self.drawer.xcor(), self.drawer.ycor()-40)
            self.drawer.write("Выйти", align="center", font=("Arial", 23, "normal"))

        if type == "game":
            screen_now = "game"
            self.cell_size = 21
            self.drawer.hideturtle()
            self.drawer.fillcolor("gray")
            self.drawer.begin_fill()
            self.drawer.penup()
            self.drawer.sety(fieldsize//2+50)
            self.drawer.pendown()
            self.drawer.setx(-fieldsize//2-20)
            self.drawer.seth(180)
            self.drawer.circle(30, 90)
            self.drawer.sety(-fieldsize//2-20)
            self.drawer.circle(30, 90)
            self.drawer.setx(fieldsize//2+25)
            self.drawer.circle(30, 90)
            self.drawer.sety(fieldsize//2+20)
            self.drawer.circle(30, 90)
            self.drawer.setx(0)
            self.drawer.end_fill()
            self.drawer.penup()
            self.drawer.goto(-fieldsize//2+5, fieldsize//2+15)
            self.drawer.pendown()
            self.drawer.seth(90)
            self.drawer.fillcolor("lightgray")
            self.drawer.begin_fill()
            self.drawer.circle(25)
            self.drawer.end_fill()
            self.drawer.penup()
            self.drawer.goto(-fieldsize//2-5, fieldsize//2+20)
            self.drawer.fillcolor("gray")
            self.drawer.begin_fill()
            self.drawer.pendown()
            self.drawer.setx(-fieldsize//2-25)
            self.drawer.sety(fieldsize//2+30)
            self.drawer.goto(-fieldsize//2-35, fieldsize//2+15)
            self.drawer.goto(-fieldsize//2-25, fieldsize//2)
            self.drawer.sety(fieldsize//2+10)
            self.drawer.setx(-fieldsize//2-5)
            self.drawer.sety(fieldsize//2+20)
            self.drawer.end_fill()
            self.drawer.penup()
            self.drawer.goto(round((fieldsize//cell_size//2-1)*cell_size+cell_size/2) if fieldsize//cell_size % 2 == 0 else round(fieldsize//cell_size//2*cell_size+cell_size/2), -round((fieldsize//cell_size//2-1)*cell_size+cell_size/2) if fieldsize//cell_size % 2== 0 else -round(fieldsize//cell_size//2*cell_size+cell_size/2))
            self.drawer.pendown()
            self.drawer.fillcolor("lightgreen")
            self.drawer.begin_fill()
            self.drawer.goto(round((fieldsize//cell_size//2-1)*cell_size+cell_size/2) if fieldsize//cell_size % 2 == 0 else round(fieldsize//cell_size//2*cell_size+cell_size/2), round((fieldsize//cell_size//2-1)*cell_size+cell_size/2) if fieldsize//cell_size % 2== 0 else round(fieldsize//cell_size//2*cell_size+cell_size/2))
            self.drawer.goto(-round((fieldsize//cell_size//2-1)*cell_size+cell_size/2) if fieldsize//cell_size % 2== 0 else -round(fieldsize//cell_size//2*cell_size+cell_size/2), round((fieldsize//cell_size//2-1)*cell_size+cell_size/2) if fieldsize//cell_size % 2== 0 else round(fieldsize//cell_size//2*cell_size+cell_size/2))
            self.drawer.goto(-round((fieldsize//cell_size//2-1)*cell_size+cell_size/2) if fieldsize//cell_size % 2== 0 else -round(fieldsize//cell_size//2*cell_size+cell_size/2), -round((fieldsize//cell_size//2-1)*cell_size+cell_size/2) if fieldsize//cell_size % 2== 0 else -round(fieldsize//cell_size//2*cell_size+cell_size/2))
            self.drawer.goto(round((fieldsize//cell_size//2-1)*cell_size+cell_size/2) if fieldsize//cell_size % 2== 0 else round(fieldsize//cell_size//2*cell_size+cell_size/2), -round((fieldsize//cell_size//2-1)*cell_size+cell_size/2) if fieldsize//cell_size % 2== 0 else -round(fieldsize//cell_size//2*cell_size+cell_size/2))
            self.drawer.end_fill()
        
        if type == "settings":
            screen_now = "settings"
            self.drawer.hideturtle()
            self.drawer.fillcolor("gray")
            self.drawer.begin_fill()
            self.drawer.penup()
            self.drawer.sety(self.settingsx//2+50)
            self.drawer.pendown()
            self.drawer.setx(-self.settingsx//2-20)
            self.drawer.seth(180)
            self.drawer.circle(30, 90)
            self.drawer.sety(-self.settingsy//2-20)
            self.drawer.circle(30, 90)
            self.drawer.setx(self.settingsx//2+25)
            self.drawer.circle(30, 90)
            self.drawer.sety(self.settingsy//2+20)
            self.drawer.circle(30, 90)
            self.drawer.setx(0)
            self.drawer.end_fill()
            self.drawer.penup()
            self.drawer.goto(-self.settingsx//2+5, self.settingsy//2+15)
            self.drawer.pendown()
            self.drawer.seth(90)
            self.drawer.fillcolor("lightgray")
            self.drawer.begin_fill()
            self.drawer.circle(25)
            self.drawer.end_fill()
            self.drawer.penup()
            self.drawer.goto(-self.settingsx//2-5, self.settingsy//2+20)
            self.drawer.fillcolor("gray")
            self.drawer.begin_fill()
            self.drawer.pendown()
            self.drawer.setx(-self.settingsx//2-25)
            self.drawer.sety(self.settingsy//2+30)
            self.drawer.goto(-self.settingsx//2-35, self.settingsy//2+15)
            self.drawer.goto(-self.settingsx//2-25, self.settingsy//2)
            self.drawer.sety(self.settingsy//2+10)
            self.drawer.setx(-self.settingsx//2-5)
            self.drawer.sety(self.settingsy//2+20)
            self.drawer.end_fill()
            self.drawer.penup()
            self.drawer.fillcolor("lightgray")
            self.drawer.goto(0, 100)
            self.drawer.pendown()
            self.drawer.begin_fill()
            self.drawer.setx(self.drawer.xcor()-150)
            self.drawer.seth(180)
            self.drawer.circle(20, 180)
            self.drawer.setx(self.drawer.xcor()+300)
            self.drawer.seth(0)
            self.drawer.circle(20, 180)
            self.drawer.setx(self.drawer.xcor()-150)
            self.drawer.end_fill()
            self.drawer.penup()
            self.drawer.goto(0, 50)
            self.drawer.pendown()
            self.drawer.begin_fill()
            self.drawer.setx(self.drawer.xcor()-150)
            self.drawer.seth(180)
            self.drawer.circle(20, 180)
            self.drawer.setx(self.drawer.xcor()+300)
            self.drawer.seth(0)
            self.drawer.circle(20, 180)
            self.drawer.setx(self.drawer.xcor()-150)
            self.drawer.end_fill()
            self.drawer.penup()
            self.drawer.goto(0, 0)
            self.drawer.pendown()
            self.drawer.begin_fill()
            self.drawer.setx(self.drawer.xcor()-150)
            self.drawer.seth(180)
            self.drawer.circle(20, 180)
            self.drawer.setx(self.drawer.xcor()+300)
            self.drawer.seth(0)
            self.drawer.circle(20, 180)
            self.drawer.setx(self.drawer.xcor()-150)
            self.drawer.end_fill()
            self.drawer.penup()
            self.drawer.goto(0, -50)
            self.drawer.pendown()
            self.drawer.begin_fill()
            self.drawer.setx(self.drawer.xcor()-150)
            self.drawer.seth(180)
            self.drawer.circle(20, 180)
            self.drawer.setx(self.drawer.xcor()+300)
            self.drawer.seth(0)
            self.drawer.circle(20, 180)
            self.drawer.setx(self.drawer.xcor()-150)
            self.drawer.end_fill()
            self.setsize.goto(0, 62.5)
            self.setsize.write(f"Размер поля : {'малый' if Settings.fieldsize == 400 else 'средний' if Settings.fieldsize == 500 else 'большой' if Settings.fieldsize == 600 else 'огромный'}", align="center", font=("Arial", 20, "normal"))
            self.setspeed.goto(0, 12.5)
            self.setspeed.write(f"Скорость змеи : {'малая' if Settings.delay == 140 else 'обычная' if Settings.delay == 130 else 'средняя' if Settings.delay == 120 else 'большая' if Settings.delay == 110 else 'огромная'}", align="center", font=("Arial", 20, "normal"))
            self.setqstruct.goto(0, -37.5)
            self.setqstruct.write(f"Кол-во стен : {'нет' if Settings.qstruct == 0 else 'малое' if Settings.qstruct == 10 else 'обычное' if Settings.qstruct == 20 else 'среднее' if Settings.qstruct == 30 else 'большое' if Settings.qstruct == 40 else 'огромное'}", align="center", font=("Arial", 20, "normal"))
            self.setsapple.goto(0, -87.5)
            self.setsapple.write(f"Cуперяблоко : {'есть' if Settings.superapple else 'нет'}", align="center", font=("Arial", 20, "normal"))