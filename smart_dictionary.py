import os
import pickle


book = 'dictionary.bin'

if not os.path.isfile(book):
    with open(book, 'wb') as f:
        d = {'стол': 'table', 'стул': 'chair'}
        pickle.dump(d, f)

else:
    with open(book, 'rb') as f:
        d = pickle.load(f)

    while True:

        w = input('\nВведите слово (или Q для выхода)\n')

        if w in d:
            print(d[w])

        elif w == 'Q':
            break

        else:
            n_w = input('Я не знаю этого слова, введите перевод\n')
            d[w] = n_w

    with open(book, 'wb') as f:
        pickle.dump(d, f)
