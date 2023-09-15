#ESTE É UM ENORME COMPILADO DE VÁRIOS ALGORÍTMOS FEITOS DURANTE O CURSO SENAC
#SÃO TODOS FEITOS POR MIM, E TAMBÉM CRIEI UM MENU PARA UM FÁCIL ACESSO, ENTÃO É SÓ INICIAR O CÓDIGO INTEIRO E SELECIONAR A OPÇÃO QUE VOCÊ QUER
#ENTÃO VOCÊ VIZUALIZA O EXERCÍCIO SELECIONADO
#EM ALGUNS PROGRAMAS, EU FIZ UMAS ANOTAÇÕES, PARA QUE SEJA UM POUCO MAIS TRANQUILO O ENTENDIMENTO, TANTO JÁ SABENDO QUANTO NÃO SABENDO ALGO SOBRE PROGRAMAÇÃO

#Atividade para saber se vale apena comprar a TV (Apenas se for 32 polegadas e 1900 reais, ou maior ou mais barata)

from time import sleep

def televisão():

    x = int(input("\nPolegadas da TV: "))
    y = float(input("Valor da TV: "))

    if x < 32 and y > 1900: #Se for menor que 32 polegadas e maior que 1900 não deve comprar
        print("\nNão comprar.")
    elif x >= 32 and y <= 1900:
        print("\nComprar.")
    else:
        print("\nNão Comprar.")

#Atividade de termômetro para saber se está com febre 
#Essa atividade foi refeita mais abaixo com uma fórmula melhorada

def temperatura1():

    temperatura = float(input("\nCom quantos graus você está?: "))

    if temperatura >= 38:
        print("\nVocê está com febre")
    else:
        print("\nNão está com febre")

#Atividade de Valores de frutas e alteração de preço (Se ouve inflação ou não)

def frutas():

    print("\n[1] - Tomate", "\n[2] - Limão", "\n[3] - Banana", "\n[4] - Laranja") #Aqui foi colocado os nomes com números para o entendimento mais fácil

    selec = int(input("\nInforme o número da fruta que quer saber o valor: "))
    val = float(input("\nDigite quanto está a fruta atualmente: "))

    y1 = 2.47 #Uma variável pra cada valor das frutas
    y2 = 0.49
    y3 = 1.35
    y4 = 0.30

    if selec == 1: 
        if val > y1:
            x1 = val - y1
            print("\nA unidade custa",y1,"seu valor aumentou em R$:",round(x1,3)) #Esse comando chamado round, formata a variável
        elif val < y1:
            x2 = y1 - val
            print("\nA unidade custa",y1,"seu valor diminuiu em R$:",round(x2,3))
        else:
            print("\nO Valor se manteve o mesmo")
            
    if selec == 2:
        if val > y2:
            x3 = val - y2
            print("\nA unidade custa",y2,"seu valor aumentou em R$:",round(x3,3))
        elif val < y2:
            x4 = y2 - val
            print("\nA unidade custa",y2,"seu valor diminuiu em R$:",round(x4,3))
        else:
            print("\nO Valor se manteve o mesmo")
            
    if selec == 3:
        if val > y3:
            x5 = val - y3
            print("\nA unidade custa",y3,"seu valor aumentou em R$:",round(x5,3))
        elif val < y3:
            x6 = y3 - val
            print("\nA unidade custa",y3,"seu valor diminuiu em R$:",round(x6,3))
        else:
            print("\nO Valor se manteve o mesmo")

    if selec == 4:
        if val > y4:
            x7 = val - y4
            print("\nA unidade custa",y4,"seu valor aumentou em R$:",round(x7,3))
        elif val < y4:
            x8 = y4 - val
            print("\nA unidade custa",y4,"seu valor diminuiu em R$:",round(x8,3))
        else:
            print("\nO Valor se manteve o mesmo")

#Atividade, múltiplo de 5, sim ou não

def multiplo5():

    x = int(input("\nDigite um número: "))

    if x % 5 == 0: #Este comando faz x ser um número que quando dividido por 5 dê 0, sendo assim, um múltiplo de 5
        print(f"\n{x} é um múltiplo de 5") #O f transforma em função, e com isso podemos colocar o x no meio do print sem usar vírgulas
    else:
        print(f"\n{x} não é um múltiplo de 5")

#Atividade de Aprovado ou Reprovado com média 7

def aprovreprov():

    nota1 = float(input("\nDigite a nota da avaliação 1: "))

    if nota1 >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

    nota2 = float(input("\nDigite a nota da avaliação 2: "))

    if nota2 >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

    nota3 = float(input("\nDigite a nota da avaliação 3: "))

    if nota3 >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

    nota4 = float(input("\nDigite a nota da avaliação 4: "))

    if nota4 >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

#Atividade de Par ou Impar

def parimpar():

    x = int(input("\nDigite um número: "))
    resultado = x % 2 #Aqui 2 ja é um número par, então se o número for dividido por 2 até chegar a 0 ele é par, se sobrar, é impar
    if resultado == 0:
        print("\n",x, "é par")
    else:
        print("\n",x, "é impar")

#Atividade testando o While, mostrando valores menores que o informado até chegar a 0

def testwhile():

    mast = int(input("\nDigite o número: "))

    while (mast > 0): #Uso do while, ele significa ENQUANTO, ou seja, enquanto mast for maior que 0 ele continua a diminuir
        print("Número: ", mast)
        mast = mast -1 
        if (mast == 0): #No momento quem que mast chegar a 0 ele puxará o comando break
            print("\nBom, acabamos, até a próxima\n")
            break #Aqui o break faz com que o código seja finalizado

#Atividade usando o "for", mostrando multiplos de 3 até chegar ao número informado

def testfor():

    x = int(input("\nDigite o Número: "))

    for x in range (0,x,1): #Aqui dentro dos parêntesis, o primeiro valor é o início, o segundo é o fim, e o terceiro é pra dizer que vai de 1 em 1 
        if (x % 3 == 0): #Este comando faz todos serem os múltiplos de 3 
            print(x,"\n")

#Atividade de somar números infinitamente até que o resultado dê 0

def somaate0():

    x = float(input("\nDigite seu número" ))
    y = float(input("Digite seu número" ))
    resultado = x+y 
    print("")
    print(resultado)

    while (resultado != 0): #Aqui temos o comando while, seguido de um sinal != que significa diferença, ou seja, enquanto for diferente de 0...

        x = float(input("\nDigite seu número" ))
        resultado = resultado + x
        print("")
        print(resultado)

        if (x==0): #Aqui em baixo deixa claro que quando o valor bater 0, o código quebra 
            break

#Atividade todos os números divisíveis por 7 porém que não são multiplos de 5 (entre 2000 e 3200)

def div7mult5():

    x = 0

    for x in range (2000, 3200,1): #Aqui é informado que a conta será feita apenas do número 2000 ao 3200, sendo contado 1 por 1
        if (x%7==0): #Deve ser divisível por 7
            if (x%5 != 0): #Deixa claro que quando for múltiplo de 5 não deve ser contabilizado
                print (x,"\n")

#Atividade de fazer IMC 

def imc():

    pac = int(input("\nDigite o numero de pacientes: "))

    for pac in range (0,pac,1): #Aqui o "pac" escrito, será informado acima, e entrará para a fórmula
        nome = (input("\nDigite o nome do paciente: "))
        altura = float(input("Digite a altura do paciente: "))
        peso = float(input("Digite o peso do paciente: "))

        imc = peso /(altura**2) #Essa é a fórmula real para fazer um imc
        print(f"\nO {nome}, tem {altura} de altura, pesa {peso} tem o imc igual a {imc:.2f}") 
        #Nesse final usamos o f no início e o :.2f dentro da função, após a variável, para formatarmos as casas decimais

#Atividade de desconto no inss com valores estipulados no exercício

def inssdesc():

    sal = float(input("\nDigite seu salário R$: "))

    x = 600.00
    y = 1200.00
    z = 2000.00

    if sal <= x:
        desc = 0
    elif sal <= y:
        desc = sal * 0.20
    elif sal <= z:
        desc = sal * 0.25
    else:
        desc = sal * 0.30

    print(f"\nO desconto do INSS para um salário de R$ {sal:.2f} é de R$ {desc:.2f}") #Aqui novamente é usado o comando de formatação para poder definir as casas decimais 

#Atividade de média ponderada

def mediapond():

    nota1 = float(input("\nDigite a sua nota da avaliação 1: "))
    nota2 = float(input("Digite a sua nota da avaliação 2: "))

    result = (nota1*2)+(nota2*3)
    result2 = result / 5

    print(f"\nSua média ponderada é:{result2:.2f}")

    print("")

#Atividade de nota sendo 9,8,7,5,4 notas diferentes

def notas2():

    nota1 = float(input("\nDigite sua nota: "))

    if nota1 >= 9:
        print("\nExcelente")
    elif nota1 < 9 and nota1 >=8: #Aqui é usado o comando "and" para significar 2 coisas ao mesmo tempo, se tal e tal faça isso...
        print("\nÓtimo")
    elif nota1 < 8 and nota1 >=7:
        print("\nBom")
    elif nota1 < 7 and nota1 >=5:
        print("\nRegular")
    else:
        print("\nPéssimo")

#Atividade de termômetro porém mais complexa

def termometro2():

    while True: 
        temperatura = (input("\nCom quantos graus você está?: ")) #Aqui a variável não pode usar float nem int, deve ser puro

        if temperatura == ("sair"): #Ao digitar alguma temperatura, o programa irá rodar, mas ao digitar "sair" o programa fecha
            print("saindo...")
            break #Com a variável pura, o break funciona

        temperatura = int(temperatura) #Nesse momento a variável deve ser transformada em int para poder ser trabalhada
        if temperatura <= 39 and temperatura >= 38:
            print(f"\nSua temperatura é: {temperatura}\nVocê está com febre, tome um remédio e repouse.")
        elif temperatura > 39:
            print(f"\nSua temperatura é: {temperatura}\nVocê está com muita febre, tome um remédio e procure um médico")
        else:
            print(f"\nSua temperatura é: {temperatura}\nVocê não está com febre")

    print("")

#Menu para puxar todos os exercícios e transformálos em 1 só

def mainMenu():
    while True:
        print("--------------------\n-----Menu Principal------\n--------------------\n")
        print("[1] - Televisão\n[2] - Termômetro 1\n[3] - Termômetro 2\n[4] - Inflação de Fruta\n[5] - Múltiplos de 5\n[6] - Aprovado ou Reprovado\n[7] - Par ou Ímpar\n[8] - Teste do While\n[9] - Teste do for\n[10] - Soma Infinita\n[11] - Calculo de IMC\n[12] - Calcular desconto do INSS\n[13] - Média Ponderada\n[14] - Notas Escolares\n[15] - Teste do for 2\n[0] - Sair\n")

        jdz = int(input("Digite um numero:"))

        if jdz == 1:
            print("\nEste exercício é para para saber se deve ou não comprar uma televisão, os requistos são que ela seja de 32 polegadas e com valor de R$: 1900,00, com isso sendo menor ou mais cara, ela não vale apena.")
            televisão()
            sleep(5)
        elif jdz == 2:
            print("\nEste exercício é um exercício bem simples para um termômetro, recomendo que veja o exercício 2 de termômetro, mas ele mostra a evolução, insira seus graus de febre para saber se está com febre ou não.")
            temperatura1()
            sleep(5)
        elif jdz == 3:
            print("\nEste exercício é uma versão mais complexa do termômetro usando os comandos de while para ser mais preciso.")
            termometro2()
            sleep(5)
        elif jdz == 4:
            print("\nEste exercício é para dizer se a fruta que você deseja teve uma inflação ou uma deflação no valor, selecione a fruta e informe o valor dela (OBS: Os valores no código já são predefinidos).")
            frutas()
            sleep(5)
        elif jdz == 5:
            print("\nEste exercício é para para saber se o número informado é um múltiplo de 5 ou não.")
            multiplo5()
            sleep(5)
        elif jdz == 6:
            print("\nEste exercício é para saber se o aluno foi aprovado ou reprovado, de acordo com sua nota, baseando-se em uma média de valor 7.0.")
            aprovreprov()
            sleep(5)
        elif jdz == 7:
            print("\nEste exercício é para saber se o número informado é par, ou ímpar.")
            parimpar()
            sleep(5)
        elif jdz == 8:
            print("\nEste exercício é apenas um teste com o comando while, onde ele contará automaticamente do número informado até o 0, subtraindo de 1 em 1.")
            testwhile()
            sleep(5)
        elif jdz == 9:
            print("\nEste exercício é apenas para testar o comando for, quando o valor for informado, será contabilizado todos os número múltiplos de 3 até o número informado.")
            testfor()
            sleep(5)
        elif jdz == 10:
            print("\nEste exercício é uma repetição, onde ele soma o primeiro e o segundo número, informa o valor, e enquanto for colocando mais números ele vai somando naquele resultado, ele finaliza quando o valor chegar a 0, ou seja, você deve colocar o valor atual como negativo, então chegará a 0 e o código finalizada.")
            somaate0()
            sleep(5)
        elif jdz == 11:
            print("\nEste exercício calcula o IMC (Índice de Massa Corporal) com base nos valores informados pelo usuário.")
            imc()
            sleep(5)
        elif jdz == 12:
            print("\nEste exercício calcula o desconto do INSS no seu salário.")
            inssdesc()
            sleep(5)
        elif jdz == 13:
            print("\nEste exercício é um cálculo de média ponderada, informe os valores e receba a média.")
            mediapond()
            sleep(5)
        elif jdz == 14:
            print("\nEste exercício é para receber notas escolares e informar se ela está 'excelente','ótimo','bom','regular' ou 'péssimo'.")                                  
            notas2()
            sleep(5)
        elif jdz == 15:
            print("\nEste exercício é mais um teste do for, onde ele mostra os números divisíveis por 7 mas exclui os múltiplos de 5, apenas entre os números 2000 até 3200.")
            div7mult5()
            sleep(5)
        elif jdz == 0:
            print("Saindo...\n")
            sleep(3)
            break
        else:
            print("Opção Invalida")
            sleep(3)



mainMenu()



