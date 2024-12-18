import numpy as np

def preprocess_user_data(user_data):
    user_vector = np.array([user_data['interests'], user_data['location']])
    return user_vector

def preprocess_non_profit_data(non_profit_data):
    return non_profit_data.drop(columns=['name', 'description']).values
