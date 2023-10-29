from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)

@app.route('/' , methods = ['GET' , 'POST'])
def index():
    pokemon = ""
    pokedex = ""

    if request.method == "POST":
        pokemon = request.form["pokemon"] # get the name="pokemon" from our form in index.html
        pokedex = get_info(pokemon)

    return render_template(
    'index.html', 
    pokemon=pokemon,
    pokedex = pokedex
    )

if __name__ == "__main__":
    app.run(debug=True)