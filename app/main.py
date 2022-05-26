from flask import Flask, request
from flask import jsonify
from config import config

from api.predict_data import get_predict_data_post, get_predict_data
from api.predict_risk import get_risk_data_post, get_risk_data_get

from flask_cors import CORS, cross_origin


def create_app(enviroment):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(enviroment)

    return app


enviroment = config['development']
app = create_app(enviroment)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
@cross_origin()
def initial_get():
    response = {
        'message': 'Endpoint para consumir la predicción del nivel de satifacción del usuario',
        'status': 200
    }

    return jsonify(response)


@app.route('/prediccion', methods=['GET', 'POST'])
@cross_origin()
def call_predict():
    if request.method == 'POST':
        return get_predict_data_post(request)
    return get_predict_data()


@app.route('/prediccion-model-risk', methods=['GET', 'POST'])
@cross_origin()
def call_predict_risk():
    if request.method == 'POST':
        return get_risk_data_post(request)
    return get_risk_data_get()
