cpf = '094.843.269-19'

cpf_separado = cpf[:11].strip().split('.')
cpf_editado = []
for numero in cpf_separado:
    for valor in numero:
        valor = int(valor)
        cpf_editado.append(valor)
print(cpf_editado)
calculator = []
contador = 10
for numero in cpf_editado:
    numero = int(numero)
    print(f'A multiplicação entre: {numero} e :{contador} é igual a: {numero*contador}')
    calculo = numero * contador
    print(calculo)
    calculator.append(calculo)
    contador -= 1
print(calculator)
resultado = sum(calculator)
print(resultado)
validador = 11 - (resultado % 11)
if validador > 9 :
    digito1 = validador
    cpf_editado.append(digito1)
elif validador < 9:
    digito1 = validador
    cpf_editado.append(digito1)

print(cpf_editado)

calculator = []
contador = 11
for numero in cpf_editado:
    numero = int(numero)
    print(f'A multiplicação entre: {numero} e :{contador} é igual a: {numero * contador}')
    calculo = numero * contador
    calculator.append(calculo)
    contador -= 1
resultado = sum(calculator)
validador = 11 - (resultado % 11)
cpf_editado.append(validador)
lista_final = []
for valor in cpf_editado:
    valor = str(valor)
    lista_final.append(valor)
lista_final = ''.join(lista_final)
cpf_final = []

print(lista_final)

if lista_final == cpf:
    print('Deu Boa Conseguiu gurizao')

