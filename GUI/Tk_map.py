from tkinter import *
import requests
from io import BytesIO
from PIL import Image, ImageTk


class App:
    def __init__(self):
        self.root = Tk()

        self.root.title('Map')
        self.root.geometry('800x600')
        self.root.resizable(False, False)
        self.root.iconphoto(False, PhotoImage(file='img/map.png'))

        self.canvas = Canvas(height=20)
        self.canvas.pack()
        self.label = Label(text='Поиск по карте', font=('Verdana', 16))
        self.label.pack()
        self.canvas = Canvas(width=500, height=450)
        self.canvas.pack(anchor=CENTER, pady=20)

        self.finder = Button(text='Найти', command=self.find)
        self.finder.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.plus = Button(text='+', command=self.big)
        self.plus.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.minus = Button(text='-', command=self.small)
        self.minus.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.place = Entry(width=60, font=('Verdana', 12))
        self.place.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)

        self.image = None  # заглушка
        self.delta = '0.005,0.005'

        self.root.mainloop()

    def find(self):
        name = self.place.get()
        apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
        api_server = 'https://static-maps.yandex.ru/1.x/'

        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={name}&kind=metro&format=json"
        resp = requests.get(geocoder_request).json()
        r = ','.join(resp["response"]['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split())

        # Собираем параметры для запроса к static-maps
        map_param = {
            'll': r,
            'spn': self.delta,
            'l': 'map',
            'pt': f'{r},pm2dgl'
        }

        pict = Image.open(BytesIO(requests.get(api_server, params=map_param).content))
        self.image = ImageTk.PhotoImage(pict)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    def big(self):
        self.delta = f"{float(self.delta.split(',')[0]) / 2},{float(self.delta.split(',')[1]) / 2}"
        self.find()

    def small(self):
        self.delta = f"{float(self.delta.split(',')[0]) * 2},{float(self.delta.split(',')[1]) * 2}"
        self.find()


App()
