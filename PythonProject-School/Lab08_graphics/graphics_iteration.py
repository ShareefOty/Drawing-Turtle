import turtle
t = turtle.Turtle()
t.speed(11)


def basic_flower():
    '''
    draw a 4 petal flower with fixed size and color
    '''

    # set up color
    t.color('black','plum')
    t.begin_fill()
    
    # after each petal, turn 90 degrees to offset next petal
    # Turn 90 because it is 4 petals. 360/4 = 90
    t.circle(50)
    t.right(90) 
    t.circle(50)
    t.right(90)
    t.circle(50)
    t.right(90)
    t.circle(50)
    t.right(90)

    # Think of this as a closing statement to begin_fill
    # Anything drawn between begin_ and end_fill will be filled
    # with the color set in t.color(pen,fill)
    t.end_fill()
    
    
def flower():
    '''
    draw a flower based on function parameters that make use of iteration
    '''
    
    pass

def sun():
    # from https://docs.python.org/3/library/turtle.html
    # move without drawing
    t.penup()
    t.goto(150,150)
    t.pendown()
    
    # set color of pen and fill 
    t.color('red', 'yellow')
    t.begin_fill()

    # draw the star with 18 points (2 iterations per point)
    for i in range(36):
        t.forward(200)
        t.left(170)     # 36 iterations; 360/36 = 10; 180-10
    t.end_fill()


if __name__ == '__main__':
    basic_flower()
    sun()

