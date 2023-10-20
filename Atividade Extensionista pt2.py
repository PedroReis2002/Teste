import random

alunos = []

# Adiciona os dados do aluno dentro de um dicionário,
# que por sua vez é acrescentado em uma lista chamada "alunos".
def adiciona_aluno(nome, identificacao_aluno, xp, nivel):
    aluno = {
        'Nome': nome,
        'Id': identificacao_aluno,
        'Xp': xp,
        'Nível': nivel
    }
    alunos.append(aluno)

# Função responsável por gerar as questões do aluno,
# Bem como por retornar os valores do seu xp e nível de acordo com suas respostas.
def detector_nivel(nome, nivel, xp):
    print("Boas vindas {}!" .format(nome))
    if nivel == 1:
        xp = gerador_questoes_lv1(nome, nivel, xp)
        return xp
    elif nivel == 2:
        xp = gerador_questoes_lv2(nome, nivel, xp)
        return xp
    elif nivel == 3:
        xp = gerador_questoes_lv3(nome, nivel, xp)
        return xp

def gerador_questoes_lv1(nome, nivel, xp):
    while xp < 50:
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
                print("{} ganhou +10 de XP" .format(nome))
                xp += 10
                if xp >= 50:
                    return xp
                else:
                 continue
            else:
                print("Incorreto")
                continue
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
                print("{} ganhou +10 de XP" .format(nome))
                xp += 10
                if xp >= 50:
                    return xp
                else:
                 continue
            else:
                print("Incorreto")
                continue

# Gerador de questôes nivel 2
def gerador_questoes_lv2(nome, nivel, xp):
    while xp < 200:
        v1 = random.randint(2, 30)
        v2 = random.randint(1, 30)
        # Isso aqui vai garantir que não tenham contas com o resultado negativo
        while True:
            if (v2 == v1):
                v2 = random.randint(1, 30)
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
                print("{} ganhou +30 de XP" .format(nome))
                xp += 30
                if xp >= 200:
                    return xp
                else:
                 continue
            else:
                print("Incorreto")
                continue
        elif operacoes == 2:
            while True:
                if (v2 > v1) or (v2 == v1):
                    v2 = random.randint(1, 30)
                    continue
                else:
                    break
            print("{} - {} = ?".format(v1, v2))
            resultado = int(input('>>>'" "))
            if resultado == (v1 - v2):
                print("Correto")
                print("{} ganhou +30 de XP" .format(nome))
                xp += 30
                if xp >= 200:
                    return xp
                else:
                 continue
            else:
                print("Incorreto")
                continue

# Gerador de questôes nivel 3
def gerador_questoes_lv3(nome, nivel, xp):
    while xp < 500:
        v1 = random.randint(11, 30)
        v2 = random.randint(10, 30)
        # Isso aqui vai garantir que não tenham contas com o resultado negativo
        while True:
            if (v2 == v1):
                v2 = random.randint(10, 30)
                continue
            else:
                break
        operacoes = random.randint(1, 3)
        print("Qual o resultado da seguinte operação?")
        if operacoes == 1:
            print("{} + {} = ?".format(v1, v2))
            resultado = int(input('>>>'" "))
            if resultado == (v1 + v2):
                print("Correto")
                print("{} ganhou +30 de XP" .format(nome))
                xp += 30
                if xp >= 200:
                    return xp
                else:
                 continue
            else:
                print("Incorreto")
                continue
        elif operacoes == 2:
            while True:
                if (v2 > v1) or (v2 == v1):
                    v2 = random.randint(10, 30)
                    continue
                else:
                    break
            print("{} - {} = ?".format(v1, v2))
            resultado = int(input('>>>'" "))
            if resultado == (v1 - v2):
                print("Correto")
                print("{} ganhou +30 de XP" .format(nome))
                xp += 30
                if xp >= 500:
                    return xp
                else:
                 continue
            else:
                print("Incorreto")
                continue
        elif operacoes == 3:
            #Isso aqui serve para balancear as opercaoes com multiplicação
            v1 = random.randint(2, 30)
            v2 = random.randint(1, 10)
            print("{} x {} = ?".format(v1, v2))
            resultado = int(input('>>>'" "))
            if resultado == (v1 * v2):
                print("Correto")
                print("{} ganhou +30 de XP" .format(nome))
                xp += 30
                if xp >= 500:
                    return xp
                else:
                 continue
            else:
                print("Incorreto")
                continue


# Loop principal, coleta o nome do aluno e víncula a ele os dados iniciais do jogo.
while True:
    nomeAluno = str(input('Digite o seu nome: '))
    id_aluno = len(alunos) + 1
    print('')
    # Valores iniciais
    nivel_aluno = 3
    xp_aluno = 0
    xp_aluno = detector_nivel(nomeAluno, nivel_aluno, xp_aluno)
    adiciona_aluno(nomeAluno, id_aluno, xp_aluno, nivel_aluno)

    # Fazendo com que os alunos fiquem ordenados dentro da lista de acordo com o seu XP (ORDEM DECRESCENTE)
    alunos.sort(key=lambda item: item['Xp'], reverse=True)

    posicao = 0
    print(f'{"=-" * 4}RANKING DE ALUNOS{"-=" * 4}')
    for aluno in alunos:
        posicao += 1
        print(f'{posicao}° {aluno}')