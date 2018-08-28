import os
from flask import Flask

def create_app(test_config=None):
    # Create and configure Flask app
    app = Flask(__name__, instance_relative_config=True)
    
    @app.route('/predict', methods=['GET', 'POST'])
    def predict():
        request.get_data()
        print(request.mimetype)
        input = request.get_json(force=True)
        if validate(input):
            resp.status_code = 200
        else:
            return abort(400)
        output = {'house_value': 1.0, 'stddev': 1.0}
        resp = jsonify(output)
        return resp

    def validate(input):
        labels = {'crime_rate',
                  'avg_number_of_rooms',
                  'distance_to_employment_center',
                  'property_tax_rate',
                  'pupil_teacher_ratio'
                  }
        if labels not in input:
            return False
        elif not all([isinstance(input[x], (int, float)) for x in labels]):
            return False
        else:
            return True

    return app
