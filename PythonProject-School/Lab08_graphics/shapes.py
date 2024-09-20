import turtle

def draw_circle(position, radius, color):
    '''
    Draw a circle at location position, which is a list [x,y].
    Draw with given radius and color.
    Color is a list of 2 strings, e.g. ['black','plum'], the
    first color is the PEN the second color is the FILL
    '''
    # move turtle to x y without drawing
    turtle.penup()
    turtle.goto(position[0], position[1])
    turtle.pendown()

    # ready the colors for outline and fill
    turtle.pencolor(color[0])
    turtle.fillcolor(color[1])

    # draw the circle
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(position,h,w, color):
    '''
    Draw a rectangle at location (x,y) -- this is the lower left corner.
    rectangle has height h and width w
    color is a LIST of 2 strings: the first is pen color, and
    the second is fill color.
    '''
    # move the turtle to (x,y) -- without drawing
    turtle.penup()
    turtle.goto(position[0], position[1])
    turtle.pendown()

    # ready the colors for outline and fill
    turtle.pencolor(color[0])
    turtle.fillcolor(color[1])

    # draw the rectangle
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(w)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(90)
    turtle.end_fill()

def draw_triangle(position,h,w, color):
    '''
    Draw a triangle at location (x,y) -- this is the lower left corner.
    The triangle has height h and width w
    color is a LIST of 2 strings: the first is pen color, and
    the second is fill color.

    This assumes an equilateral triangle. The three points of the triangle
    are (x,y), (x+w,y), and (x+w//2,y+h).
    '''
    # move the turtle to (x,y) without drawing
    turtle.penup()
    turtle.goto(position[0], position[1])
    turtle.pendown()

    # ready the colors for outline and fill
    turtle.pencolor(color[0])
    turtle.fillcolor(color[1])

    # draw the triangle
    turtle.begin_fill()
    turtle.goto(position[0]+w, position[1])
    turtle.goto(position[0]+w//2, position[1]+h)
    turtle.goto(position[0], position[1])
    turtle.end_fill()

# Initialize the turtle screen
screen = turtle.Screen()

# Create a turtle object with code
my_turtle = turtle.Turtle()

#_______________________________________________________________________
#####################    TEST YOUR CODE   ##############################


# create a turtle that is in the global scope of this file
# this will open a graphics window
t = turtle.Turtle()

'''
code in the if-statement will be executed only when you run
this module, not when you import it.
'''
if __name__== '__main__':
    draw_circle([35,70],65,['red','blue'])
    draw_rectangle([-75,-150],50,150,['blue','blue'])
    draw_rectangle([-45,-95],50,150,['red','green'])
    draw_triangle([-20,-90],150,100,['yellow','red'])
    draw_triangle([260,40],150,100,['blue','yellow'])
