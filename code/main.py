from caminho import encontrar_pontos, a_star, destacar_caminho, imprimir_labirinto

if __name__ == "__main__":

    labirinto = [
        ["S", "1", "1", "1", "1"],
        ["0", "0", "0", "0", "0"],
        ["0", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["1", "0", "1", "0", "0"],
        ["1", "0", "0", "0", "E"]
    ]

    try:
        inicio, fim = encontrar_pontos(labirinto)
    except ValueError as e:
        print(e)
        exit(1)

    print("Labirinto original:\n")
    imprimir_labirinto(labirinto)

    caminho = a_star(labirinto, inicio, fim)

    if caminho:
        print("Menor caminho encontrado (coordenadas):")
        print(caminho)
        print("\nLabirinto com caminho destacado:\n")
        imprimir_labirinto(destacar_caminho(labirinto, caminho))
    else:
        print("Sem solução encontrada para o labirinto.")