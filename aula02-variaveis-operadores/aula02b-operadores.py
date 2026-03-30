from operator import truediv

num1 = 5
num2 = 2

print(type(num1), type(num2))

resultado_operação = num1 / num2
print(resultado_operação, type(resultado_operação))

#operadores de atribuição

num = 15
print() #pular linha
print(num)

num = 15 + 2 #acumulando 2 em um
print(num)

num += 2
print(num)

# Operadores RELACIONAIS

print(6 <= 7)

idade = 20
print(idade ==10)  #booleano

logado = True
print(logado, type(logado))


maior_idade = idade >=18
print(maior_idade, type(maior_idade))

# STRING

nome1 = "Marcos"
nome2= "marcos"

print(nome1.upper() == nome2.upper())