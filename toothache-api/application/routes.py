from application import app
from flask import flask, request, Response

@app.route('/get_toothache', methods=['POST'])
def toothache():
    count = 0

    sweet_data = request.get_json()
    
    if sweet_data['cakes'] == 'Red Velvet':
        count += 6
    elif sweet_data['cakes'] == 'Victoria Sponge':
        count += 4
    elif sweet_data['cakes'] == 'Chocolate':
        count += 7
    elif sweet_data['cakes'] == 'Confetti':
        count += 9
    elif sweet_data['cakes'] == 'Bubblegum':
        count += 10
    elif sweet_data['cakes'] == 'Lemon Drizzle':
        count += 5

    if sweet_data['shakes'] == 'Chocolate':
        count += 1
    elif sweet_data['shakes'] == 'Biscoff':
        count += 2
    elif sweet_data['shakes'] == 'Strawberry':
        count += 3
    elif sweet_data['shakes'] == 'Jammy Dodger':
        count += 4
    elif sweet_data['shakes'] == 'Vanilla':
        count += 5
    elif sweet_data['shakes'] == "Cookies 'n' Cream":
        count += 6

        return str(count)