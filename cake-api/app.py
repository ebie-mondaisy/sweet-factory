from flask import Flask
from application import app

if __name == '__main__':
    app.run(debug = True, port = 5000, host = '0.0.0.0')