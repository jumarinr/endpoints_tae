import os
from xmlrpc.client import Boolean
import joblib
from flask import Request, jsonify, Response
import pandas


# cargamos la ruta donde está almacenado el modelo de adultos
RELATIVE_PATH_ABUELOS = '/models/model_adultos.pkl'
ABSOLUTE_PATH = os.getcwd()
MODEL_PATH_ABUELOS = ABSOLUTE_PATH + RELATIVE_PATH_ABUELOS

# cargamos el modelo de adultos
loaded_model_abuelos = joblib.load(open(MODEL_PATH_ABUELOS, 'rb'))


def get_predict_data_post(request: Request):
    # extraemos los datos de la petición
    file_uploaded = request.files["file"]
    data_base_submitted = pandas.read_csv(file_uploaded)
    is_abuelo = request.form.get('isAbuelo')
    is_abuelo = True if is_abuelo == 'true' else False

    # definimos el modelo a utilizar
    model_to_use = loaded_model_abuelos if is_abuelo == True else loaded_model_abuelos

    # definimos la data de prueba
    test_data = data_base_submitted.drop(['life_satisfaction'], axis=1)

    # definimos la predicción
    prediccion = model_to_use.predict(test_data)
    result_prediccion = pandas.Series(prediccion)

    # retornamos los datos
    return result_prediccion.to_json(orient="table")


def get_predict_data():
    return Response('La peticion se debe realizar con el metodo POST', status=400)
