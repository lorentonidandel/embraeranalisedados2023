
# nome = input("Qual seu nome?")
# print(nome)

#Pergunte ao usuario quantos anos ele tem

# idade = int( input("Quantos anos vocÊ tem?"))

# maioridade = idade >=18
# print(maioridade)

# numero = int( input("Digite um numero: ") )
# doisDigitos = numero >= 10 and numero <= 99
# print(doisDigitos)


# nota1 = float(input("Digite a primeira nota"))
# nota2 = float(input("Digite a segunda nota"))
# nota3 = float(input("Digite a terceira nota"))
# media = (nota1 + nota2 + nota3)/3

# if media >= 7:
#     print("Aprovado")
# else: 
#     print("Reprovado")

# anoNascimento = int(input("Digite o seu ano de nascimento: "))
# idade = 2023 - anoNascimento

# if idade == 18:
#     print("O usuário fará ou fez 18 anos este ano.")



# idade = int(input("Digite a sua idade: "))

# if idade >= 0 and idade <= 11:
#     print("Criança")

# elif idade >= 12 and idade <= 18:
#     print("Adolescente")

# elif idade >= 19 and idade <= 24:
#     print("Jovem")

# elif idade >= 25 and idade <= 40:
#     print("Adulto")

# elif idade >=41 and idade <= 60: 
#     print("Meia Idade")

# elif idade > 60:
#     print("Idoso")


# primeiroValor = int( input("Digite um valor: "))
# segundoValor = int( input("Digite um valor: "))
# print( "Primeiro" if primeiroValor > segundoValor else "Segundo")

# nome = input("Digite o seu nome: ")
# print(f"Olá {nome}")

# mensagem = input("Digite uma mensagem: ")
# print(mensagem.upper ())

# idade = input("Digite sua idade: ")
# if idade.isdigit():
#     print(f"Você tem {idade} anos.")
# else:
#     print("Você digitou uma idade inválida")

# nomeCompleto = input("Digite seu nome completo: ")
# nomeCompletoDividido = nomeCompleto.split(" ")
# print(nomeCompletoDividido[1])

# familia = ("Loren, Gucci, Alex, Aline")
# print(familia)

# cidades = []
# cidade = input("Digite o nome da primeira cidade: ")
# cidades.append(cidade)

# cidades.append(input("Digite o nome da segunda cidade: "))

# cidades.append(input("Digite o nome da terceira cidade: "))
# print (cidades)

# numeros = [1,3,6,10,5,23]
# numeroDigitado = int(input("Digite um número: "))
# if numeroDigitado in numeros:
#     print(f"O número {numeroDigitado} está na lista")
# else:
#     print(f"O número {numeroDigitado} não está na lista")

# nomes = []
# nomes.append(input("Digite o primeiro nome: "))
# nomes.append(input("Digite o segundo nome: "))
# nomes.append(input("Digite o terceiro nome: "))
# nomes.append(input("Digite o quarto nome: "))
# nomes.append(input("Digite o quinto nome: "))

# posicaoParaExcluir = int( input("Escolha uma posição de 0(zero) até quatro(4) para excluir da lista: "))
# del nomes[posicaoParaExcluir]
# print(nomes)


# itensCompra = ["Arroz", "Leite", "Ovos", "Feijão", "Tomate"]
# for item in itensCompra:
#     print(item)
 
# for numero in range(1,11):
#     if numero % 2 == 0:
#         print(numero)

# for numero in range(51,101,2):
#     print(numero)

numeros = []
for numeros in range(10):
    itemDigitado = int (input("Digite um valor: "))
    if(itemDigitado % 2 ==0):
        itemDigitado += 1
    numeros.append(itemDigitado)

for numero in numeros:
    print(numero)