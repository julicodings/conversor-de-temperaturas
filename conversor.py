#converter celsius para F
#converter F para celsius

def celsius_para_farenheit(celsius):
    return (celsius * 9/5) + 32

def fareheit_para_celsius(farenheit):
    return (farenheit - 32) * 5/9

def menu():
    print("--BEM-VINDO AO CONVERSOR DE TEMPERATURA--")
    print("Escolha uma opção:")
    print("1. Converter de Celsius para Farenheit")
    print("2. Converter de Farenheit para Celsius")
    print("3. Sair")

def conversor_temperaturas():
    menu()
    opcao = int(input("Digite a opção desejada (1/2/3): "))

    if opcao == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        celsius_para_farenheit(celsius)
        print(f"A temperatura em Farenheit é: {celsius_para_farenheit(celsius):.2f}")

    elif opcao == 2:
        farenheit = float(input("Digite a temperatura em Farenheit: "))
        fareheit_para_celsius(farenheit)
        print(f"A temperatura em Celsius é: {fareheit_para_celsius(farenheit):.2f}")

    elif opcao == 3:
        print("Saindo do programa...")

    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    conversor_temperaturas()    

