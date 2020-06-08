

string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
contador = 10
# [string[i:i+contador] primeiro i = primeiro elemento da lista de onde ela vai começar
# [string[i:i+contador] segundo i = aonde ela vai parar + contador que soma o i(0) e contador(10) no proximo laço
# i == 10
# range(0,len(string), contador) = 0 começa do 0, vai até o final da lista, pulando de contador(10) em contador(10)

listcomprehension = [string[i:i+contador] for i in range(0,len(string), contador)]
print(listcomprehension)
retorno = '.'.join(listcomprehension)
print(retorno)