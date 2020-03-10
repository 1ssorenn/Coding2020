'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!

'''
import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(0)

my_screen = turtle.Screen()
my_screen.bgcolor("White")


my_screen.clear()
my_turtle.home()

def recur_h(x, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.forward(x // 2)
        my_turtle.right(90)
        my_turtle.forward(x // 2)
        pos_1 = my_turtle.pos()
        my_turtle.down()
        my_turtle.right(180)
        my_turtle.forward(x)
        my_turtle.up()
        pos_2 = my_turtle.pos()
        my_turtle.right(180)
        my_turtle.forward(x // 2)
        my_turtle.right(90)
        my_turtle.down()
        my_turtle.forward(x)
        my_turtle.up()
        my_turtle.right(90)
        my_turtle.forward(x // 2)
        pos_3 = my_turtle.pos()
        my_turtle.right(180)
        my_turtle.down()
        my_turtle.forward(x)
        my_turtle.up()
        my_turtle.right(90)
        recur_h(x // 2, depth // 2)
        my_turtle.goto(pos_1)
        recur_h(x // 2, depth // 2)
        my_turtle.goto(pos_2)
        recur_h(x // 2, depth // 2)
        my_turtle.goto(pos_3)
        recur_h(x // 2, depth // 2)


recur_h(250, 10)


my_screen.clear()
my_turtle.home()
#  Recur_sq won't run correctly after recur_h, told to turn it in like this
def recur_sq(x, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.forward(x // 2)
        my_turtle.right(90)
        my_turtle.forward(x // 2)
        pos_1 = my_turtle.pos()
        my_turtle.down()
        my_turtle.right(90)
        my_turtle.forward(x)
        my_turtle.right(90)
        my_turtle.forward(x)
        pos_2 = my_turtle.pos()
        my_turtle.right(90)
        my_turtle.forward(x)
        pos_3 = my_turtle.pos()
        my_turtle.right(90)
        my_turtle.forward(x)
        pos_4 = my_turtle.pos()
        my_turtle.right(90)
        my_turtle.forward(x)
        my_turtle.up()
        recur_sq(x // 2, depth // 2)
        my_turtle.goto(pos_1)
        recur_sq(x // 2, depth // 2)
        my_turtle.goto(pos_2)
        recur_sq(x // 2, depth // 2)
        my_turtle.goto(pos_3)
        recur_sq(x // 2, depth // 2)





recur_sq(250, 10)

my_screen.clear()
my_turtle.home()

my_turtle.forward(45)

def own_draw(x, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(0, 0)
        my_turtle.down()
        pos = my_turtle.pos()
        my_turtle.forward(x)
        pos_1 = my_turtle.pos()
        my_turtle.right(135)
        my_turtle.forward(x)
        pos_2 = my_turtle.pos()
        my_turtle.right(90)
        my_turtle.goto(pos)
        own_draw(x, depth - 1)
        own_draw(x * 2, depth - 1)






own_draw(150, 10)
my_screen.exitonclick()


