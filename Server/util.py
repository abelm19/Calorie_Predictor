import pickle
import json
import numpy as np

__data_columns = None
__model = None

def get_estimated_calories(gender,age,height,weight,duration,heart_rate,body_temp):

    x = np.zeros(len(__data_columns))
    x[0] = gender
    x[1] = age
    x[2] = height
    x[3] = weight
    x[4] = duration
    x[5] = heart_rate
    x[6] = body_temp
    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('./artifacts/calorie_pred.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_calories(1,33,140,76,35,150,39))
    print(get_estimated_calories(0,33,180,76,35,150,39))
    print(get_estimated_calories(1,32,189,76,35,150,39))
    print(get_estimated_calories(0,44,200,76,35,150,39))
