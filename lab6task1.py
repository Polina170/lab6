def is_divis(number):
    return number % 3 == 0
numbr = int(input())
if is_divis(numbr):
    print('Число делится на 3')
else:
    print('Число не делится на 3')