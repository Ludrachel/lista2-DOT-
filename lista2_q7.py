def encontrar_elemento_faltante(lista):
    try:
        n = len(lista) + 1
        soma_esperada = (n * (n + 1)) // 2
        soma_real = sum(lista)
        elemento_faltante = soma_esperada - soma_real
        return elemento_faltante

    except TypeError:
        print("Erro: O parâmetro deve ser uma lista de números.")
        return None
    
lista = [4, 3, 1, 5]
elemento_faltante = encontrar_elemento_faltante(lista)
print(elemento_faltante)