from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    context = {
        'title': 'My internet shop'
    }
    return render_template('index.html', **context)


@app.route('/clothes/')
def clothes_page():
    context = {
        'title': 'Clothes Page'
    }
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes_page():
    context = {
        'title': 'Shoes Page'
    }
    return render_template('shoes.html', **context)


@app.route('/jacket/')
def jacket_page():
    context = {
        'title': 'Jacket Page'
    }
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run()
