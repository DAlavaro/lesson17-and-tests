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


# """ Шаг 2 - делаем дамп в словарь """
# user = User(id=1, name='jane', age=19)
# user_schema = UserSchema()
# result = user_schema.dump(user)
# print(type(result))
# print(result["name"])
#
#
# """ Шаг 3 - делаем дамп в строку """
# user = User(id=1, name='jane', age=19)
# user_schema = UserSchema()
# result = user_schema.dumps(user)
# print(type(result))
# print(result)


# """ Шаг 4 - делаем дамп списка """
# user1 = User(id=1, name='jane', age=19)
# user2 = User(id=2, name='jane2', age=19)
# user3 = User(id=3, name='jane3', age=19)
# user4 = User(id=4, name='jane4', age=19)
# user_schema = UserSchema(many=True)
# print(user_schema.dump([user1, user2, user3, user4]))
# print(user_schema.dumps([user1, user2, user3, user4]))


""" Шаг 4 - делаем дессереализацию """
user_json_str = '{"name": "jane", "age": 19}'
user_schema = UserSchema()

user_dict = user_schema.loads((user_json_str))
user = User(**user_dict)
print(user.age)






if __name__ == '__main__':
    app.run()
