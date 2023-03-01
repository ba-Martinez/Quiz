# Solicita um número do usuário
num = int(input("Digite um número inteiro: "))

# Define os dois primeiros valores da sequência
a, b = 0, 1

# Loop para calcular a sequência de Fibonacci
while b <= num:
    if b == num:
        print(f"{num} pertence à sequência de Fibonacci.")
        break
    a, b = b, a + b
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
