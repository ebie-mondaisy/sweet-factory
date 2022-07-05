from application import app
from flask import url_for
from flask_testing import TestCase
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestFront(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as z:
            z.get('http://cake-api:5000/get_cake', text='Confetti')
            z.get('http://milkshake-api:5000/get_milkshake', text='Strawberry')
            z.post('http://toothache-api:5000/get_toothache', text='16')
            response=self.client.get(url_for('home'))
            self.assert200(response)
            self.assertIn(b'Confetti', response.data)
            self.assertIn(b'Strawberry', response.data)
            self.assertIn(b'16', response.data)