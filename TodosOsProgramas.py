#NOTA IMPORTANTE, TODOS ESSES TRABALHOS FUNCIONAM INDIVIDUALMENTE, COPIE OS TESTOS, COLE NA PLATAFORMA E TESTE, POIS SE TENTAR RODAR TODOS JUNTOS DARÁ ERRO
#ESTE É APENAS UM COMPILADO DE TRABALHOS PARA UMA VIZUALIZAÇÃO MAIS FÁCIL
#EM ALGUNS PROGRAMAS, EU FIZ UMAS ANOTAÇÕES, PARA QUE SEJA UM POUCO MAIS TRANQUILO O ENTENDIMENTO, TANTO JÁ SABENDO QUANTO NÃO SABENDO ALGO SOBRE PROGRAMAÇÃO

#Atividade para saber se vale apena comprar a TV (Apenas se for 32 polegadas e 1900 reais, ou maior ou mais barata)

print("")

x = int(input("Polegadas da TV: "))
y = float(input("Valor da TV: "))

if x < 32 and y > 1900: #Se for menor que 32 polegadas e maior que 1900 não deve comprar
    print("Não comprar")
elif x >= 32 and y <= 1900:
    print("Comprar")
else:
    print("Não Comprar")

print("")

#Atividade de termômetro para saber se está com febre 
#Essa atividade foi refeita mais abaixo com uma fórmula melhorada

print("")

temperatura = float(input("Com quantos graus você está?: "))

if temperatura >= 38:
    print("Você está com febre")
else:
    print("Não está com febre")

print("")

#Atividade de Valores de frutas e alteração de preço (Se ouve inflação ou não)

print("")

print("\n[1] - Tomate", "\n[2] - Limão", "\n[3] - Banana", "\n[4] - Laranja") #Aqui foi colocado os nomes com números para o entendimento mais fácil

print("")

selec = int(input("Informe o número da fruta que quer saber o valor: "))
val = float(input("Digite quanto está a fruta atualmente: "))

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
        
print("")

#Atividade, múltiplo de 5, sim ou não

print("")

x = int(input("Digite um número: "))

if x % 5 == 0: #Este comando faz x ser um número que quando dividido por 5 dê 0, sendo assim, um múltiplo de 5
    print(f"{x} é um múltiplo de 5") #O f transforma em função, e com isso podemos colocar o x no meio do print sem usar vírgulas
else:
    print(f"{x} não é um múltiplo de 5")

print("")

#Atividade de Aprovado ou Reprovado com média 7

print("")

nota1 = float(input("Digite a nota da avaliação 1: "))

if nota1 >= 7:
    print("Aprovado")
else:
    print("Reprovado")

nota2 = float(input("Digite a nota da avaliação 2: "))

if nota2 >= 7:
    print("Aprovado")
else:
    print("Reprovado")

nota3 = float(input("Digite a nota da avaliação 3: "))

if nota3 >= 7:
    print("Aprovado")
else:
    print("Reprovado")

nota4 = float(input("Digite a nota da avaliação 4: "))

if nota4 >= 7:
    print("Aprovado")
else:
    print("Reprovado")

print("")

#Atividade de Par ou Impar

print("")

x = int(input("Digite um número: "))
resultado = x % 2 #Aqui 2 ja é um número par, então se o número for dividido por 2 até chegar a 0 ele é par, se sobrar, é impar
if resultado == 0:
    print(x, "é par")
else:
    print(x, "é impar")

print("")

#Atividade testando o While, mostrando valores menores que o informado até chegar a 0

print("")

mast = int(input("Digite o número: "))

while (mast > 0): #Uso do while, ele significa ENQUANTO, ou seja, enquanto mast for maior que 0 ele continua a diminuir
    print("Número: ", mast)
    mast = mast -1 
    if (mast == 0): #No momento quem que mast chegar a 0 ele puxará o comando break
        print("Bom, acabamos, até a próxima")
        break #Aqui o break faz com que o código seja finalizado

print("")

#Atividade usando o "for", mostrando multiplos de 3 até chegar ao número informado

print("")

x = int(input("Digite o Número: "))

for x in range (0,x,1): #Aqui dentro dos parêntesis, o primeiro valor é o início, o segundo é o fim, e o terceiro é pra dizer que vai de 1 em 1 
    if (x % 3 == 0): #Este comando faz todos serem os múltiplos de 3 
        print(x)

print("")

#Atividade de somar números infinitamente até que o resultado dê 0

print("")

x = float(input("Digite seu número" ))
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

print("")

#Atividade todos os números divisíveis por 7 porém que não são multiplos de 5 (entre 2000 e 3200)

print("")

x = 0

for x in range (2000, 3200,1): #Aqui é informado que a conta será feita apenas do número 2000 ao 3200, sendo contado 1 por 1
    if (x%7==0): #Deve ser divisível por 7
        if (x%5 != 0): #Deixa claro que quando for múltiplo de 5 não deve ser contabilizado
            print (x)

print("")

#Atividade de fazer IMC 

print("")

pac = int(input("Digite o numero de pacientes: "))

for pac in range (0,pac,1): #Aqui o "pac" escrito, será informado acima, e entrará para a fórmula
    nome = (input("\nDigite o nome do paciente: "))
    altura = float(input("Digite a altura do paciente: "))
    peso = float(input("Digite o peso do paciente: "))

    imc = peso /(altura**2) #Essa é a fórmula real para fazer um imc
    print(f"\nO {nome}, tem {altura} de altura, pesa {peso} tem o imc igual a {imc:.2f}") 
    #Nesse final usamos o f no início e o :.2f dentro da função, após a variável, para formatarmos as casas decimais
print("")

#Atividade de desconto no inss com valores estipulados no exercício

print("")

sal = float(input("Digite seu salário R$: "))

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

print(f"O desconto do INSS para um salário de R$ {sal:.2f} é de R$ {desc:.2f}") #Aqui novamente é usado o comando de formatação para poder definir as casas decimais 

print("")

#Atividade de média ponderada

print("")

nota1 = float(input("Digite a sua nota da avaliação 1: "))
nota2 = float(input("Digite a sua nota da avaliação 2: "))

result = (nota1*2)+(nota2*3)
result2 = result / 5

print(f"\nSua média ponderada é:{result2:.2f}")

print("")

#Atividade de nota sendo 9,8,7,5,4 notas diferentes

print("")

nota1 = float(input("Digite sua nota: "))

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

print("")

#Atividade de termômetro porém mais complexa

print("")

while True: 
    temperatura = (input("Com quantos graus você está?: ")) #Aqui a variável não pode usar float nem int, deve ser puro

    if temperatura == ("sair"):
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
