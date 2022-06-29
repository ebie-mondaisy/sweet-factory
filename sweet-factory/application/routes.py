from application import app, db
from flask import Flask, request, render_template, url_for
from application.models import *
import requests


@app.route('/')
def home():
    cakes = requests.get('http://cake-api:5000/get_cake').text
    shakes = requests.get('http://milkshake-api:5000/get_milkshake').text
    cream = requests.post('http://icecream-api:5000/get_icecream')