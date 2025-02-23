from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
import json

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2)])
    pasword = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=4)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


# Список пользователей с их статусами
users = [
    {"id": 1, "name": "Анна", "active": True},
    {"id": 2, "name": "Виктор", "active": False},
    {"id": 3, "name": "Роман", "active": True},
]

# Функция для создания визуального отображения статуса пользователей
def get_user_status(users):
    user_status = {}
    for user in users:
        status_color = "green" if user["active"] else "red"
        user_status[user["name"]] = status_color
    return user_status

# Отправка данных в формате JSON
def send_json(data):
    json_data = json.dumps(data)
    print(json_data)

# Получаем статусы пользователей
user_status = get_user_status(users)

# Отправляем статусы
send_json(user_status)