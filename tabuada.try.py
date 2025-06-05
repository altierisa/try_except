
try:
    numero = int(input('Digite o numero para a tabuada > '))
    i = int(input('Digite o multiplicando:'))
    fim = int(input('Digite o multiplicador:'))
    while i <= fim:
        print(f' {i} x {numero} = {i * numero}')
        i += 1 

except ValueError:
    print("Digite um número correto.")
except Exception as e:
    print("Ocorreu um erro inesperado.")
except ArithmeticError:
    print("Erro na conta aritmética")