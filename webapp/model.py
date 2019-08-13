import numpy as np
import sklearn


def model_prediction(input):
    labels = ['crime_rate',
              'avg_number_of_rooms',
              'distance_to_employment_centers',
              'property_tax_rate',
              'pupil_teacher_ratio'
              ]
    train = np.asarray([input[x] for x in labels]).reshape(1,-1)
    model = sklearn.externals.joblib.load('model.pkl')
    SD = sklearn.externals.joblib.load('SD.pkl')
    prediction = model.predict(train)
    result = {'house_value': prediction[0],
              'stddev': SD}
    return result