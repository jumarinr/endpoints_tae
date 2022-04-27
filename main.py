from flask import Flask
from flask import jsonify
from config import config


def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    return app


enviroment = config['development']
app = create_app(enviroment)


@app.route('/', methods=['GET'])
def initial_get():
    response = {'message': 'success'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=False)
