import turtle

ay = turtle.Turtle()
ay.speed(10)
ay.pensize(3)
ay.color("pink")


def Fibonacci(n):
    sequencia = [1,1]

    while len(sequencia) < n:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)

    return sequencia

def quadrado(t, tamanho):
    for i in range(4):
        t.forward(tamanho)
        t.right(90)


def espirral(t, tamanhos):
    for tamanho in tamanhos:
        quadrado(t, tamanho)

        t.circle(tamanho, 90)

numeros = Fibonacci(20)

espirral(ay, numeros)

turtle.done()