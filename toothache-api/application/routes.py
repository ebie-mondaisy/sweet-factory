from application import app
from flask import Flask, request, Response
import pdb

@app.route('/get_toothache', methods=['POST'])
def toothache():
    count = 0

    # pdb.set_trace()

    sweet_data = request.get_json()
    
    if sweet_data['cakes'] == 'Red Velvet':
        count += 6
    if sweet_data['cakes'] == 'Victoria Sponge':
        count += 4
    if sweet_data['cakes'] == 'Chocolate':
        count += 7
    if sweet_data['cakes'] == 'Confetti':
        count += 9
    if sweet_data['cakes'] == 'Bubblegum':
        count += 10
    if sweet_data['cakes'] == 'Lemon Drizzle':
        count += 5

    if sweet_data['shakes'] == 'Chocolate':
        count += 5
    if sweet_data['shakes'] == 'Biscoff':
        count += 6
    if sweet_data['shakes'] == 'Strawberry':
        count += 7
    if sweet_data['shakes'] == 'Jammy Dodger':
        count += 10
    if sweet_data['shakes'] == 'Vanilla':
        count += 3
    if sweet_data['shakes'] == "Cookies 'n' Cream":
        count += 8

    return str(count)