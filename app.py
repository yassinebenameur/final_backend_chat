
import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required
from flask_restful import Resource, Api

from Auth import Authentication

app = Flask(__name__)
JWT_SECRET_KEY = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
# app.secret_key = 't1NP63m4wnBg6nyHYKfmc2Ulvdtggbsd'
api = Api(app)
path = os.path.dirname(__file__)
CORS(app)
jwt = JWTManager(app)



authentication = Authentication()


class HelloWorld(Resource):
    @jwt_required
    def get(self):
        return {'hello': 'world'}


class Login(Resource):
    def post(self):
        return authentication.login()


class Signup(Resource):
    def post(self):
        print('jesuis ici')
        return authentication.signup()


class SocketIO(Resource):
    @jwt_required
    def get(self):
        return


api.add_resource(HelloWorld, '/')
api.add_resource(Login, '/login')
api.add_resource(Signup, '/signup')
api.add_resource(SocketIO, '/socketIO')

if __name__ == '__main__':
    app.run(debug=True)
