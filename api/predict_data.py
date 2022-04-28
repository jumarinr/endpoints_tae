import os
import joblib
from flask import Request, jsonify, Response
import pandas


# cargamos la ruta donde está almacenado el modelo de adultos
RELATIVE_PATH = '/models/model_adultos.pkl'
ABSOLUTE_PATH = os.getcwd()
MODEL_PATH = ABSOLUTE_PATH + RELATIVE_PATH

# cargamos el modelo de adultos
loaded_model = joblib.load(open(MODEL_PATH, 'rb'))


def get_predict_data_post(request: Request):
    file_uploaded = request.files["file"]
    data_base_submitted = pandas.read_csv(file_uploaded)

    test_data = data_base_submitted.drop(['life_satisfaction'], axis=1)

    prediccion = loaded_model.predict(test_data)
    result_prediccion = pandas.Series(prediccion)

    return result_prediccion.to_json(orient="index")


def get_predict_data():
    return Response('La peticion se debe realizar con el metodo POST', status=400,)
