#Resolução dos exercícios 8.9, 8.10 e 8.11

def show_messages(mensagens):
    """Escreve uma mensagem na tela"""
    for msg in mensagens:
        print(msg) 

def envia_messages(mensagens, mensagens_enviadas):
    """Imprime uma mensagem e move para uma lista de mensagens enviadas"""    
    while mensagens:
        atual = mensagens.pop()
        print(f'mensagem enviada: {atual}')
        mensagens_enviadas.append(atual)


textos = ['Olá, como vai?', 'Tudo bem com você?', 'Em que posso ajudar?', 'Em que posso servir?']
enviadas = []
print('=' * 70)
print(textos)
print(enviadas)
print('=' * 70)
show_messages(textos)
envia_messages(textos[:],enviadas)
print('=' * 70)
print(textos)
print(enviadas)