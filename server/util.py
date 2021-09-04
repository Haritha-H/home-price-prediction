import json
import pickle
import numpy as np

def get_estimated_price(location, total_sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1
    result = [ '%.2f' % elem for elem in list(__model.predict([x])[0])]
    return result
def get_location_names():
    return __locations

def load_saved_artifacts():
    global __locations
    global __model
    global __data_columns
    #print('Loading saved artifacts:')
    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    with open("./artifacts/realestate_prices_prediction_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Artifacts are loaded")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location



