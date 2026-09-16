class NO:
    def __init__(self, valor, nome):
        self.nome = nome
        self.valor = valor  # Valor armazenado dentro do nó
        self.vizinhos = {}  # Dicionário para guardar os vizinhos do nó

    def adicionar_vizinhos(self, nome, peso):
        # Verifica se já não existe esse vizinho
        if nome not in self.vizinhos:
            self.vizinhos[nome] = peso  # Adiciona o peso da ligação


class diagrama:
    def __init__(self):
        # Dicionário para armazenar todos os nós
        self.armazenamento = {}

    def adicionar_No(self, nome, valor):
        # Verifica se o nome ainda não está no dicionário
        if nome not in self.armazenamento:

            # Cria um novo objeto NO e armazena no dicionário
            self.armazenamento[nome] = NO(valor, nome)

    def pegar(self, nome):
        # Verifica se o nome está no dicionário
        if nome in self.armazenamento:

            # Retorna o objeto NO
            return self.armazenamento[nome]

        # Caso não seja encontrado
        return None

    # Adiciona uma aresta entre dois vértices
    def borda(self, vertice1, vertice2, peso):

        # Garante que o primeiro vértice existe
        self.adicionar_No(vertice1, "")

        # Garante que o segundo vértice existe
        self.adicionar_No(vertice2, "")

        # Adiciona o vertice2 como vizinho do vertice1
        self.pegar(vertice1).adicionar_vizinhos(vertice2, peso)

        # Adiciona o vertice1 como vizinho do vertice2
        self.pegar(vertice2).adicionar_vizinhos(vertice1, peso)


def BFS(grafico, iniciar_No, procura_Valor):

    # Fila da BFS
    queie = [iniciar_No]

    # Evita visitar o mesmo nó repetidamente
    verificacao = {iniciar_No}

    # Continua enquanto houver elementos na fila
    while len(queie) != 0:

        # Pega o primeiro elemento da fila
        atual = queie.pop(0)

        # Procura o nó de acordo com o nome
        no = grafico.pegar(atual)

        # Se não existir, pula para o próximo
        if no is None:
            continue

        # Mostra o valor do nó atual
        print(no.valor)
        print()

        # Verifica se encontrou o valor procurado
        if no.valor == procura_Valor:
            return no

        # Percorre todos os vizinhos do nó atual
        for vertice in no.vizinhos:

            # Verifica se esse vizinho ainda não foi visitado
            if vertice not in verificacao:

                # Marca o vizinho como visitado
                verificacao.add(vertice)

                # Coloca o vizinho no final da fila
                queie.append(vertice)

    # Se a busca terminar sem encontrar o valor
    return None
