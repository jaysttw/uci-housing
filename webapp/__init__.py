import os
import numpy as np
import sklearn
from flask import Flask, request, jsonify, json, abort

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

def validate(input):
    labels = {'crime_rate',
              'avg_number_of_rooms',
              'distance_to_employment_center',
              'property_tax_rate',
              'pupil_teacher_ratio'
              }
    #print(f"Label check: {[x in input for x in labels]}")
    #print(f"Type check: {[isinstance(input[x], (int, float)) for x in labels]}")
    if not all([x in input for x in labels]):
        return False
    elif not all([isinstance(input[x], (int, float)) for x in labels]):
        return False
    else:
        return True

def model_prediction(input):
    labels = ['crime_rate',
              'avg_number_of_rooms',
              'distance_to_employment_center',
              'property_tax_rate',
              'pupil_teacher_ratio'
              ]
    train = np.asarray([input[x] for x in labels]).reshape(1,-1)
    model = sklearn.externals.joblib.load(
        os.path.abspath(
            os.path.join(
                os.path.pardir,
                'model.pkl'
            )
        )
    )
    SD = sklearn.externals.joblib.load(
        os.path.abspath(
            os.path.join(
                os.path.pardir,
                'SD.pkl'
            )
        )
    )
    prediction = model.predict(train)
    result = {'house_value': prediction[0],
              'stddev': SD}
    return result