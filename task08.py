'''Задание No8
Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, 
меню, подвал), и дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.'''
from flask import Flask
from flask import render_template # импорт функции отрисовки шаблона

app = Flask(__name__) # создаём приложение (экземпляр класс Flask) и передаём имя запускаемого модуля


@app.route('/') # Декоратор с параметром (url-адресом)
def base():
    return render_template('base.html') # содержимое базовой веб страницы


@app.route('/about/')
def about():
    return render_template('about.html') # содержимое базовой веб страницы


@app.route('/contact/')
def contact():
    return render_template('contact.html') # содержимое базовой веб страницы


if __name__ == '__main__':
    app.run(debug=True)  # используем run()-функцию для запуска локального сервера с нашим приложением