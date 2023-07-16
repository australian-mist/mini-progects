import random as r


s = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890&_'


while True:
    a = input('\nВыберите действие\n1 - сгенерировать пароль, 2 - задать пароль, 3 - ввести пароль, Q - выйти\n')

    if a == '1':
        n = int(input('Сколько символов добавить в пароль?\n'))
        gen_pas = list(s)
        r.shuffle(gen_pas)
        gen_pas = gen_pas[:(n-1)]

        if ('&' not in gen_pas) and ('_' not in gen_pas):
            gen_pas.append('&')
        else:
            gen_pas.append(''.join(r.sample(s, 1)))

        gen_pas = ''.join(gen_pas)
        print(gen_pas)

    elif a == '2':
        pas = ''.join(input('Введите пароль\n'))
        print('Пароль установлен')

    elif a == '3':
        i = 3
        j = ''
        while i > 0:
            try:
                pas = pas
            except NameError:
                j = 'Пароль не задан'
                break

            print(f'У вас {i} попытка') if i == 1 else print(f'У вас {i} попытки')
            ent_pas = input()

            if ent_pas == pas:
                j = 'Доступ разрешен'
                break
            else:
                i -= 1
                j = 'Доступ запрещен'
        print(j)

    elif a == 'Q':
        break

    else:
        print('Некорректное действие')
        continue
