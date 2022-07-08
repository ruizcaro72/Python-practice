num1 = int (input ('Ingresa un numero : '))
num2 = int (input ('Ingresa un numero : '))
num3 = int (input ('Ingresa un numero : '))
num4 = int (input ('Ingresa un numero : '))
num5 = int (input ('Ingresa un numero : '))

if (num1-num2)*(num1-num2)<(num1-num3)*(num1-num3):
    cercano=num2
else:
    cercano=num3
if (num1-num4)*(num1-num4)<(num1-cercano)*(num1-cercano):
    cercano=num4
if (num1-num5)*(num1-num5)<(num1-cercano)*(num1-cercano):
    cercano=num5

print ('El numero mas cercano al primero es: ' + str(cercano))