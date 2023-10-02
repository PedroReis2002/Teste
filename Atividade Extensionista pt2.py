#Isso aqui vai ajudar a gerar os numeros aleatorios
import random

# A ideia é que a ordem seja aluno = [ID, Nome, XP, nivel]
aluno = [1, "Nome", 20, 1]


def gerador(ID, Nome, XP, N):
    print("Boas vindas {}!" .format(Nome))
    # A ideia e que com cada nivel mais variaveis sejam adicionadas
    if N == 1:
        v1 = random.randint(2, 10)
        v2 = random.randint(1, 10)
        # Isso aqui vai garantir que não tenham contas com o resultado negativo
        while True:
            if (v2 == v1):
                v2 = random.randint(1, 10)
                continue
            else:
                break
        operacoes = random.randint(1, 2)
        print("Qual o resultado da seguinte operação?")
        if operacoes == 1:
            print("{} + {} = ?".format(v1, v2))
            resultado = int(input('>>>'" "))
            if resultado == (v1 + v2):
                print("Correto")
            else:
                print("Incorreto")

        elif operacoes == 2:
            while True:    
                if (v2 > v1) or (v2 == v1):
                    v2 = random.randint(1, 10)
                    continue
                else:
                    break
            print("{} - {} = ?".format(v1, v2))
            resultado = int(input('>>>'" "))
            if resultado == (v1 - v2):
                    print("Correto")
            else:
                print("Incorreto")

gerador(aluno[0], aluno[1], aluno[2], aluno[3])