# REALIZA UMA PESQUISA PELOS NÓ'S NAS ÁRVORES

class NO:
    def __init__(self, mei, esq, dir):
        self.item = mei
        self.esq = esq
        self.dir = dir

class Arvore:
    def __init__(self):
        self.raiz = NO(None, None, None)
        self.raiz = None # Raiz da arvore igual a null