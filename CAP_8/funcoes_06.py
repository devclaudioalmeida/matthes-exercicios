from funcoes_05 import make_car, build_profile
import funcoes_04 as F4

car = make_car('Fiat', 'Fastback', ano=2023, cor='preto')
print(car)
print('^' * 80)
usuario = build_profile('Cláudio', 'Almeida', idade=39, sexo='M', profissao='Desenvolvedor')
print(f'Informações do usuário: {usuario}')
print('^' * 80)
carro = make_car('VW', 'Fusca', ano_fab=1979, ano_mod=1980, cor='amarelo', cilindrada=1600)
print(f'Informações do veículo: {carro}')
print('^' * 80)

F4.sandwiches('salame', 'queijo', 'pimentão', 'presunto', 'ovo', 'salsicha', 'alface', 'cogumelo', 'rapadura')