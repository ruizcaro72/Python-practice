list1 = []
list2 = []
list3 = []
size = 10

print('Ingrese 10 numeros')
for i in range(size):
    numero = int(input('Numero: '))
    list1.append(numero)
    if numero % 2 == 0:
        list2.append(numero)
    else:
        list3.append(numero)

print('Lista principal')
print(list1)
print('Numeros pares')
print(list2)
print('Numeros impares')
print(list3)


