import turtle
w = int(input('Enter the width of rectangle'))
h = int(input('Enter the height of rectangle'))
for variable in range(0, 2):
    turtle.forward(h)
    turtle.right(90)
    turtle.forward(w)
    turtle.right(90)
