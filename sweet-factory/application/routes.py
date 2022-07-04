from application import app
from flask import Flask, request, render_template, url_for
import requests, json


@app.route('/')
def home():
    cakes = requests.get('http://cake-api:5000/get_cake').text
    shakes = requests.get('http://milkshake-api:5000/get_milkshake').text
    tooth = requests.post('http://toothache-api:5000/get_toothache', json = dict(cakes=cakes, shakes=shakes))

    return render_template('home.html', cakes=cakes, shakes=shakes, tooth=tooth.text)