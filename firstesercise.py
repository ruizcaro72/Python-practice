numbers = [1, -5, 8, -2, 7, -7, -3, 4, 9, -10, 8, -6]

print('Numeros')
print(numbers)

for n in range(len(numbers)):
    if numbers[n] < 0:
        numbers[n] = 0

print(numbers)
