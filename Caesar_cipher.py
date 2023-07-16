n = int(input('\nВведите коэффициент шифра: '))

while True:
    m = int(input('\nВыберите действие:\n1 - закодировать\n2 - раскодировать\n0 - выйти\n'))

    if m == 0:
        break

    elif m == 1:
        str_old = input('Введите текст: ')
        str_new = ''

        for i in str_old:
            i = chr(ord(i) + n)
            str_new = str_new + i

        print('Шифр текста:', str_new)

    elif m == 2:
        str_old = input('Введите текст: ')
        str_new = ''

        for i in str_old:
            i = chr(ord(i) - n)
            str_new = str_new + i

        print('Исходный текст:', str_new)

    else:
        print('Ошибка')
