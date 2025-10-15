import turtle


def square(side_len, coordinate_start, color_pen, color_fill, pensize):
    turtle.up()
    turtle.goto(coordinate_start[0], coordinate_start[1])
    turtle.pencolor(color_pen)
    turtle.fillcolor(color_fill)
    turtle.pensize(pensize)
    turtle.left(90)
    turtle.down()

    turtle.begin_fill()
    
    for _ in range(4):
        turtle.forward(side_len)
        turtle.right(90)

    turtle.end_fill()


def circle(side_len, coordinate_start, color_pen, color_fill, pensize):
    turtle.up()
    turtle.goto(coordinate_start[0], coordinate_start[1])
    turtle.pencolor(color_pen)
    turtle.fillcolor(color_fill)
    turtle.pensize(pensize)
    turtle.down()

    turtle.begin_fill()
    
    turtle.circle(side_len)

    turtle.end_fill()


def hoop(side_len, coordinate_start, color_pen, color_fill, pensize):
    turtle.up()
    turtle.goto(coordinate_start[0], coordinate_start[1])
    turtle.pencolor(color_pen)
    turtle.fillcolor(color_fill)
    turtle.pensize(pensize)
    turtle.down()

    turtle.begin_fill()
    
    turtle.circle(side_len)

    turtle.up()
    turtle.goto(coordinate_start[0] *0.75, coordinate_start[1])
    turtle.pencolor(color_pen)
    turtle.fillcolor(color_fill)
    turtle.pensize(pensize)
    turtle.down()

    turtle.circle(side_len//2)
    
    turtle.end_fill()


def ornament():
    color_dict = {'medium_blue' : '#0000CD', 'sea_green' : '#2E8B57', 
                  'dark_red' : '#8B0000', 'white' : '#FFFFFF'}

    turtle.tracer(False)
    square(200, (0, 0), color_dict['sea_green'], color_dict['sea_green'], 1)
    hoop(100, (200, 100), color_dict['white'], color_dict['dark_red'], 2)
    circle(50, (150, 100), color_dict['white'], color_dict['medium_blue'], 2)
    
    turtle.done()


ornament()