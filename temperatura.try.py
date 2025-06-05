

try:
    print("1 - Fahrenheit ---> Celsius ")
    print("2 - Celsius ---> Kelvin ")
    menu = int(input("Digite o código da temperatura a ser convertida: "))
    match menu:
        case 1:
            f= float(input("Digite a temperatura em Fahrenheit: "))
            temp_c = f - 32
            temp_ce = temp_c * 5
            temp_cel = temp_ce / 9
            print(f" {f} é igual a {temp_cel}°C")
        
        case 2: 
            c = float(input("Digite a temperatura em Celsius:"))
            temp_k= c + 273,15
            print(f" {c} é igual a {temp_k}K ")


except ValueError:
    print("Digite um número correto.")
except Exception as e:
    print("Ocorreu um erro inesperado.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ArithmeticError:
    print("Erro na conta aritmética")