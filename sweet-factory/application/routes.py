from application import app, db
from flask import Flask, request, render_template, url_for
from application.models import *
import requests


@app.route('/', methods = ['GET'])
def home():
    cakes = requests.get('http://cake-api:5000/get_cake')
    shakes = requests.get('http://milkshake-api:5000/get_milkshake')
    cream = requests.post('http://icecream-api:5000/get_icecream', json = dict(cakes=cakes, shakes=shakes))
    return render_template('home.html', cakes=cakes, shakes=shakes, cream=cream.text, title='Home')


@app.route('/idea-library', methods=['GET'])
def ideas():
    pass