# Projeto PathFinder

O **PathFinder** é um projeto desenvolvido para implementar e analisar o **Algoritmo A\***, uma técnica eficiente de busca utilizada para encontrar o **menor caminho entre dois pontos em um labirinto 2D**. O algoritmo é amplamente aplicado em sistemas de navegação, jogos e robótica, por combinar o custo real percorrido com uma estimativa da distância restante, garantindo soluções rápidas e otimizadas.

## Sobre o Algoritmo A\*

O **Algoritmo A\*** (A-Star) é um dos algoritmos mais populares para busca de caminhos em grafos ou grades. Ele foi projetado para encontrar o caminho mais curto entre um ponto inicial (**S**) e um ponto final (**E**) enquanto evita obstáculos, sendo ideal para ambientes como **labirintos, mapas e grids de navegação**.

A principal característica do A\* é a combinação de dois fatores na sua busca:
- **g(n):** o custo real do caminho percorrido até o ponto atual.  
- **h(n):** uma estimativa heurística da distância até o destino (neste caso, a **distância de Manhattan**).  

A função de avaliação usada é:  f(n) = g(n) + h(n) onde o algoritmo sempre expande o nó com o menor valor de `f(n)`.

Essa estratégia faz com que o A\* equilibre **exploração** (buscando novos caminhos) e **otimização** (mantendo o foco no destino), tornando-o muito mais eficiente do que algoritmos de busca exaustiva.

## Como executar o projeto

1. Clone o repositório do link: `https://github.com/iannovais/fpaa-robozinho-caminho.git`

2. Depois entre na pasta necessária de copie: `cd code`

3. logo após, execute o main: `python main.py`

4. A saída esperada é: 
- O labirinto original.
- O menor caminho encontrado em forma de coordenadas.
- O labirinto atualizado com o caminho marcado com "*".


## Estrutura do projeto

A organização do projeto foi pensada para manter o código modular e fácil de entender, separando a lógica principal da execução.

```
FPAA-ROBOZINHO-CAMINHO/
│
├── code/
│   ├── caminho.py        # Implementação do algoritmo A*
│   └── main.py           # Script principal para execução
│
├── .gitignore            # Ignora arquivos temporários e cache no Git
└── README.md             # Documentação do projeto
```



## Funcionamento do Algoritmo Implementado

No código desenvolvido, o **Algoritmo A*** utiliza uma **fila de prioridade (heapq)** para decidir qual posição do labirinto será analisada em seguida. Cada célula é avaliada de acordo com a soma de dois valores: o **custo real percorrido (g)** e a **heurística da distância de Manhattan (h)**, que estima o quanto falta até o destino. Durante a execução, o algoritmo inicia no ponto **S** e percorre o labirinto expandindo as posições vizinhas válidas (cima, baixo, esquerda e direita). Para cada posição, calcula-se:

$$
\boldsymbol{f(n) = g(n) + h(n)}
$$

* **g(n)** é incrementado a cada passo, representando o custo acumulado do caminho percorrido.
* **h(n)** é obtido pela **distância de Manhattan**, somando a diferença entre as coordenadas do ponto atual e do ponto final — uma estimativa simples e eficiente para grids bidimensionais.

A cada iteração, o algoritmo escolhe o nó com o **menor valor de f(n)**, priorizando caminhos que já têm baixo custo e que aparentam estar mais próximos do destino. Esse processo continua até que o ponto **E** seja alcançado. Por fim, o programa reconstrói o caminho percorrido, marcando-o no labirinto com o símbolo `"*"` para evidenciar a rota mais curta. Dessa forma, o **PathFinder** demonstra de maneira prática como o **Algoritmo A*** combina o custo real do trajeto e a estimativa heurística para encontrar, de forma otimizada, o **menor caminho possível dentro de um labirinto**.


