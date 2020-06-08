variavel = 'valor'

print(variavel)


def func():
    print(variavel)


def func2():
    variavel = 'Outro valor'
    print(variavel)


func()
func2()
print(variavel)


def func2():
    global variavel # Não é uma boa pratica de programação
    variavel = 'Outro valor'
    print(variavel)

func2()
print(variavel)


def teste():
    variavel = 'Junior'
    return variavel

def outro_teste(argumento):
    print(argumento)

var = teste()
outro_teste(var)