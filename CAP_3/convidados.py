#Exercícios práticos do livro 3.4, 3.5, 3.6 e 3.7
convidados = list()
convidados.append('Antônio')
convidados.append('José Alexandre')
convidados.append('Luana')
print(f'Lista de convidados: {convidados}')#solução do 3.4 até aqui
nao_pode = 'Luana'
convidados.remove('Luana')
novo_convidado = 'Marina'
convidados.append(novo_convidado)
print(f'O convidado(a) {nao_pode} não comparecerá! Foi convidado(a) {novo_convidado} para seu lugar!')
print(f'Lista de convidados atualizada: {convidados}')#solução do 3.5 até aqui
print('Foi convidado o Cássio!')
convidados.append('Cássio')
print(f'Lista de convidados atualizada: {convidados}')
print('Foi convidada a Nathalia!')
convidados.insert(3, 'Nathalia')
print(f'Lista de convidados atualizada: {convidados}')
print('Foi convidada a Thaís!')
convidados.insert(3, 'Thaís')
print(f'Lista de convidados atualizada: {convidados}')#Solução do 3.6 até aqui
print('Hove um imprevisto, lamento não poder convida-la Thaís!')
convidados.remove('Thaís')
print(f'Lista de convidados atualizada: {convidados}')
print('Hove um imprevisto, lamento não poder convida-lo Cássio!')
convidados.pop()
print(f'Lista de convidados atualizada: {convidados}')
print('Hove um imprevisto, lamento não poder convida-la Nathalia!')
convidados.pop()
print(f'Lista de convidados atualizada: {convidados}')
print('Hove um imprevisto, lamento não poder convida-la Marina!')
convidados.pop()
print(f'Lista de convidados atualizada: {convidados}')
print('tudo finalizado!')
del convidados[1]
del convidados[0]
print(f'Lista de convidados atualizada: {convidados}')#solução do 3.7 até aqui


