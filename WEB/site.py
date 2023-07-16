from flask import Flask, request, render_template
import json


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная')


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', title='Счетчик', number=3)


@app.route('/poster')
def poster():
    return render_template('poster.html', title='Постер')


@app.route('/queue')
def queue():
    return render_template('queue.html', title='Очередь')


@app.route('/news')
def news():

    with open("static/news.json", "rt", encoding="utf-8") as f:
        news_list = json.loads(f.read())

    return render_template('news.html', title='Новости', news=news_list)


@app.route('/carousel')
def carousel():
    return render_template('carousel.html', title='Карусель')


@app.route('/form', methods=['GET', 'POST'])
def form():

    if request.method == 'GET':
        return render_template('form.html', title='Форма')

    elif request.method == 'POST':
        # f = request.img['file']  # request.form.get('file')
        # f.save('static/loaded.png')

        my_form = request.form.to_dict()

        return render_template('form_show.html', title='Ваши данные', data=my_form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
