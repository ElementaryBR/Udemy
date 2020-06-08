d1 =  {'chave':'valor da chave','cahve2':'Chave2'}
d1['novachave'] = 'Valor da nova chave'

print(d1)

dicionario = {(1,2,3):'Valor tupla', 'str':'Valor da String',123:'Valor do int'}
print(dicionario)
print(dicionario.get('nomedachave'))
print(dicionario[(1,2,3)])

dicionario[123] = 123
print(dicionario)

dicionario.update({'nova_chave':'Novo Valor'})
print(dicionario)

print('Valor tupla' in dicionario.values())
n1 = dicionario.values()
print(n1)
print('str' in dicionario.keys())
n2 = dicionario.keys()
print(n2)

for k in dicionario.values():
    print(k)

for k in dicionario:
    print(k)

for k in dicionario.items():
    print(list(k))

for k, v in dicionario.items():
    print(k, v)

clientes = {
    'cliente1':{
    'nome':'Junior',
    'sobrenome':'Cardoso',
    'idade': 19,
},
    'cliente2':{
    'nome':'Corona',
    'sobrenome':'Covid',
    'idade': 19,
},
'cliente3':{
    'nome':'Bolsonaro',
    'sobrenome':'Atleta',
    'idade': 200,
    }
}

for cliente_k,cliente_v in clientes.items():
    print(f'Exibindo Informações: {cliente_k}')
    for dados_k, dados_v in cliente_v.items():
        print(f'\t{dados_k} = {dados_v}')
