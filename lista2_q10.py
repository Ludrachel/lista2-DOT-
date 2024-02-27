def verificar_quadrado_perfeito(numero):
    try:
        if not isinstance(numero, int):
            raise TypeError("O parâmetro deve ser um número inteiro.")

        if numero < 0:
            return False

        raiz = 1
        while raiz * raiz <= numero:
            if raiz * raiz == numero:
                return True
            raiz += 1

        return False

    except TypeError as e:
        print("Erro:", str(e))
        return False
    
numero = 25
eh_quadrado_perfeito = verificar_quadrado_perfeito(numero)
print(eh_quadrado_perfeito)