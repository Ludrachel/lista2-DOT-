def contar_substrings(string, substring):
    try:
        if not string or not substring:
            return 0

        count = 0
        index = 0
        while index < len(string):
            index = string.find(substring, index)
            if index == -1:
                break
            count += 1
            index += len(substring)

        return count

    except TypeError:
        print("Erro: Os parâmetros devem ser strings.")
        return 0
    
string = "abracadabra"
substring = "abra"
quantidade_ocorrencias = contar_substrings(string, substring)
print(quantidade_ocorrencias)