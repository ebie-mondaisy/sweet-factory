from application import app
from flask import Flask, request, Response
import random

@app.route('/get_milkshake', methods=['GET'])
def milkshake():
    milk_flavour = random.choice(["Chocolate", "Biscoff", "Strawberry", "Jammy Dodger", "Vanilla", "Cookies 'n' Cream"])