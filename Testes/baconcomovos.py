'''

1 - Receber um numero inteiro
2 - Saber se o numero é multiplo de 3 e 5:
    Bacon com Ovos
3 -  Saber se o numero é multiplo somente de 3:
    Bacon
4 -  Saber se o numero é multiplo somente de 5:
    Ovos
5 -  Saber se não é multiplo nem de 3 e nem de 5:
    Passar Fome
'''

def bacon_com_ovos(numero_inteiro):
    assert isinstance(numero_inteiro, int),'numero passado deve ser int'

    if numero_inteiro % 3 == 0 and numero_inteiro % 5 ==0:
        return 'Bacon com Ovos'

    if numero_inteiro % 3 == 0:
        return 'Ovos'

    if numero_inteiro % 5 ==0:
        return 'Bacon'
    else:
        return 'Passar Fome'