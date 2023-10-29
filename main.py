from flask import Flask, render_template, flash, request, redirect, url_for, session
import json
import requests
from functions import *

app = Flask(__name__)


@app.route('/' , methods = ['GET' , 'POST'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)