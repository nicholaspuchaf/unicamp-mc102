from math import floor


def soma_vetores(v1: list[int], v2: list[int]) -> list[int]:

    tam = len(v1) if len(v1) > len(v2) else len(v2)

    resultado = []

    for i in range(tam):

        if len(v1) < i+1:
            v1.append(0)
        if len(v2) < i+1:
            v2.append(0)

        resultado.append(v1[i]+v2[i])

    return resultado


def subtrai_vetores(v1: list[int], v2: list[int]) -> list[int]:
    tam = len(v1) if len(v1) > len(v2) else len(v2)

    resultado = []

    for i in range(tam):

        if len(v1) < i+1:
            v1.append(0)
        if len(v2) < i+1:
            v2.append(0)

        resultado.append(v1[i]-v2[i])

    return resultado


def multiplica_vetores(v1: list[int], v2: list[int]) -> list[int]:
    tam = len(v1) if len(v1) > len(v2) else len(v2)
    resultado = []
    for i in range(tam):
        if len(v1) < i+1:
            v1.append(1)
        if len(v2) < i+1:
            v2.append(1)
        resultado.append(v1[i]*v2[i])

    return resultado


def divide_vetores(v1: list[int], v2: list[int]) -> list[int]:
    tam = len(v1) if len(v1) > len(v2) else len(v2)

    resultado = []

    for i in range(tam):
        if len(v1) < i+1:
            v1.append(0)
        if len(v2) < i+1:
            v2.append(1)

        resultado.append(floor(v1[i]/v2[i]))

    return resultado


def multiplicacao_escalar(v1: list[int], e: int) -> list[int]:
    v2 = []
    for i in range(len(v1)):
        v2.append(v1[i]*e)
    return v2


def n_duplicacao(v1: list[int], n: int) -> list[int]:
    res: list[int] = []
    for _ in range(n):
        res = res + v1
    return res


def soma_elementos(v1: list[int]) -> int:
    soma: int = 0
    for i in v1:
        soma += i
    return soma


def produto_interno(v1: list[int], v2: list[int]) -> int:
    newVet = multiplica_vetores(v1, v2)
    return soma_elementos(newVet)


def multiplica_todos(v1: list[int], v2: list[int]) -> list[int]:
    resultado = []

    for i in range(len(v1)):
        soma = 0
        for j in range(len(v2)):
            soma += v1[i]*v2[j]

        resultado.append(soma)

    return resultado


def correlacao_cruzada(v1: list[int], vmenor: list[int]) -> list[int]:

    resultado = []
    i = 0
    while i <= len(v1)-len(vmenor):
        soma = 0

        for j in range(len(vmenor)):
            soma += v1[i+j] * vmenor[j]
        i += 1
        resultado.append(soma)

    return resultado


def converterInt(vetor: list[str]) -> list[int]:
    retorno: list[int] = []
    for i in vetor:
        retorno.append(int(i))
    return retorno


if __name__ == "__main__":

    vetor1 = converterInt(input().split(","))
    vetor2 = []
    comando = ""
    comando = input()
    while comando != "fim":
        if comando == "soma_vetores":
            vetor2 = converterInt(input().split(','))
            vetor1 = soma_vetores(vetor1, vetor2)
        elif comando == "subtrai_vetores":
            vetor2 = converterInt(input().split(','))
            vetor1 = subtrai_vetores(vetor1, vetor2)
        elif comando == "multiplica_vetores":
            vetor2 = converterInt(input().split(','))
            vetor1 = multiplica_vetores(vetor1, vetor2)
        elif comando == "divide_vetores":
            vetor2 = converterInt(input().split(','))
            vetor1 = divide_vetores(vetor1, vetor2)
        elif comando == "multiplicacao_escalar":
            e = int(input())
            vetor1 = multiplicacao_escalar(vetor1, e)
        elif comando == "n_duplicacao":
            n = int(input())
            vetor1 = n_duplicacao(vetor1, n)
        elif comando == "soma_elementos":
            vetor1 = [soma_elementos(vetor1)]
        elif comando == "produto_interno":
            vetor2 = converterInt(input().split(','))
            vetor1 = [produto_interno(vetor1, vetor2)]
        elif comando == "multiplica_todos":
            vetor2 = converterInt(input().split(','))
            vetor1 = multiplica_todos(vetor1, vetor2)
        elif comando == "correlacao_cruzada":
            vetor2 = converterInt(input().split(','))
            vetor1 = correlacao_cruzada(vetor1, vetor2)

        print(vetor1)
        comando = input()