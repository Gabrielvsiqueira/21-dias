#Exercicio 5
valor_saque = int(input("Digite o valor do saque: "))
if valor_saque < 0:
    print("valor menor que 0 é impossível de sacar.")
else:
    nota_100 = valor_saque // 100 #vai pegar somente o valor inteiro do numero dividido
    valor_saque %= 100 # vai incrementar o valor inteiro na variavel, somente o valor inteiro
    
    nota_50 = valor_saque // 50
    valor_saque %= 50
    
    nota_20 = valor_saque // 20
    valor_saque %= 20
    
    nota_10 = valor_saque // 10
    valor_saque %= 10
    
    nota_5 = valor_saque // 5
    valor_saque %= 5
    
    nota_1 = valor_saque // 1 
    valor_saque %= 1  
    
    print(f"Valor corresponde há: {nota_100} notas de $100, {nota_50} notas de $50, {nota_20} notas de $20, {nota_10} notas de $10, {nota_5} notas de $5, {nota_1} notas de $1.")
    
# Exercicio 2 pedra, papel e tessoura
import random
print("########### PEDRA, PAPEL OU TESSOURA ###########")
opcoes = ["Pedra", "Papel", "Tessoura"]
usuario = input("Informe sua jogada:")
computador = random.choice(opcoes)

if usuario == computador:
    print(f"Empate: {usuario} x {computador}")
elif (usuario == "pedra" and computador == "tessoura") or (usuario == "tessoura" and computador == "papel") or (usuario == "papel" and computador == "pedra"):
    print("Você ganhou!")
else:
    print("Computador ganhou!")
    
# Exercico 3 tarifa de taxi
km_percorrido = float(input("Informe a quantidade de Km percorridos: "))
valor_corrida = 4.00 + (km_percorrido * 0.25)
if km_percorrido <= 0:
    print(f" Cobrado somente o valor fixo da taxa = {valor_corrida}")
else:
    print(f"Valor total da corrida = R${valor_corrida:.2f}")
