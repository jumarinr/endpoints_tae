import os
from flask import Request, Response
import pandas
import pickle
import numpy

ABSOLUTE_PATH = os.getcwd()


# cargamos la ruta donde está almacenado el modelo riesgo de credito
RELATIVE_PATH_RISK = '/models/scorecard_model.pickle'

MODEL_PATH = ABSOLUTE_PATH + RELATIVE_PATH_RISK

# cargamos el modelo del riesgo
pickle_model = pickle.load(open(MODEL_PATH, 'rb'))


min_score = 300
max_score = 850


def condition(predited_value): return predited_value[1]


def get_risk_data_post(request: Request):
    file_uploaded = request.files["file"]

    # definimos la data de prueba
    test_data = pandas.read_csv(file_uploaded, sep=r",|;", engine='python')

    prediccion = pickle_model.score(test_data)

    result_prediccion = pandas.Series(prediccion)
    result_prediccion = result_prediccion.astype(numpy.float64)

    return result_prediccion.to_json(orient="table")


def get_risk_data_get():
    return Response('La peticion se debe realizar con el metodo POST', status=400)
