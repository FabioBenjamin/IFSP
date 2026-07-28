import turtle

leo = turtle.Turtle()
leo.left(90)
leo.speed(100)

def arvore(i):
    if i < 10:
        return
    else:
        leo.forward(i)
        leo.left(45)
        arvore(3*i/4)
        leo.right(90)
        arvore(3*i/4)
        leo.left(45)
        leo.backward(i)


arvore(100)
turtle.done()
