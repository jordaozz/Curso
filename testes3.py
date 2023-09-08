#NOTA IMPORTANTE, TODOS ESSES TRABALHOS FUNCIONAM INDIVIDUALMENTE, COPIE OS TESTOS, COLE NA PLATAFORMA E TESTE, POIS SE TENTAR RODAR TODOS JUNTOS DARÁ ERRO
#ESTE É APENAS UM COMPILADO DE TRABALHOS PARA UMA VIZUALIZAÇÃO MAIS FÁCIL

#Atividade para saber se vale apena comprar a TV (Apenas se for 32 polegadas e 1900 reais, ou maior ou mais barata)

print("")

x = int(input("Polegadas da TV: "))
y = float(input("Valor da TV: "))

if x < 32 and y > 1900:
    print("Não comprar")
elif x >= 32 and y <= 1900:
    print("Comprar")
else:
    print("Não Comprar")

print("")

#Atividade de termômetro para saber se está com febre 

print("")

temperatura = float(input("Com quantos graus você está?: "))

if temperatura >= 38:
    print("Você está com febre")
else:
    print("Não está com febre")

print("")

#Atividade de Valores de frutas e alteração de preço (Se ouve inflação ou não)

print("")

print("\n[1] - Tomate", "\n[2] - Limão", "\n[3] - Banana", "\n[4] - Laranja")

print("")

selec = int(input("Informe o número da fruta que quer saber o valor: "))
val = float(input("Digite quanto está a fruta atualmente: "))

y1 = 2.47
y2 = 0.49
y3 = 1.35
y4 = 0.30

if selec == 1:
    if val > y1:
        x1 = val - y1
        print("\nA unidade custa",y1,"seu valor aumentou em R$:",round(x1,3))
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



