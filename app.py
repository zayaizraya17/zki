# app.py
from flask import Flask, render_template, request
from password_generator import generate_password

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        # Получаем длину пароля из формы
        length = int(request.form.get('length', 6))
        # Генерируем пароль
        password = generate_password(length)
    # Отображаем страницу с формой и результатом
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)