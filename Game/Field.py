from Game.Operations import Operations

class Field:
    def genstruct(struct, qstruct, structs, snake, fieldsize, cell_size): # генерация стен
        structs = []
        for _ in range(qstruct):
            xy = Operations.checkcoord(structs, snake, fieldsize, cell_size)
            x = xy[0]
            y = xy[1]
            struct.speed(0)
            struct.shape('square')
            struct.color('black')
            struct.penup()
            struct.hideturtle()
            struct.goto(x, y)
            structs.append((struct.xcor(), struct.ycor()))
            struct.pendown()
            struct.fillcolor("black")
            struct.begin_fill()
            struct.goto(struct.xcor()+cell_size//2, struct.ycor()+cell_size//2)
            struct.setx(struct.xcor()-(cell_size-1))
            struct.sety(struct.ycor()-(cell_size-1))
            struct.setx(struct.xcor()+(cell_size-1))
            struct.sety(struct.ycor()+(cell_size-1))
            struct.end_fill()
        return structs

    def genscore(score, fieldy, sc, hsc):
        score.penup()
        score.sety(fieldy//2)
        score.pendown()
        if sc > hsc:
            hsc = sc
        score.clear()
        score.write(f"Счёт : {sc}     Рекорд : {hsc}", align="center", font=("Arial", 25, "normal"))
        return sc, hsc
