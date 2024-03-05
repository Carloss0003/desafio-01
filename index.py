def continueProgram():
    continueConfirm = input('Deseja continuar? s/n ')

    if continueConfirm == 's':
        startProgram()
    elif continueConfirm == 'n':
        return
    else:
       continueProgram()

def handleUserError():
    print()
    print('Por favor, apenas números serão aceitos')
    print()

def handleCalculateAreaTriangle():
    try:
        base = float(input('Qual a base do triangulo? '))
        heigth = float(input('Qual a altura? '))
        area = float(base * heigth / 2)
        print(f'A area do triangulo de base: {base} e altura {heigth} é igual: {area}')
        print()
        continueProgram()
    except ValueError:
        handleUserError()
        handleCalculateAreaTriangle()
    

def handleCalculateAreaSquare():
    try:
        length = float(input('Qual o comprimento do lado do quadrado? '))
        area = length **2
        print()
        print(f'A área do quadrado é igual: {area}')
        print()
        continueProgram()
    except ValueError:
        handleUserError()
        handleCalculateAreaSquare()

def handleCalculatePerimeterTriangle():
    try:
        side_a = float(input('Qual o comprimento do lado A do triangulo? '))
        side_b = float(input('Qual o comprimento lado b? '))
        side_c = float(input('Qual o comprimento lado c? '))

        perimeter = side_a + side_b + side_c
        print()
        print(f'O perimetro do triangulo é igual: {perimeter}')
        print()
        continueProgram()
    except ValueError:
        handleUserError()
        handleCalculatePerimeterTriangle()

def handleCalculatePerimeterSquare():
    try:
        width = float(input('Qual comprimento do lado do quadrado? '))
        perimeterSquare = width + width + width + width
        print()
        print(f'O perimetro do quadrado é igual: {perimeterSquare}')
        print()
        continueProgram()
    except ValueError:
        handleUserError()
        handleCalculatePerimeterSquare()

def startProgram():
    print()
    print('Selecione a operação')
    print()
    print('1: área do Triangulo')
    print('2: Área do quadrado')
    print('3: perimetro do triangulo')
    print('4: perimetro do quadrado')
    print()
    option = input('O que iremos calcular? ')
    print()
    if option == '1':
        handleCalculateAreaTriangle()
    elif option == '2':
        handleCalculateAreaSquare()
    elif option == '3':
        handleCalculatePerimeterTriangle()
    elif option == '4':
        handleCalculatePerimeterSquare()
    else:
        print()
        print('Cuidado, está opção não existe e pode acabar não gerando o resultado que deseja')
        print()
        startProgram()

print('Neste programa você poderá calcular a area e o perimetro do quadrado e do triangulo.')
print()
startProgram()