def contar_caracteres(string):
    try:                           
        contagem = {}                      # Começar com o  dicionário vazio para armazenar a contagem de caracteres

        for char in string:                # Iterar por cada caractere na string
            if char in contagem:           # Verificar se o caractere já está no dicionário
                contagem[char] += 1        # Se estiver, incrementar a contagem
            else:
                contagem[char] = 1         # Se não estiver, adicionar o caractere ao dicionário com contagem 1

        return contagem

    except TypeError:
        print("Erro: O parâmetro deve ser uma string.")
        return {}
    
string = "parabens!"
resultado = contar_caracteres(string)
print(resultado)