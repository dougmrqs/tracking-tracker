import json
from app import app
from app.forms import LoginForm
from flask import render_template, request


@app.route('/', methods=['GET'])
def index():
    if request.args:
        print(request.args)
    form = LoginForm()
    return render_template('filters.html', form=form)

@app.route('/query')
def query_form():
    return render_template('filters.html')

@app.route('/countries')
def countries_table():
    filename = './app/assets/paises.json'
    with open(filename, 'r') as openfile: 
        db = json.load(openfile)
    return render_template('countries_table.html', db = db)

@app.route('/postals')
def postals_table():
    filename = './app/assets/siglas.json'
    with open(filename, 'r') as openfile: 
        db = json.load(openfile)
    return render_template('postals_table.html', db = db)

@app.route('/crawlers')
def crawl_tools():
    return render_template("crawl_tools.html")

@app.route('/export_csv')
def export_csv():
    print('EXPORTA AI')
    return render_template("filters.html")