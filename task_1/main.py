from app import app

if __name__ == '__main__':
    print("Запуск веб-сервиса Flask...")
    print("Доступные маршруты:")
    print("  GET /                    — Приветствие")
    print("  GET /hello/<name>        — Персональное приветствие")
    print("  GET /square/<int:number> — Квадрат числа")
    print("  GET /time                — Текущее серверное время")
    print("  GET /repeat/<word>/<n>   — Повтор слова n раз")
    app.run(debug=True, host='127.0.0.1', port=5000)