def encontrar_elemento_repetido(lista):
    try:
        if not isinstance(lista, list):
            raise TypeError("O parâmetro deve ser uma lista.")

        contador = {}
        for elemento in lista:
            if elemento in contador:
                contador[elemento] += 1
            else:
                contador[elemento] = 1

        elemento_repetido = None
        maior_contagem = 0

        for elemento, contagem in contador.items():
            if contagem > maior_contagem:
                elemento_repetido = elemento
                maior_contagem = contagem

        return elemento_repetido

    except TypeError as e:
        print("Erro:", str(e))
        return None
    
lista = [1, 2, 3, 2, 4, 3, 2, 1, 5]
elemento_repetido = encontrar_elemento_repetido(lista)
print(elemento_repetido)