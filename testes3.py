#Atividade para saber se vale apena comprar a TV

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

#Atividade de Valores de frutas e alteração de preço

print("")

print("\n[1] - Tomatinho", "\n[2] - Limãozinho", "\n[3] - Bananinha", "\n[4] - Laranjinha")

selec = int(input("Informe o número da fruta que quer saber o valor: "))
val = float(input("Digite quanto está a fruta atualmente: "))

if selec == 1:
    if val > 2.47:
        print("\nA unidade está mais cara que o normal")
    elif val == 2.47:
        print("\nO Valor não foi alterado")
    else:
        print("\nEstá no preço ideal ou mais barato")

if selec == 2:
    if val > 0.49:
        print("\nA unidade está mais cara que o normal")
    elif val == 0.49:
        print("\nO Valor não foi alterado")
    else:
        print("\nEstá no preço ideal ou mais barato")

if selec == 3:
    if val > 1.35:
        print("\nA unidade está mais cara que o normal")
    elif val == 1.35:
        print("\nO Valor não foi alterado")
    else:
        print("\nEstá no preço ideal ou mais barato")

if selec == 4:
    if val > 0.30:
        print("\nA unidade está mais cara que o normal")
    elif val == 0.30:
        print("\nO Valor não foi alterado")
    else:
        print("\nEstá no preço ideal ou mais barato")

print("")



