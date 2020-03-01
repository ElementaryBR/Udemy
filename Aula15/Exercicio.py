while True:
    print('#'*50,'\n','\t'*4,'Calculadora\n','#'*50,sep='')
    n1 = int(input('\nDigite um numero: '))
    n2 = int(input('\nDigite outro numero: '))
    operador = input('\nDigite um operador para o calculos [+,-,*,/]: \n')

    if operador == '+':
        resultado = n1 + n2
        print(resultado)
    elif operador == '-':
        resultado = n1 - n2
        print(resultado)
    elif operador == '*':
        resultado = n1 * n2
        print(resultado)
    elif operador == '/':
        resultado = n1 / n2
        print(resultado)

    sair = input('Deseja sair? [s/n]: ')
    if sair == 's' or sair == 'S' or sair == 'Sim' or sair == 'sim' or sair == 'SIM':
        break