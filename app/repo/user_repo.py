from app.models.user import User
from app.infra.database import connect
import bson
class UserRepository():

    def create(self, user):
        new_user = User(email=f'{user["name"]}@gmail.com', name=user["name"], last_name='Lawley')
        new_user.idade = user["idade"]
        new_user.save()

        new_user._data.update({
            "id": str(new_user.pk)
        })

        return new_user._data
        return self.create_user_dict(new_user)
    
    def create_user_dict(self, new_user: User):
        return {
            "id": str(new_user.pk),
            "name": new_user.name,
            "email": new_user.email,
            "last_name": new_user.last_name,
            "idade": new_user.idade
        }

    def get_by_id(self, id):
        print(type(id))
        user = User.objects(pk=id).first()
        user._data.update({
            "id": str(user.pk)
        })
        return user._data
