import os
import joblib
from flask import Request, jsonify


RELATIVE_PATH = '/models/model_adultos.pkl'

absolute_path = os.getcwd()
model_path = absolute_path + RELATIVE_PATH
# load the model from disk
loaded_model = joblib.load(open(model_path, 'rb'))


def get_predict_data(request: Request):
    response = {
        'status': 200
    }

    print(request)

    #result = loaded_model.score(X_test, Y_test)

    return jsonify(response)
