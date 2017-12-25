from flask import render_template
from app import app
from app.forms import SearchForm
import requests


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    data = None

    if form.validate_on_submit():
        payload = {
            'action': 'opensearch',
            'search': form.query.data,
            'limit': 10,
            'namespace': 0,
            'format': 'json'
        }
        
        r = requests.get('https://en.wikipedia.org/w/api.php', params=payload)
        
        data = r.json()


    return render_template('index.html', data=data, form=form)
