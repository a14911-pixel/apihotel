from flask_restful import Resource, reqparse
from models.hotel import HotelModel


# Listar todos os hóteis
class Hoteis(Resource):
    def get(self):
        return { "hoteis": [hotel.json() in HotelModel.query.all()]}

# Listar, inserir, atualizar e eliminar um hotel específico
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, help="Nome obrigatótio")
    argumentos.add_argument("estrelas", type=float, help="Estrelas obrigatótio")
    argumentos.add_argument("diaria", type=float, help="Diária obrigatótio")
    argumentos.add_argument("cidade", type=str, help="Cidade obrigatótio")

    def get(self, id_hotel):
        hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if hotel_encontrado:
                return hotel_encontrado.json(), 200
        return { "message" : "Hotel not found"}, 404
        

    def post(self, id_hotel):
        dados = Hotel.argumentos.parse_args()# Dicionário
        hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if hotel_encontrado:
         return { " message": "Hotel with this id already exists"}
        novo_hotel = HotelModel(id_hotel, **dados)
        novo_hotel.save_hotel()
        return novo_hotel.json(), 200

      def put(self, id_hotel):
        dados = Hotel.argumentos.parse_args()
        Hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if Hotel_encontrado:
            hotel_atualizado = HotelModel(id_hotel, **dados)
            hotel_atualizado.update_hotel(**dados)
            hotel_atualizado.save_hotel()
            return hotel_atualizado.json(), 200
            hotel.update(**dados)
            return hotel, 200
                
            novo_hotel = { "hotel_id" : id_hotel, **dados}
            hoteis.append(novo_hotel)
            return novo_hotel, 201 # Created

    def delete(self, id_hotel):
         global hoteis
         hoteis = [hotel for hotel in hoteis if hotel["hotel_id"] != id_hotel]
         return { "message": f"Hotel with {id_hotel} deleted"}