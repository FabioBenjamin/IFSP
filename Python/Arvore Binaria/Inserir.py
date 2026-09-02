# TREINAMENTO ARVORE DE BUSCA BINARIA
# Repositorio utilizado: https://gist.github.com/divanibarbosa/a8662693e44ab9ee0d0e8c2d74808929

# Direções da arvore (esquerda, meio, direita)
# Esquerda = menor valor
# Direita = maior valor
# Meio = Valor atual

# MEIO --> Referencia para comparar e decidir a direção que será orientada

class NO: 
    def __init__(self, mei, esq, dir):
        self.item = mei
        self.esq = esq
        self.dir = dir

class Arvore:
    def __init__(self):
        self.root = NO(None, None, None)
        self.root = None

    def inserir(self, valor):
        novo = NO(valor, None, None) # Cria um novo nó
        if self.root == None:
            self.root = novo
        else: # Caso não seja a raiz que está procurando
            atual = self.root

            # Descobrir o direcionamento partindo da raiz
            while True:
                anterior = atual

                if valor <= atual.item: # Direcionar para a esquerda
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        return
                # Fim da busca a esquerda 
                
                else: # Direcionar para a direita
                    atual = atual.dir
                    if atual == None: 
                        anterior.dir = novo
                        return
                # Fim da busca a direita