from random import randint

class Operations:
    def coord(fieldsize): # генерация случайного числа
        return randint(-(fieldsize//2), fieldsize//2)

    def round_coord(coord, cell_size): # округление числа до делимости на ширину змеи
        if coord < 0:
            coord1 = -coord % cell_size
            coord = coord + coord1
            return coord
        else:
            coord1 = coord % cell_size
            coord = coord - coord1
            return coord
    
    def checkcoord(structs, snake, fieldsize, cell_size): # проверка не совпадают ли сгенерированные координаты с координатами уже существующих объектов
        x = 0
        y = 0
        pos = []
        for struct in structs:
            pos.append((struct[0], struct[1]))
        for body in snake:
            pos.append((body.pos()[0], body.pos()[1]))
        while (x >= -cell_size * 2 and x <= cell_size * 2 and y >= -cell_size * 2 and y <= cell_size * 2) or ((x, y) in pos):
            x = Operations.round_coord(Operations.coord(fieldsize), cell_size)
            y = Operations.round_coord(Operations.coord(fieldsize), cell_size)
        return x, y