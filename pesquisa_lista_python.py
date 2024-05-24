
nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joana', 'Maria', 'Mariana', 'João','Mariana',
               'Giscard','Michelle','Giscard','Frederico','Márcia','Carla','Clarissa']

for nome in nomes_lista:
    print(nome)

nome = input('Digite o nome a ser pesquisado: ').capitalize()

try:
    indice = nomes_lista.index(nome)
    quantidade = nomes_lista.count(nome)
    print(f'Nome encontrado: {nome} {quantidade} vez(es) no índice {indice}')
except:
    print(f'{nome} não encontrado na lista.')
