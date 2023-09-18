'''Задание No1
Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".'''

from flask import Flask
from flask import render_template # импорт функции отрисовки шаблона

app = Flask(__name__) # создаём приложение (экземпляр класс Flask) и передаём имя запускаемого модуля

@app.route('/') # Декоратор с параметром (url-адресом)
def hello_world():
    return 'Hello World!' # содержимое веб страницы

'''Задание No2
Добавьте две дополнительные страницы в ваше веб-приложение:
○ страницу "about" 
○ страницу "contact".'''
@app.route('/about/')
def about():
    return 'About me'

@app.route('/contact/')
def contact():
    return 'My contact'

'''Задание No3
Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.'''
@app.route('/number/<int:one>/<int:two>/')
def summary(one: int, two: int): # принимает 2а числа навход и возвращает сумму
    return f'Результат: {one + two}'

'''Задание No4
Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.'''
@app.route('/string/<string:text>/') 
def len_text(text: str):
    return f'{len(text)}'

'''Задание No5
Написать функцию, которая будет выводить на экран HTML страницу с заголовком 
"Моя первая HTML страница" и абзацем "Привет, мир!".'''
@app.route('/index/')
def html_index():
    return render_template('index.html') # index.html должен находится в папке temlates на одном уровне с приложением 

'''Задание No6
Написать функцию, которая будет выводить на экран HTML страницу с таблицей, 
содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через контекст.'''
@app.route('/students/')
def students_table():
    head = {'firstname':'Имя','lastname':'Фамилия', 'age':'Возраст', 'rating':'Средний бал'}
    # список словарей данных о студентах
    students = [{'firstname':'Михаил','lastname':'Ломоносов', 'age':24, 'rating':98}, 
                {'firstname':'Исаак','lastname':'Ньютон', 'age':22, 'rating':99}]
    # context = {'students': _students}
    return render_template('index.html', **head, students=students)
    # return render_template('index.html', **head, **context) #пробасываем аргументы head и students в шаблон index.html

'''Задание No7
Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через контекст.'''
@app.route('/news/')
def content():
    news_block = [{'title': 'article_1', 'description': 'text1', 'data': 'data1'},
                  {'title': 'article_2', 'description': 'text2', 'data': 'data2'},
                  {'title': 'article_3', 'description': 'text3', 'data': 'data3'}]
    return render_template('news.html', news_block=news_block)
    
'''Задание No8
Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, 
меню, подвал), и дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.'''


if __name__ == '__main__':
    app.run(debug=True)  # используем run()-функцию для запуска локального сервера с нашим приложением