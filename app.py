from flask import Flask
from flask_restful import Resource, Api

# Variável representar a minha aplicação
app = Flask(__name__)
api = Api(app)

hoteis = [
    { "hotel_id": "paraiso", "nome": "Hotel Paraiso", "estrelas": 4.6, "diaria":123.99, "cidade": "Porto"},
    { "hotel_id": "fukui", "nome": "Fukui Resort", "estrelas": 4.8, "diaria":225.99, "cidade": "Viena"},
    { "hotel_id": "aguas", "nome": "Hotel Aguas", "estrelas": 4.2, "diaria":193.99, "cidade": "Lisboa"},
]

class Hoteis(Resource):
    def get(self):
        return { "hoteis": hoteis}


# Rotas
api.add_resource(Hoteis, "/hoteis")
    

if __name__ == "__main__":
    app.run(debug=True)
