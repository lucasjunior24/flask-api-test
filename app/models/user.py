from mongoengine import Document, StringField, IntField

class User(Document):
    email = StringField(required=True)
    name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    idade = IntField(max_length=50)