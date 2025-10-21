#Exercício 5.10

usuarios_correntes = ['pedro', 'maria', 'admin', 'marcos']
novos_usuarios = ['maria', 'manoel', 'marina']

if usuarios_correntes:
    if novos_usuarios:
        for novo_usuario in novos_usuarios:
            if novo_usuario.lower() in usuarios_correntes:
                print(f'{novo_usuario} já está em uso, por favor tente outro!') 
            else:
                usuarios_correntes.append(novo_usuario)
                print(f'{novo_usuario} cadastrado com sucesso!')
    else:
        print('Nenhum novo usuário cadastrado!')
print(usuarios_correntes)