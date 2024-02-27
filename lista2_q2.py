def verificar_anagrama(str1, str2):
    try:
        # Remover espaços em branco e converter para letras minúsculas
        str1 = str1.replace(" ", "").lower()
        str2 = str2.replace(" ", "").lower()

        # Verificar se as strings têm o mesmo comprimento
        if len(str1) != len(str2):
            return False

        # Verificar se as strings são anagramas
        for char in str1:
            if char in str2:
                str2 = str2.replace(char, "", 1)
            else:
                return False

        return True

    except AttributeError:
        print("Erro: Os parâmetros devem ser strings.")
        return False
    
str1 = "alo"
str2 = "ola"
resultado = verificar_anagrama(str1, str2)
print(resultado)