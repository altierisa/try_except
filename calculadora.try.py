

print("1 - Adição")
print("2 - Subtração")
print("3 - Potenciação")
print("4 - Multiplicação")
print("5 - Divisão")

menu = int(input("Digite o código da conta que deseja executar"))

try:
    match menu:
        case 1:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            adicao = num1 + num2
            print("A soma resulta em: ", adicao)
        case 2:
            num3 = float(input("Digite o primeiro número: "))
            num4 = float(input("Digite o segundo número: "))
            subtracao = num3 - num4
            print("A soma resulta em: ", subtracao)
        case 3:
            num5 = float(input("Digite o primeiro número: "))
            num6 = float(input("Digite o segundo número: "))
            potencia = num5 ** num6
            print("A soma resulta em: ", potencia)
        case 4:
            num7 = float(input("Digite o primeiro número: "))
            num8 = float(input("Digite o segundo número: "))
            multi = num7 * num8
            print("A soma resulta em: ", multi)
        case 5:
            num9 = float(input("Digite o primeiro número: "))
            num0 = float(input("Digite o segundo número: "))
            div = num9 / num0
            print("A soma resulta em: ", div)
except ValueError:
    print("Digite um número correto.")
except Exception as e:
    print("Ocorreu um erro inesperado.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ArithmeticError:
    print("Erro na conta aritmético.")
            
