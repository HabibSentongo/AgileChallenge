import uuid
from datetime import datetime 
class User:

    def __init__(self, id, firstname, lastname, username, role,password):
        self.id = int(uuid.uuid4())
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.role = role
        self.password = password

        

    def get_user_details(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'username': self.username,
            'role': self.role,
            'password': self.password



        }
