from application import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
from application import routes

class TestBase(TestCase):
    def create_app(self):
        return app


class TestCake(TestBase):
    def test_cake_name(self):
        with patch('random.choice') as x:
            x.return_value = "Chocolate"
            response = self.client.get(url_for('cake'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Chocolate', response.data)