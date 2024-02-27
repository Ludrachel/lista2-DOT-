def e_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_primos_gemeos(n):
    primos_gemeos = []
    try:
        for i in range(2, n - 1):
            if e_primo(i) and e_primo(i + 2):
                primos_gemeos.append((i, i + 2))
    except TypeError:
        print("Erro: O valor de 'n' deve ser um número inteiro.")
        return []
    return primos_gemeos

n = 100
pares_primos_gemeos = encontrar_primos_gemeos(n)
print(pares_primos_gemeos)