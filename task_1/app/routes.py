from flask import jsonify
from datetime import datetime
from app import app

@app.route('/')
def index():
    return "Добро пожаловать в Flask-сервис!"

@app.route('/hello/<name>')
def hello(name):
    return f"Привет, {name}!"

@app.route('/square/<int:number>')
def square(number):
    result = number ** 2
    return f"Квадрат числа {number} равен {result}."

@app.route('/time')
def server_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Текущее серверное время: {current_time}"

@app.route('/repeat/<word>/<int:n>')
def repeat_word(word, n):
    if n < 0:
        return "Ошибка: количество повторений должно быть неотрицательным.", 400
    result = " ".join([word] * n)
    return f"Результат повторения слова '{word}' {n} раз(а): {result}"