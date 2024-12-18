import unittest
from recommender import recommend_non_profits

class RecommendTestCase(unittest.TestCase):
    def test_recommend_non_profits(self):
        user_data = {
            'interests': 1,
            'location': 'New York'
        }
        recommendations = recommend_non_profits(user_data)
        self.assertIsInstance(recommendations, list)
