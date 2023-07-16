from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance  # для обработки изображений
import os
from datetime import datetime


class App:
    def __init__(self):
        self.root = Tk()

        self.root.title('Photo')
        self.root.geometry('800x610')
        self.root.resizable(False, False)
        self.root.iconphoto(False, PhotoImage(file='img/add.png'))
        self.root['bg'] = 'white'

        self.label = Label(text='\nОбработка изображений', font=('Verdana', 16), bg='white')
        self.label.pack()
        self.canvas = Canvas(height=400, bg='white')
        self.canvas.pack(anchor=CENTER, pady=20)

        self.load = Button(text='Открыть', command=self.open)
        self.load.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.blur = Button(text='Размыть', command=self.effect)
        self.blur.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.sharper = Button(text='Резкость', command=self.sharp)
        self.sharper.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.exit = Button(text='Выход', command=self.ex)
        self.exit.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)

        self.dtime = Label(font=('Verdana', 20), bg='white')
        self.dtime.place(x=310, y=540)
        self.show_time()

        self.cwd = os.getcwd()
        self.image, self.time, self.w, self.h = None, None, None, None
        self.orig = Image.new('RGB', (600, 400), (255, 255, 255))

        self.root.mainloop()

    def open(self):
        try:
            fullpath = filedialog.askopenfilename(title='Выбор картинки', initialdir=self.cwd,
                                                  filetypes=(('GIF', '*.gif'), ('PNG', '*.png'), ('JPG', '*.jpg')))
            self.orig = Image.open(fullpath)
            self.w, self.h = self.orig.size

            if self.w > 600:
                ratio = self.w / 600
                self.orig = self.orig.resize((600, int(self.h / ratio)))
            self.image = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        except AttributeError:
            self.image = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchore=NW, image=self.image)

    def effect(self):
        blur_image = self.orig.filter(ImageFilter.BLUR)
        self.image = ImageTk.PhotoImage(blur_image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    def sharp(self):
        sharper = ImageEnhance.Sharpness(self.orig)
        sharp_image = sharper.enhance(5.0)
        self.image = ImageTk.PhotoImage(sharp_image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    def show_time(self):
        self.time = datetime.time(datetime.now()).strftime("%H:%M:%S")
        self.dtime['text'] = self.time
        self.dtime.after(1000, self.show_time)

    def ex(self):
        self.root.destroy()


App()
