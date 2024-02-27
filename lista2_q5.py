def verificar_ano_bissexto(ano):
    try:
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            return True
        else:
            return False

    except TypeError:
        print("Erro: O parâmetro deve ser um número inteiro.")
        return False
    
ano = 2024
resultado = verificar_ano_bissexto(ano)
print(resultado)