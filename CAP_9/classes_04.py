#Exercício 9.10

from classes_01 import Restaurante, Sorveteria

rest_01 = Restaurante('Maravilhas Mineiras', 'Tradicional')
rest_01.restaurante_info()
print('~' * 80)

rest_arabe = Restaurante('Sabores Internacional', 'Arabe')
rest_arabe.restaurante_info()
rest_arabe.restaurante_aberto()
rest_italiano = Restaurante('Delicias da Nona', 'Italiana')
rest_japones = Restaurante('SUSHITAKARO', 'Japonesa')
rest_mexicano = Restaurante('Arriba Burritos', 'Mexicana')
sov_01 = Sorveteria('Gostosuras FIT', 'Light')
rest_japones.restaurante_info()
rest_italiano.restaurante_info()
rest_mexicano.restaurante_info()
print('+' *60)
rest_japones.ler_num_servidos()
rest_japones.num_servidos = 1
rest_japones.ler_num_servidos()
rest_japones.set_num_served(3)
rest_japones.ler_num_servidos()
rest_japones.incremeta_num_servidos(2)
rest_japones.ler_num_servidos()
print('+' *60)
sov_01.incremeta_num_servidos (1)
sov_01.get_sabores()
sov_01.ler_num_servidos()