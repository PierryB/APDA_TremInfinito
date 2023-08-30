escolha = input("Defina o tamanho do trilho \n [1] Trilho infinito \n [2] Trilho finito ")

if(escolha == "1"):
    def calcular_posicao_final(comandos):
        posicao = 0
        for comando in comandos:
            posicao += comando
        return posicao

    lista_de_comandos = []
    a = input("Digite as direcoes divididas por virgula ")
    a = a.split(",")
    for i in a:
        if(i.lower() == "direita"):
            lista_de_comandos.append(1)
        elif(i.lower() == "esquerda"):
            lista_de_comandos.append(-1)
    print(a)
    # lista_de_comandos = [-1, 1, 1, -1]
    print(lista_de_comandos)
    posicao_final = calcular_posicao_final(lista_de_comandos)
    print("A posição final do trem é:", posicao_final)
elif(escolha == "2"):
    def calcular_posicao_final(comandos):
        posicao = 0
        for comando in comandos:
            posicao += comando
        return posicao

    lista_de_comandos = []
    limiteCima = input("Digite o limite maximo do trilho: ")
    limiteBaixo = input("Digite o limite minimo do trilho: ")
    a = input("Digite as direcoes divididas por virgula ")
    a = a.split(",")
    for i in a:
        if(i.lower() == "direita"):
            lista_de_comandos.append(1)
        elif(i.lower() == "esquerda"):
            lista_de_comandos.append(-1)

    print(a)
    print(lista_de_comandos)

    posicao_final = calcular_posicao_final(lista_de_comandos)
    if(posicao_final > int(limiteCima)):
        posicao_final = limiteCima
    elif(posicao_final < int(limiteBaixo)):
        posicao_final = limiteBaixo

    comandos = len(a)
    if(comandos > 30):
        print("Você usou comandos demais(maximo de comandos: 30)")
    else:
        print("A posição final do trem é:", posicao_final)