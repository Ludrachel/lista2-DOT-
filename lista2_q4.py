def contar_divisores(numero):
    try:
        if numero <= 0:
            return 0

        divisores = 0
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores += 1

        return divisores

    except TypeError:
        print("Erro: O parâmetro deve ser um número inteiro.")
        return 0
    
numero = 12
quantidade_divisores = contar_divisores(numero)
print(quantidade_divisores)