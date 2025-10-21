#exercício 6.3 glossário

glos = {'int': 'Converte um valor para numero inteiro!',
        'float': 'Converte um valor para numero real!', 
        'str': 'Faz conversão para string!',
        'range': 'Função que gera uma lista de valores inteiros!',
        'lower': 'Funçao que converte caracteres de uma string em minusculas!',
        }
print()
for k, v in glos.items():
    print(f'{k} -> {v}')
print()
# A partir daqui são testes práticos
for f in glos.keys():
    print(f)
print()
for f in sorted(glos.keys()):
    print(f)
print()
linguagens = {'python', 'c', 'java', 'python', 'cobol', 'python', 'c', 'java'}#Cria um conjunto de itens únicos.
print(linguagens)