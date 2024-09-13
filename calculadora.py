def calculadora():
    print("Escolha a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")
   
    # Recebendo os números como float para aceitar números decimais  
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
  
    # Verificando a operação escolhida
    if escolha == '1':
       print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif escolha == '2':
       print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif escolha == '3':
       print(f"Resultado: {num1} * {num2} = {num1 * num2}")
    elif escolha == '4':
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Escolha inválida.")
    if ___name___== "___main___":
        calculadora() 
