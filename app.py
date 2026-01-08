from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Base URL API
API_BASE_URL = "https://dummyjson.com/recipes"

@app.route('/')
def index():
    # Request data dari API
    response = requests.get(API_BASE_URL)
    data = response.json()
    recipes = data['recipes']
    return render_template('index.html', recipes=recipes)

@app.route('/detail/<int:recipe_id>')
def detail(recipe_id):
    # Request detail resep berdasarkan ID
    response = requests.get(f"{API_BASE_URL}/{recipe_id}")
    recipe = response.json()
    return render_template('detail.html', recipe=recipe)

@app.route('/search')
def search():
    # Fitur pencarian (bonus)
    query = request.args.get('q', '')
    response = requests.get(f"{API_BASE_URL}/search?q={query}")
    data = response.json()
    recipes = data['recipes']
    return render_template('index.html', recipes=recipes, query=query)

if __name__ == '__main__':
    app.run(debug=True)