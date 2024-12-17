#exercicio 5 - Calculadora
numero1 = float(input("Digite o primeiro numero: ")) #permite que o usuário insira dados
numero2 = float(input("Digite o segundo numero: "))

print(f" Soma = {numero1} + {numero2}  =  {numero1 + numero2}")
print(f" Subtração = {numero1} - {numero2}  =  {numero1 - numero2}")
print(f" Multiplicação = {numero1} * {numero2}  =  {numero1 * numero2}")
print(f" Divisão = {numero1} / {numero2}  =  {numero1 / numero2}")

#exercicio 6 - Conversor de temperadura
valor_celcius = float(input("Digite o valor da temperatura em graus Celcius: "))
formula = valor_celcius * (9/5) + 32
print("Valor convertido para Fahrenheit é:", formula)

#exercicio 7 - Area de um circulo
pi = 3.14159
raio = int(input("Digite o valor do raio do circulo: "))
area = pi * (raio*raio)
print("Valor da área do circulo é: ", area)