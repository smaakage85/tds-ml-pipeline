from flask import Flask, jsonify, request
import os
app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

# instantiate and build model
from pkg.models import Model

model = Model()
model.build_model()

# check version
import pkg_resources
vrs = pkg_resources.get_distribution('irismodel').version

welcome = """
        Try calling the app (Windows): 
        curl -H "Content-Type: application/json" -X POST -d "[{\\"x1\\":5.1, \\"x2\\":3.5, \\"x3\\":1.4, \\"x4\\":0.2}, {\\"x1\\":6.2, \\"x2\\":3.4, \\"x3\\":5.4, \\"x4\\":2.3}]" https://larsk-flask.herokuapp.com/predict/
        """

@app.route('/')
def home():
    return welcome

@app.route('/predict/', methods=['POST'])
def predict():
    X = request.get_json()
    X = model.parse_input(X)     
    preds = model.predict(X)
    preds_json = model.parse_output(preds)
    return jsonify({'model_version': vrs}, preds_json)

@app.route('/')
def hello_world():
    return 'Flask Dockerized and deployed to Heroku'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)