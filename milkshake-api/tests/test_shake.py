from application import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
from application import routes

class TestBase(TestCase):
    def create_app(self):
        return app


class TestShake(TestBase):
    def test_shake_name(self):
        with patch('random.choice') as y:
            y.return_value = "Biscoff"
            response = self.client.get(url_for('milkshake'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Biscoff', response.data)