import unittest
from mock import MagicMock, patch, call
from personality import views

class TestViews(unittest.TestCase):
    def setUp(self):
        self.mockclass = MockClass()

    def test_json_review(self):
        views_reviews = views.all_reviews()
        mock_reviews = self.mockclass.mock_review()
        self.assertEquals(type(views_reviews), type(mock_reviews))
        views_one = views_reviews[0]
        mock_one = mock_reviews[0]
        views_keys = views_one.keys()
        mock_keys = mock_one.keys()
        for i in mock_keys:
            self.assertIn(i, views_keys)

class MockClass():
    def mock_review(self):
        reviews = [
                      {
                        "reviewerID": "A3D6KZT0QG6UKB",
                        "reviewerName": "Tim Lieder \"Founder of Dybbuk Press\"",
                        "reviewText": "There's a scene in Misery where the author writes what he thinks his nurse/tormentor wants to read and suffers for his presumption. Her main problem is the fact that he cheated when he explained that his heroine was alive, but there was also the fact that he was second guessing his audience."
                      },
                      {
                        "reviewerID": "AER15RIMV8E6D",
                        "reviewerName": "Pumpkin Man",
                        "reviewText": "Season 1- Monk is a hilarious and an incredibly entertaining series. Three years earlier, Adrian Monk's wife, Trudy was murdered by a car bomb. He has extreme O.C.D. and relies on his Nurse/Assistant Sharona to help him while he solves murders with Captain Leland Stottlemeyer, and Lt. Randy Disher."
                      }
                    ]
        return reviews

if __name__ == '__main__':
    unittest.main()
