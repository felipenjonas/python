# Programa que cria uma lista (vetor) com N elementos,
# Insere o valores neste Array (input ou randit) e em seguida,
# mostrar o MENOR e o maior valor da lista.

numbers_list = [  ]

start = 0
amount = int(input('Digite um valor: \n'))

for item in range(amount):
    start += 1 
    numbers_list.append(start)


print(f'Lista:{numbers_list} \n')

print(f'O Valor mais alto da lista: [ {max(numbers_list)} ]\n')
print(f'O menor valor da lista é: [ {min(numbers_list)} ] \n')





