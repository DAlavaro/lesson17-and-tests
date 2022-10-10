"""Шаг 0 - готовимся """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column


""" Шаг 1 - составляем схему """


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    age = fields.Int()


""" Шаг 2 - делаем дамп в словарь """
user = User(id=1, name='jane', age=19)
user_schema = UserSchema()
result = user_schema.dump(user)
print(type(result))
print(result["name"])



if __name__ == '__main__':
    app.run()
