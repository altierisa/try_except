

try:
    peso = float(input('Digite o seu peso: '))
    altura = float(input('Digite a sua altura: '))
    imc = peso / altura ** 2
    if imc <= 18.5:
        print(f' IMC {imc} indica peso abaixo do normal.⚠️')
    elif 18.5 < imc <= 24.9:
        print(f' IMC {imc} indica Eutrofia.✅')
    elif 24.9 < imc <= 29.9:
        print(f' IMC {imc} indica Sobrepeso.⚠️')
    elif 29.9 < imc <= 34.9:
        print(f' IMC {imc} indica Obesidadde grau I.🚨')
    elif 34.9 < imc <= 39.9:
        print(f' IMC {imc} indica Obesidade grau II.🚨')
    else:
        print(f' IMC {imc} indica Obesidade grau III (MÓRBIDA)🚨.')

except ValueError:
    print("Digite um número correto.")
except Exception as e:
    print("Ocorreu um erro inesperado.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ArithmeticError:
    print("Erro na conta aritmética.")
            