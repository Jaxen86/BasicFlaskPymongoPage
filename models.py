from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, object):
        self.email = object["email"]
        self.first_name = object["first_name"]
        self.last_name = object["last_name"]
        self.password = object["password"]
        self._id = str(object["_id"])

    def get_id(self):
        return self.email

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name


