import random
import string

def generate_password_from_id(user_id):
    # Определение алфавитов
    uppercase_letters = string.ascii_uppercase  # Заглавные буквы (A-Z)
    lowercase_letters = string.ascii_lowercase  # Строчные буквы (a-z)
    digits = string.digits  # Цифры (0-9)
    special_chars = '!"#$%&\'()*'  # Специальные символы

    # Генерация пароля по требованиям
    p1 = random.choice(uppercase_letters)  # Случайная заглавная буква
    p2 = str(len(user_id) % 10)  # Остаток от деления длины user_id на 10
    p3 = random.choice(digits)  # Случайная цифра
    p4 = random.choice(special_chars)  # Случайный специальный символ
    p5 = random.choice(lowercase_letters)  # Случайная строчная буква
    p6 = random.choice(digits)  # Случайная цифра

    # Сборка пароля
    password = p1 + p2 + p3 + p4 + p5 + p6
    return password

# Основная программа
if __name__ == "__main__":
    # Запрос идентификатора пользователя
    user_id = input("Введите идентификатор пользователя: ")

    # Генерация пароля
    password = generate_password_from_id(user_id)

    # Вывод пароля
    print("Сгенерированный пароль:", password)

    # Ожидание завершения (для Windows)
    input("Нажмите Enter для выхода...")