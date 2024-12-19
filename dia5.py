# Estruturas de Repetição
# Repetir uma coisa N vezes
# Onde N, a gente pode definir
#ou n é uma condição
# um looping com uma condicao mal definida = loop infinito = bug
frutas = ["maça", "banana","laranja"]

#for varivael in sequencia  -- vai repitir o numero de vezes dentro do array
# bloco de código repetido n vezes

for fruta in frutas:
    print(fruta)

#while

contador = 0

while contador < 5:
    contador += 1
    print("Num while", contador)

#Exercicio 1 - Imprimir Numeros de 1 a 10
for numero in range(1,11):
    print(numero)

#Exercicio 2 - Somatorio de 1 a N
valores_somatorio = int(input("Informe um numero inteiro e positivo: "))
soma = 0
for i in range(1, valores_somatorio+1):
    soma += i # soma = soma + i
    print("A soma dos números de 1 a ", valores_somatorio, " é: ", soma)

#Exercicio 3 - Tabuada
tabuada = int(input("Digite o numero que deseja ver a tabuada: "))
for i in range(1,11):
    resultado = tabuada * i
    print(i," x ", tabuada, " = ", resultado)
    
#Exercico 4 - Contando numeros pares e impares
pares = 0
impares = 0

for i in range(1,21):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
        
print("Numeros impares: ", impares)
print("Numeros pares: ", pares)

#Exercicio 5 - Adivinhe o número
import random
numero_aleatorio = random.randrange(1,100)

while True:
    escolha_usuario = int(input("Escolha um numero entre 1 e 100: "))
    
    if escolha_usuario == numero_aleatorio:
        print(f"Você adivinhou o número! {numero_aleatorio}")
        break
    elif escolha_usuario < numero_aleatorio:
        print(f"Numero {escolha_usuario} é menor que o numero sorteado")
    elif escolha_usuario > numero_aleatorio:
        print(f"Numero {escolha_usuario} é maior que o numero sorteado")    

# Exercicio 6 - Calcular o Fatorial de um número
fatorial = int(input("Digite um número para o calculo do fatorial: "))
n = 1
for i in range(n, fatorial):
    fatorial = fatorial * n
    n += 1

print(f"fatorial de {n} é: ", fatorial)

# Exercicio 7 - Serie Fibonacci
numero_fibonacci = int(input("Informe a quantiade de vezes quer ver a sequencia de fibonacci: "))
a, b = 0,1
if numero_fibonacci <= 0:
    print("Por favor insira um numero positivo")
    
for i in range(numero_fibonacci):
    a,b = b, a + b
    print(f"termo {i + 1}: ",a )