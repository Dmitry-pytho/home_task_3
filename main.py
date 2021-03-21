from flask import Flask, render_template
from faker import Faker
from random import shuffle, choice
import string
import requests

app = Flask(__name__)


@app.route('/')
def start_page():
    return "start page"


@app.route('/users/generate')
@app.route('/users/generate/<int:N>')
def users_generate_by_url(N=20):
    dict_of_fakes = {}
    fake = Faker()
    for _ in range(N):
        dict_of_fakes[fake.name()] = fake.email()
    return dict_of_fakes


@app.route('/password/generate')
@app.route('/password/generate/<int:N>')
def generate_password_exact_value(N=30):
    symbols = list(string.ascii_letters)
    shuffle(symbols)
    random_password = ""
    for _ in range(N):
        symbol = choice(symbols)
        random_password = (random_password + symbol)
    return random_password


@app.route('/astro')
def list_of_astro():
    r = requests.get('http://api.open-notify.org/astros.json')
    astro = r.json()
    number_of_astro = str(len(astro["people"]))
    return number_of_astro


