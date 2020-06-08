perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2 ?: ',
        'respostas': {'a': '1','b': '4','c': '15','d': 'Peixe'},
        'resposta_certa': 'b'},

    'Pergunta 2':{
        'pergunta': 'Quanto é 2 + 5 ?: ',
        'respostas': {'a': '7','b': '4','c': '15','d': 'Peixe'},
        'resposta_certa': 'a'}
}

quantidade_de_acertos = 0
for perg, pergunta in perguntas.items():
    print(f'\n{perg} : {pergunta["pergunta"]}')
    print('Respostas:')
    for valores, respos in pergunta['respostas'].items():
        print(f'[{valores}] = {respos}')

    print()
    respostas = input('Digite sua resposta: ')
    if respostas == pergunta['resposta_certa']:
        quantidade_de_acertos +=1
        print('Acertou Miseravii')
    else:
        print('ERRROOOOOOU')

try:
    porcentagem_acerto_respostas = quantidade_de_acertos / len(perguntas) * 100
    print(f'\nAcertou: {porcentagem_acerto_respostas:.0f}% das perguntas')
except ZeroDivisionError:
    print('\nErrou tudo, pelo amor dos meu filhinho')

