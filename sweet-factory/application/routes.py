from application import app, db
from flask import Flask, request, render_template, url_for
from application.models import *
import requests, json


@app.route('/', methods = ['POST', 'GET'])
def home():
    cakes = requests.get('http://cake-api:5000/get_cake').text
    shakes = requests.get('http://milkshake-api:5000/get_milkshake').text
    tooth = requests.post('http://icecream-api:5000/get_toothache', json = dict(cakes=cakes, shakes=shakes))

    combo = Treats(cake_name=cakes, milk_name=shakes, toothache=tooth.text)

    six_res = Treats.query.order_by(Treats.id.desc()).limit(6).all()

    if combo:
        db.session.add(combo)
        db.session.commit()

    return render_template('home.html', six_res=six_res, cakes=cakes, shakes=shakes, tooth=tooth.text, title='Home')


@app.route('/idea-library', methods=['GET'])
def ideas():
    tooth_hurt = Treats.query.all()
    return render_template('library.html', tooth_hurt=tooth_hurt)