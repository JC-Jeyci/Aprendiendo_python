import turtle
# La libreria de turtle sirve para crear programas graficos en python

def make_line_and_turn(test, largo):
    test.forward(largo)
    test.left(90)


def make_square(test):
    largo = int(input())
    make_line_and_turn(test, largo)


def main():
    window = turtle.Screen()
    test = turtle.Turtle()

    make_square(test)
    turtle.mainloop()
 


if __name__ == '__main__':
    main()