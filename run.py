# on importe flask

from flask import Flask, render_template
import utils as u

# render permet de gerer la partit template

app = Flask(__name__)  # objet

# on creer une simple variable avec notre donnee

users = [
    {'name': 'Hero', 'grade': 1, 'notes': [15, 17, 11, 9, 10]},
    {'name': 'Dunn', 'grade': 2, 'notes': [10, 11, 11, 19, 7]},
    {'name': 'Sue', 'grade': 2, 'notes': [13, 17, 9, 9, 7]},
    {'name': 'Thor', 'grade': 1, 'notes': [15, 17, 20, 19, 16]},
    {'name': 'Hicks', 'grade': 1, 'notes': [13, 10, 11, 6, 12]},
]


# premiere route
@app.route('/')  # decorateur
@app.route('/home')
def index():

    # dans data, on stocke notre variable et title de meme

    return render_template('index.html', data=users, title="Liste des etudiants", average=u.moyenne)

# deuxieme route


@app.route('/contact')  # dans la console avec /contact on accede a cette page
def contact():
    return 'Page contact'  # on affiche "page contact"

@app.route('/best')  # dans la console avec /contact on accede a cette page
def best():
    return render_template('best.html', maximum=u.moyenne_max, data = users)


if __name__ == "__main__":
    app.run()
