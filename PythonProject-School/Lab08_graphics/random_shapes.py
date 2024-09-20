import shapes
import random


def user_circle():
    '''
    Get input from the user to draw a circle to their specifications
    '''
    position = int(input("Enter the x position: "))
    position2 = int(input("Enter the y position: "))
    radius = int(input("Enter the radius: "))
    fill_color = input('Choose a color: ')
    pen_color = input('Choose a pen color: ')
    shapes.draw_circle([position, position2], radius, [fill_color,pen_color])

def random_rectangles():
    '''
    Draw a random number of random rectangles.
    The position and size is random.
    '''
    num_rectangles = random.randint(1, 10)
    for i in range(num_rectangles):
        position = [random.randint(-250, 250), random.randint(-250, 250)]
        h = random.randint(20, 80)
        w = random.randint(20, 80)
        color = ['red', 'blue']
        shapes.draw_rectangle(position, h, w, [color[0],color[1]])


#_______________________________________________________________________
#####################    TEST YOUR CODE   ##############################
if __name__ == '__main__':
    user_circle()
    random_rectangles()

