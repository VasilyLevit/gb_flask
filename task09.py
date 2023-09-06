'''Задание 9
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.'''

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('fashion_base.html')

@app.route('/clothing/')
def clothing():
    return render_template('fashion_clothing.html')

@app.route('/shoes/')
def shoes():
    return render_template('fashion_shoes.html')

@app.route('/jewerly/')
def jewerly():
    return render_template('fashion_jewerly.html')


if __name__ == '__main__':
    app.run(debug=True)