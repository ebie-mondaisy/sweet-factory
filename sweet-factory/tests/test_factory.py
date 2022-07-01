from application import app, db
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application.models import *

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db", DEBUG=True)

        return app


    def setUp(self):

        db.create_all()

        test1=Treats(cake_name="Red Velvet", milk_name="Chocolate", toothache="11")

        db.session.add(test1)
        db.session.commit()

    
    def tearDown(self):

        db.session.remove()
        db.drop_all()


class TestFront(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as z:
            z.get('http://cake-api:5000/get_cake', text='Confetti')
            z.get('http://milkshake-api:5000/get_milkshake', text='Strawberry')
            z.post('http://icecream-api:5000/get_toothache', text='16')
            response=self.client.get(url_for('home'))
            self.assert200(response)
            self.assertIn(b'Confetti', response.data)
            self.assertIn(b'Strawberry', response.data)
            self.assertIn(b'16', response.data)

    def test_idea(self):
        response=self.client.get(url_for('ideas'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)
