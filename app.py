# app.py
from flask import Flask, render_template, request
from password_generator import generate_password

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        # получает длинну из формы
        length = int(request.form.get('length', 6))
        # генерация пр
        password = generate_password(length)
    # Отображение страницы
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
