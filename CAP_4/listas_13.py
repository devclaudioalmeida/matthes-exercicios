#exercício 4.13 Buffet
refeicoes = ('arroz', 'feijão', 'frango', 'linguiça', 'salada') #Atribui essa tutla para a variavel refeicoes!
for refeicao in refeicoes:
    print(refeicao)
#refeicoes[1] = 'lombo' #tuplas são imutáveis, assim gera erro!
print(f'Tupla original de refeições: {refeicoes}')
refeicoes = ('churrasco', 'sushi', 'esfirra', 'pizza', 'canelone') #Posso atribuer uma nova tupa a variável refeicoes que não gera erro!
print(f'Nova tupla de refeições: {refeicoes}')