from application import app
from flask import flask, request, Response

@app.route('/get_icecream', methods=['POST'])
def icecream():
    sweet_data = request.get_json()
    