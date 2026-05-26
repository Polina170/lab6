def is_magic(a):
    day, month, year = a.split('.')
    day = int(day)
    month = int(month)
    year = int(year)
    lasttnums = year % 100
    if day * month == lasttnums:
        return True
    else:
        return False
date = input("Введите дату. Пример: 01.01.2001: ")
if is_magic(date):
    print("эта дата магическая")
else:
    print('Это обычная дата')