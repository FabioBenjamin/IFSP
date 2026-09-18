# Exercicio do Beecrowd - BEE 1195

class NO:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

def inserir(raiz, valor):

    if raiz is None:
        return NO(valor)

    if valor < raiz.valor:
        raiz.esq = inserir(raiz.esq, valor)
    else:
        raiz.dir = inserir(raiz.dir, valor)

    return raiz

def pre(raiz, resul):
    if raiz is not None:
        resul.append(raiz.valor)
        pre(raiz.esq, resul)
        pre(raiz.dir, resul)

def inf(raiz, resul):       
    if raiz is not None:
        inf(raiz.esq, resul)
        resul.append(raiz.valor)
        inf(raiz.dir, resul)

def pos(raiz, resul):       
    if raiz is not None:
        pos(raiz.esq, resul)
        pos(raiz.dir, resul)
        resul.append(raiz.valor)


# Calculo
C = int(input())

for caso in range(1, C + 1):
    N = int(input())
    valores = list(map(int, input().split()))

    raiz = None 

    for valor in valores:
        raiz = inserir(raiz, valor)

    pr = []
    i = []
    po = []

    pre(raiz, pr)
    inf(raiz, i)
    pos(raiz, po)

    print(f"Case {caso}:")
    print("Pre.:", *pr)
    print("In..:", *i)
    print("Post:", *po)
