# Projeto PathFinder

O **PathFinder** é um projeto desenvolvido para implementar e analisar o **Algoritmo A\***, uma técnica eficiente de busca utilizada para encontrar o **menor caminho entre dois pontos em um labirinto 2D**. O algoritmo é amplamente aplicado em sistemas de navegação, jogos e robótica, por combinar o custo real percorrido com uma estimativa da distância restante, garantindo soluções rápidas e otimizadas.

## Sobre o Algoritmo A\*

O **Algoritmo A\*** (A-Star) é um dos algoritmos mais populares para busca de caminhos em grafos ou grades. Ele foi projetado para encontrar o caminho mais curto entre um ponto inicial (**S**) e um ponto final (**E**) enquanto evita obstáculos, sendo ideal para ambientes como **labirintos, mapas e grids de navegação**.

A principal característica do A\* é a combinação de dois fatores na sua busca:
- **g(n):** o custo real do caminho percorrido até o ponto atual.  
- **h(n):** uma estimativa heurística da distância até o destino (neste caso, a **distância de Manhattan**).  

A função de avaliação usada é:  f(n) = g(n) + h(n) onde o algoritmo sempre expande o nó com o menor valor de `f(n)`.

Essa estratégia faz com que o A\* equilibre **exploração** (buscando novos caminhos) e **otimização** (mantendo o foco no destino), tornando-o muito mais eficiente do que algoritmos de busca exaustiva.



