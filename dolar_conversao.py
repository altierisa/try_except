
try:
    real = float(input("Digite o valor em reais a ser convertido para dolar: R$"))
    dolar = real / 5.58
    dolar = real / 5.58
    print(f" R${real} convertido para dolar é:U$D {dolar}")
except ValueError:
    print("Digite um número válido.")
except Exception as e:
    print("Ocorreu um erro inesperado.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ArithmeticError:
    print("Erro na conta aritmética")