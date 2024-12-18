import pandas as pd
from models import RecommenderModel
from utils import preprocess_user_data, preprocess_non_profit_data

def recommend_non_profits(user_data):
    non_profit_data = pd.read_csv('data/non_profit_data.csv')
    preprocessed_non_profits = preprocess_non_profit_data(non_profit_data)

    user_vector = preprocess_user_data(user_data)

    recommender = RecommenderModel()
    recommender.fit(preprocessed_non_profits)

    recommendations = recommender.recommend(user_vector)
    recommended_non_profits = non_profit_data.iloc[recommendations]
    
    return recommended_non_profits.to_dict(orient='records')
