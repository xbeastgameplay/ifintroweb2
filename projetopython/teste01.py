print("olá, mundo, testando python")


nome = input("Digite seu nome: ") 
print("olá", nome , "seja bem vindo")

#Variáveis e tipos básicos
nome2 = "Maria"
idade = 25
altura = 1.68
esta_estudando = True

print(nome2,idade,altura,esta_estudando)

#soma de dois números
num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))

soma = num1 + num2
print("A soma é igual a", soma)

numero = int(input("Digite um número"))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é impar.")