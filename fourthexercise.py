list = []
listreverse = []
size = 20

print('Ingrese 20 numeros de forma aleatoria')

for i in range(size):
    num = int(input('Ingrese un numero del 1 al 10: '))
    if num >= 0 and num < 10:
        list.append(num)
    else:
        print('Ingrese numeros del 1 al 10')

print(list)

for item in list[::-1]:
    listreverse.append(item)
print(listreverse)