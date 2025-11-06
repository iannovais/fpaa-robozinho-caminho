import heapq

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(labirinto, inicio, fim):
    linhas, colunas = len(labirinto), len(labirinto[0])
    fila = []
    heapq.heappush(fila, (0, inicio))
    veio_de = {inicio: None}
    g_custo = {inicio: 0}
    movimentos = [(0,1),(1,0),(-1,0),(0,-1)]

    while fila:
        _, atual = heapq.heappop(fila)
        if atual == fim:
            caminho = []
            while atual is not None:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.reverse()
            return caminho

        for mov in movimentos:
            vizinho = (atual[0] + mov[0], atual[1] + mov[1])
            if 0 <= vizinho[0] < linhas and 0 <= vizinho[1] < colunas:
                if labirinto[vizinho[0]][vizinho[1]] != "1":
                    novo_custo = g_custo[atual] + 1
                    if vizinho not in g_custo or novo_custo < g_custo[vizinho]:
                        g_custo[vizinho] = novo_custo
                        prioridade = novo_custo + heuristica(vizinho, fim)
                        heapq.heappush(fila, (prioridade, vizinho))
                        veio_de[vizinho] = atual
    return None


def encontrar_pontos(labirinto):
    inicios = []
    fins = []
    for i, linha in enumerate(labirinto):
        for j, valor in enumerate(linha):
            if valor == "S":
                inicios.append((i, j))
            elif valor == "E":
                fins.append((i, j))

    if len(inicios) != 1 or len(fins) != 1:
        raise ValueError("Erro: o labirinto deve conter exatamente um 'S' e um 'E'.")
    return inicios[0], fins[0]

def destacar_caminho(labirinto, caminho):
    lab_copia = [linha.copy() for linha in labirinto]
    for (i, j) in caminho[1:-1]:
        lab_copia[i][j] = "*"
    return lab_copia

def imprimir_labirinto(labirinto):
    for linha in labirinto:
        print(" ".join(linha))
    print()
