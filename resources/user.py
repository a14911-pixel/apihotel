from flask_restful import Resource, reqparse
from models.user import UserModel
from hmac import compare_digest
from flask_jwt_extended import create_access_token, jwt_required


# Listar, inserir, atualizar e eliminar um hotel específico
class User(Resource):

    def get(self, username):
        user_encontrado = UserModel.find_hotel(username)
        if user_encontrado:
                return user_encontrado.json(), 200
        return { "message" : "Hotel not found"}, 404

    @jwt_required() 
    def delete(self, username):
        user_encontrado = UserModel.find_user(username)
        if user_encontrado:
            user_encontrado.delete_user()
            return { "message": f"Hotel with {username} deleted"}
        return { "message": "User not found"}, 404

class UserRegister(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("username", type=str, help="Username obrigatótio")
    argumentos.add_argument("password", type=str, help="Password obrigatótio")

    def post(self):
        dados = UserRegister.argumentos.parse_args()# Dicionário
        user_encontrado = UserModel.find_user(dados["username"])
        if user_encontrado:
            return { " message": "Hotel with this username already exists"}
        novo_user = UserModel(**dados)
        novo_user.save_user()
        return novo_user.json(), 200
    
class UserLogin(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("username", type=str, help="Username obrigatótio")
    argumentos.add_argument("password", type=str, help="Password obrigatótio")

    def post(self):
        dados = UserLogin.argumentos.parse_args()
        user = UserModel.find_user(dados["username"])

        if user and compare_digest(user.password,dados["password"]):
            token = create_access_token(identity=user.username)
            return { "access_token" : token}
        return { "message": "Username or password invalid!"}

class UserLogout(Resource):
    ...
