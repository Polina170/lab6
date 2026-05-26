def lucky(a):
    half = len(a)//2
    firstHalf = a[:half]
    secondHalf = a [half:]
    first = 0
    for i in firstHalf:
        first = first + int(i)
    second = 0
    for i in secondHalf:
       second = second + int(i)
    if first == second:
        return True
    else:
        return False
ticket = (input("Введите номер билета: "))
if lucky(ticket):
    print('Этот билет счастливый!')
else:
    print('Этот билет обычный')