num1 = input("Digite o primeiro número")
num2 = input("Digite o segundo número")

try:
    num1 = int(num1)
    num2 = int(num2)
    print(F"a soma resulta em: {num1 + num2} ")
except:
    print("Digite um número correto!")