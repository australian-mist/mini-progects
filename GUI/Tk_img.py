from tkinter import *  # WEB - Graphics User Interface


status = True


class Open:
    def __init__(self):
        self.win = Tk()  # Инициализация WEB

        self.win.title('Tkinter')
        self.win.geometry('400x300')
        self.win.resizable(False, True)
        self.win.iconphoto(False, PhotoImage(file='img/img.png'))

        self.img = None
        self.canvas = Canvas(height=10)
        self.canvas.pack()
        self.lbl = Label(text='Press button', background='#b3c5a5')
        self.lbl.pack()
        self.canvas = Canvas(height=10)
        self.canvas.pack()
        self.canvas = Canvas(height=210, width=200)
        self.canvas.pack()
        self.btn = Button(text='Show', command=self.click)
        self.btn.pack()

        self.win.mainloop()

    def click(self):
        global status

        if not status:
            self.lbl['text'] = 'Press button'
            self.lbl['background'] = '#b3c5a5'
            self.btn['text'] = 'Show'
            self.canvas.delete('all')

        else:
            self.lbl['text'] = 'Button was pressed'
            self.lbl['background'] = '#b3c5c5'
            self.btn['text'] = 'Clear'
            self.img = PhotoImage(file='img/mew.png')
            self.canvas.create_image(100, 100, image=self.img)

        status = not status  # Инверсия булевой переменной


Open()
