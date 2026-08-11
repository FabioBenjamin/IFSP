import turtle
from email.policy import default

ay = turtle.Turtle()
ay.speed(10)
ay.pensize(3)

# Tamanho da tela
tela = turtle.Screen()
largura = tela.window_width()
altura = tela.window_height()

# Limite da tela
limite = min(largura, altura) * 0.4

def Fibonacci(n):
    sequencia = [1,1]

    while len(sequencia) < n:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)

    return sequencia

# Descobrir limite
n = 1
while True:

    Numero = Fibonacci(n)

    if max(Numero) > limite:
        break

    n+=1
maximo = n-1

# Pergunta Usuário
perguntaTamanho = tela.numinput(
    "MACACOS VOADORES",
    f"Digite o tamanho (máximo {maximo}):",
    default=min(20, maximo),
    minval=2,
    maxval=maximo
)

# Cor da tela
cor = tela.colormode(255)

peguntaCor = tela.textinput(
    "ESCOLHA MACACO",
    f"Escolha um numero para iniciar (máximo {cor})",
    default = min(20, cor)
)

def quadrado(t, tamanho):
    for i in range(4):
        t.forward(tamanho)
        t.left(90)


def espirral(t, tamanhos):
    for tamanho in tamanhos:
        quadrado(t, tamanho)

        t.circle(tamanho, 90)

numeros = Fibonacci(20)

escala = limite / max(numeros)

# Redimensiona todos os números
numeros = [n * escala for n in numeros]

espirral(ay, numeros)

turtle.done()
