from application import app
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        return app


class TestTooth(TestBase):
    def test_count(self):
        response = self.client.post(url_for('toothache'), json={"cakes": "Red Velvet", "shakes": "Chocolate"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'11', response.data)

    def test_count1(self):
        response = self.client.post(url_for('toothache'), json={"cakes": "Victoria Sponge", "shakes": "Biscoff"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)

    def test_count2(self):
        response = self.client.post(url_for('toothache'), json={"cakes": "Chocolate", "shakes": "Strawberry"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)

    def test_count3(self):
        response = self.client.post(url_for('toothache'), json={"cakes": "Confetti", "shakes": "Jammy Dodger"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)

    def test_count4(self):
        response = self.client.post(url_for('toothache'), json={"cakes": "Bubblegum", "shakes": "Vanilla"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'13', response.data)

    def test_count5(self):
        response = self.client.post(url_for('toothache'), json={"cakes": "Lemon Drizzle", "shakes": "Cookies 'n' Cream"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'13', response.data)