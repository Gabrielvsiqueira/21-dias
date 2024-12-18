#Operadores logicos Exercicios

#Exercicio 1 - Calcular Troco
pao = 3.50
leite = 4.20
cafe = 2.80
valor_final = (pao + leite + cafe)
verificar_troco = (20.00 - valor_final)
print("Valor total da conta: ", valor_final)
print("Valor do troco é: ", verificar_troco)

#Exercico 2 - Verificar aprovação de Exame
media_usuario = float(input("digite a media do aluno: "))
frequencia_usuario = int(input("digite a frequencia do aluno: "))
media_final = 7.0
frequencia_final = 75
if media_usuario >= media_final and frequencia_usuario >= frequencia_final:
    print("Estudante aprovado.")
else:
    print("Estudante reprovado.")
    
#Exercicio 3 - Oferta Especial
quantidade_itens = 8
compra_total = 120.00
if quantidade_itens > 10 or compra_total > 100.00:
    print("Usuario apto para receber o desconto.");
else:
    print("Usuário não está apto a receber o desconto"); 

#Exercicio 4 - Sistema de Acesso
senha_inserida = "abcd1234"
senha_correta = "abcd1234"
usuario_bloqueado = False

acesso = (senha_inserida == senha_correta) and not usuario_bloqueado
print("Acesso concedido?", acesso)

#Exercicio 5 - Divisão de tarefas
conta = 150.00
amigos = 3
valor_pessoa = (conta / amigos)
divisao_exata = conta % amigos == 0 #vai calcular o resto da divisão e verificar se é igual a 0, retornando true.
print("Valor por pessoa:", valor_pessoa)
print("A divisão é exata? ", divisao_exata)

#Exercicio 6 - Classificação Etária
idade_pessoa = int(input("Digite sua idade: "))
classificacao = (idade_pessoa >= 16)
print("Pessoa pode assistir?", classificacao)

#exercicio 7 - Par ou impar

numero_usuario = int(input("Digite um número: "))
if numero_usuario % 2 == 0:
    print("Número: ",numero_usuario)
    print("O número é par")
else:
    print("Número: ",numero_usuario)
    print("O número é impar")