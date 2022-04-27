from flask import Flask, request
from flask import jsonify
from config import config

from api.predict_data import get_predict_data


def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)

    return app


enviroment = config['development']
app = create_app(enviroment)


@app.route('/', methods=['GET'])
def initial_get():
    response = {
        'message': 'Endpoint para consumir la predicción del nivel de satifacción del usuario',
        'status': 200
    }

    return jsonify(response)


@app.route('/prediccion', methods=['GET', 'POST', 'PUT'])
def call_predict():
    return get_predict_data(request)


if __name__ == '__main__':
    app.run(debug=True)
