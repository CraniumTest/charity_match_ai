from flask import Flask, jsonify, request
from recommender import recommend_non_profits

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_data = request.json
    recommendations = recommend_non_profits(user_data)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
