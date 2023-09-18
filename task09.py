'''Задание 9
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.'''

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/main')
def main():
    context = {'title': 'Главная'}
    return render_template('fashion_main.html', **context)

@app.route('/clothing/')
def clothing():
    context = {'title': 'Одежда'}
    return render_template('fashion_clothing.html', **context)

@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('fashion_shoes.html', **context)

@app.route('/jewerly/')
def jewerly():
    context = {'title': 'Украшения'}
    return render_template('fashion_jewerly.html', **context)


if __name__ == '__main__':
    app.run(debug=True)