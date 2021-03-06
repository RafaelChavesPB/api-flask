from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

#modificação

app = Flask(__name__)
app.secret_key = 'secreta'
api = Api(app)

items = []

jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/item')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
     app.run(port=5000, debug=True)
