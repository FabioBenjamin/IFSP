import turtle
import math

ay = turtle.Turtle()
ay.speed(10)
ay.pensize(3)

# Tamanho da tela
tela = turtle.Screen()
larguraMax = tela.window_width()
alturaMax = tela.window_height()

# Lista das cores PT-BR
cores = {
    "vermelho": "red",
    "azul": "blue",
    "verde": "green",
    "roxo": "purple",
    "amarelo": "yellow",
    "rosa": "pink"
}

# Limite da tela
limite = min(larguraMax, alturaMax) * 0.4

def Fibonacci(n):
    sequencia = [1, 1]

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

    n += 1
maximo = n - 1

# Pergunta Usuário
perguntaTamanho = tela.numinput(
    "Espirais doidas",
    f"Digite o tamanho (máximo {maximo}):",
    default = min(20, maximo),
    minval = 2,
    maxval = maximo
)

# Pergunta da Escolha da Cor
cor = tela.textinput(
    "Escolha da cor",
    "Digite uma cor (ex: Vermelho, Azul, Verde, Roxo):"
)

if cor and cor.lower() in cores:
    corIngles = cores[cor.lower()]
    ay.color(corIngles)

else:
    print("Cor não encontrada ou inválida.")
    ay.color("black") # Deixa padrão caso o usuário digite errado

# Pergunta da Direção
direcao = tela.numinput(
    "Escolha da direção",
    "Digite a direção (ex: 90, 180):",
    default = 0,
    minval = 0,
    maxval = 270
)

ay.setheading(direcao)

def quadrado(t, tamanho):
    for i in range(4):
        t.forward(tamanho)
        t.left(90)

# Simulador para descobrir o tamanho real do desenho
class Simulador:

    def __init__(self, x = 0, y = 0, heading = 0):
        self.x = x
        self.y = y
        self.heading = heading

        self.minX = x, 
        self.maxX = x
        self.minY = y, 
        self.maxY = y

    def atualizarLimites(self):
        self.minX = min(self.minX, self.x), 
        self.maxX = max(self.maxX, self.x)
        self.minY = min(self.minY, self.y), 
        self.maxY = max(self.maxY, self.y)

    def forward(self, tamanho):
        self.x += tamanho * math.cos(math.radians(self.heading))
        self.y += tamanho * math.sin(math.radians(self.heading))
        self.atualizarLimites()

    def left(self, graus):
        self.heading = (self.heading + graus) % 360

    def circle(self, raio, graus = 90, passos = 36):
        anguloPasso = graus / passos
        cordaPasso = 2 * raio * math.sin(math.radians(anguloPasso / 2))

        for i in range(passos):
            self.left(anguloPasso / 2)
            self.forward(cordaPasso)
            self.left(anguloPasso / 2)

def calcularLimites(tamanhos, zoomValor, direcaoValor):
    sim = Simulador(0, 0, direcaoValor)

    for tamanho in tamanhos:
        tamanhoZoom = tamanho * zoomValor

        quadrado(sim, tamanhoZoom)
        sim.circle(tamanhoZoom, 90)

    return sim.minX, sim.minY, sim.maxX, sim.maxY

def calcularTamanhoTela(tamanhos, zoomValor, direcaoValor):
    minX, minY, maxX, maxY = calcularLimites(tamanhos, zoomValor, direcaoValor)

    # Não deixar chegar na borda
    margem = 100

    # Tamanho real necessário
    tamanhoLargura = int((maxX - minX) + margem * 2)
    tamanhoAltura = int((maxY - minY) + margem * 2)

    # Limita ao tamanho da tela cheia
    larguraNova = min(tamanhoLargura, larguraMax)
    alturaNova = min(tamanhoAltura, alturaMax)

    # Tamanho mínimo
    larguraNova = max(larguraNova, 400)
    alturaNova = max(alturaNova, 400)

    return larguraNova, alturaNova

# Tamanho da janela
largura = 400
altura = 400

tela.setup(largura, altura)

# Zoom inicial
zoom = 1.0
zoomMin = 0.1

def espirral(t, tamanhos):
    for tamanho in tamanhos:
        tamanhoZoom = tamanho * zoom

        quadrado(t, tamanhoZoom)
        t.circle(tamanhoZoom, 90)

def espirralNova():
    global largura, altura

    # Descobre o tamanho necessário
    largura, altura = calcularTamanhoTela(numeros, zoom, direcao)

    # Redimensiona a tela antes de desenhar
    tela.setup(width = largura, height = altura)

    # Apaga o desenho anterior
    tela.tracer(0)
    ay.clear()

    # Refazer no centro
    ay.penup()
    ay.goto(0, 0)

    # Voltar na direção escolhida
    ay.setheading(direcao)
    ay.pendown()

    # Desenho novo
    espirral(ay, numeros)

    tela.update()
    tela.tracer(1)

# Configuração do mouse
root = tela.getcanvas().winfo_toplevel()
_afterId = None

def mouse(event):
    global zoom, _afterId

    # Cria o novo zoom
    novoZoom = zoom

    # Aproximação
    if event.delta > 0:
        novoZoom *= 1.2

    # Afastar
    else:
        novoZoom *= 0.9

    # Impede ficar muito pequeno
    if novoZoom < zoomMin:
        novoZoom = zoomMin

    # Limite máximo
    zoomMaxLargura = larguraMax / (max(numeros) * 2)
    zoomMaxAltura = alturaMax / (max(numeros) * 2)
    zoomMax = min(zoomMaxLargura, zoomMaxAltura)

    # Impede passar do limite
    if novoZoom > zoomMax:
        novoZoom = zoomMax

    # Aplicação do zoom
    zoom = novoZoom

    # Cancela o desenho anterior
    if _afterId is not None:
        root.after_cancel(_afterId)

    # Refaz a espiral depois de terminar o scroll
    _afterId = root.after(60, espirralNova)

# Configuração do mouse para cada sistema operacional
canvas = tela.getcanvas()

# Windows
canvas.bind("<MouseWheel>", mouse)

# Linux
canvas.bind("<Button-4>", mouse)
canvas.bind("<Button-5>", mouse)

numeros = Fibonacci(int(perguntaTamanho))

escala = limite / max(numeros)

# Redimensiona todos os números
numeros = [n * escala for n in numeros]

# Descobre o tamanho necessário
largura, altura = calcularTamanhoTela(numeros, zoom, direcao)

tela.setup(width = largura, height = altura)
espirral(ay, numeros)
turtle.done()