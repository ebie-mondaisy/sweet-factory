from application import app
from flask import Flask, request, Response
import random

@app.route('/get_milkshake', methods=['GET'])
def milkshake():
    milk_flavour = ["Chocolate", "Biscoff", "Strawberry", "Jammy Dodger", "Vanilla", "Cookies 'n' Cream"]
    shake = random.choice(milk_flavour)
    return shake