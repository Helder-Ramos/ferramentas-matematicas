import math

def divisores(numero):
    divisores = set()
    limite = int(math.sqrt(numero)) + 1

    for i in range(1, limite):
        if numero % i == 0:
            divisores.add(i)
            divisores.add(numero // i)

    return sorted(list(divisores))