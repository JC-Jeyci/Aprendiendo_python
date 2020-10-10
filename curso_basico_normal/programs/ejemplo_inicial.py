import turtle
# La libreria de turtle sirve para crear programas graficos en python

window = turtle.Screen()
test = turtle.Turtle()
test.forward(100)
test.left(90)
test.forward(100)
test.left(90)
test.forward(100)
test.left(90)
test.forward(100)
test.left(90)

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

for i in range(360):
    test.pencolor(colors[i%6])
    test.forward(100)
    test.left(59)
    test.forward(100)
    test.left(59)
    test.forward(100)
    test.left(59)
    test.forward(100)
    test.left(59)


turtle.mainloop()
