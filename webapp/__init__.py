from flask import Flask, request, jsonify, abort

from webapp.model import model_prediction
from webapp.validate import validate

app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    request.get_data()
    print(request.mimetype)
    input = request.get_json(force=True)
    if validate(input):
        pass
    else:
        return abort(400)
    output = model_prediction(input) #{'house_value': 1.0, 'stddev': 1.0}
    resp = jsonify(output)
    return resp