def remover_vogais(string):
    try:
        if not isinstance(string, str):
            raise TypeError("O parâmetro deve ser uma string.")

        vogais = "aeiouAEIOU"
        nova_string = ""

        for char in string:
            if char not in vogais:
                nova_string += char

        return nova_string

    except TypeError as e:
        print("Erro:", str(e))
        return ""
    
string = "ola, mundo!"
nova_string = remover_vogais(string)
print(nova_string)