import json
from flask import request

from login import User
from login.User import User


class Authentication:

    def login(self):
        user_data = json.loads(request.data)
        print(user_data)
        username = user_data['username']
        password = user_data['password']
        result = User.try_login(username, password)
        return result

    def signup(self):
        user_data = json.loads(request.data)
        print(user_data)

        cn = user_data['cn']
        givenName = user_data['givenName']
        sn = user_data['sn']
        telephoneNumber = user_data['telephoneNumber']
        userPassword = user_data['userPassword']

        result = User.try_signup(cn=cn,
                                 givenName=givenName,
                                 sn=sn,
                                 telephoneNumber=telephoneNumber,
                                 userPassword=userPassword)
        return result
