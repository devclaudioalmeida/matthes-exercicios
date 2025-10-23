#Pratica extra usando a instrução "continue" com o "while"
#Imprime os numeros parer na tela entre 1 e 20

num = 0
while num < 20:
    num += 1
    if num % 2 != 0:
        continue
    print(num)