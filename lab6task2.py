def divide(a):
    return 100 / a
number = input("Введите число на которое хотите поделить 100: ")
try:
    numbr = float(number)
    if numbr != 0:
        res = divide(numbr)
        print(res)
    else:
        print("На ноль делить нельзя")
except:
    print('Ошибка!')