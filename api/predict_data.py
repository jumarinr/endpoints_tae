import os
from xmlrpc.client import Boolean
import joblib
from flask import Request, Response
import pandas

ABSOLUTE_PATH = os.getcwd()

# cargamos la ruta donde está almacenado el modelo de abuelos
RELATIVE_PATH_ABUELOS = '/models/granparents_model.pkl'
MODEL_PATH_ABUELOS = ABSOLUTE_PATH + RELATIVE_PATH_ABUELOS

# cargamos la ruta donde está almacenado el modelo de niños
RELATIVE_PATH_KIDS = '/models/kids_model.pkl'
MODEL_PATH_KIDS = ABSOLUTE_PATH + RELATIVE_PATH_KIDS

# cargamos el modelo de abuelos
MODELO_ABUELOS = joblib.load(open(MODEL_PATH_ABUELOS, 'rb'))

# cargamos el modelo de niños
MODELO_KIDS = joblib.load(open(MODEL_PATH_KIDS, 'rb'))


def get_predict_data_post(request: Request):
    # extraemos los datos de la petición
    print("ingresa")
    file_uploaded = request.files["file"]
    print(file_uploaded)
    is_abuelo = request.form.get('isAbuelo')
    is_abuelo = True if is_abuelo == 'true' else False

    # definimos el modelo a utilizar
    model_to_use = MODELO_ABUELOS if is_abuelo == True else MODELO_KIDS

    # definimos la data de prueba
    test_data = pandas.read_csv(file_uploaded, sep=r",|;")

    # definimos la predicción
    prediccion = model_to_use.predict(test_data)
    result_prediccion = pandas.Series(prediccion)

    # retornamos los datos
    return result_prediccion.to_json(orient="table")


def get_predict_data():
    return Response('La peticion se debe realizar con el metodo POST', status=400)
