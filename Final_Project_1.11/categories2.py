from flask import Flask, render_template, send_from_directory, url_for
import pandas as pd
import os

app = Flask(__name__)

#Load the CSV file containing all books
all_books = pd.read_excel('Booklist2.xlsx')

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/fantasy')
def display_fantasy_books():
    fantasy_books = all_books[all_books['Genre'] == 'Fantasy']
    return render_template('Fantasy.html', fantasy_books=fantasy_books)

@app.route('/mystery')
def display_mystery_books():
    mystery_books = all_books[all_books['Genre'] == 'Mystery']
    return render_template('Mystery.html', mystery_books=mystery_books)

@app.route('/crime')
def display_crime_books():
    crime_books = all_books[all_books['Genre'] == 'Crime']
    return render_template('Crime.html', crime_books=crime_books)

@app.route('/adventure')
def display_adventure_books():
    adventure_books = all_books[all_books['Genre'] == 'Adventure']
    return render_template('Adventure.html', adventure_books=adventure_books)

@app.route('/drama')
def display_drama_books():
    drama_books = all_books[all_books['Genre'] == 'Drama']
    return render_template('Drama.html', drama_books=drama_books)

@app.route('/natural_disaster')
def display_natural_disaster_books():
    natural_disaster_books = all_books[all_books['Genre'] == 'Natural Disaster']
    return render_template('Natural Disaster.html', natural_disaster_books=natural_disaster_books)

@app.route('/psychological')
def display_psychological_books():
    psychological_books = all_books[all_books['Genre'] == 'Psychological']
    return render_template('psychological.html', psychological_books=psychological_books)

@app.route('/romance')
def display_romance_books():
    romance_books = all_books[all_books['Genre'] == 'Romance']
    return render_template('Romance.html', romance_books=romance_books)

@app.route('/thriller')
def display_thriller_books():
    thriller_books = all_books[all_books['Genre'] == 'Thriller']
    return render_template('Thriller.html', thriller_books=thriller_books)

@app.route('/philosophy')
def display_philosophy_books():
    philosophy_books = all_books[all_books['Genre'] == 'Philosophy']
    return render_template('Philosophy.html', philosophy_books=philosophy_books) 

@app.route('/travel')
def display_travel_books():
    travel_books = all_books[all_books['Genre'] == 'Travel']
    return render_template('Travel.html', travel_books=travel_books)

@app.route('/young_adult')
def display_young_adult_books():
    young_adult_books = all_books[all_books['Genre'] == 'Young Adult']
    return render_template('Young Adult.html', young_adult_books=young_adult_books)

@app.route('/biography')
def display_biography_books():
    biography_books = all_books[all_books['Genre'] == 'Biography']
    return render_template('Biography.html', biography_books=biography_books)

@app.route('/horror')
def display_horror_books():
    horror_books = all_books[all_books['Genre'] == 'Horror']
    return render_template('Horror.html', horror_books=horror_books)

@app.route('/non_fiction')
def display_non_fiction_books():
    non_fiction_books = all_books[all_books['Genre'] == 'Non-Fiction']
    return render_template('Non-Fiction.html', non_fiction_books=non_fiction_books)

@app.route('/fiction')
def display_fiction_books():
    fiction_books = all_books[all_books['Genre'] == 'Fiction']
    return render_template('Fiction.html', fiction_books=fiction_books)

@app.route('/login')
def login():
    return send_from_directory('static/html', 'login.html')

@app.route('/create_account')
def create_account():
    return send_from_directory('static/html', 'create-account.html')

@app.route('/aboutus')
def aboutus():
    return send_from_directory('static/html', 'aboutus.html')

@app.route('/home')
def home():
    return send_from_directory('static/html', 'index.html')

@app.route('/contact')
def contact():
    return send_from_directory('static/html', 'contact.html')

@app.route('/orders')
def orders():
    return send_from_directory('static/html', 'order_page.html')


if __name__ == '__main__':
    app.run(debug=True)
