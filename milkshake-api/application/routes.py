from application import app
from flask import Flask, request, Response, jsonify
import random

@app.route('/get_milkshake', methods=['GET'])
def milkshake():
    milk_flavour = ["Chocolate", "Biscoff", "Strawberry", "Jammy Dodger", "Vanilla", "Cookies 'n' Cream"]

    #convert values into integer - pick one at random
    return random.choice(milk_flavour)