from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import make_response


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        name = request.form['name'] or 'No name'
        mail = request.form['mail'] or 'empty value'
        response = make_response(redirect(url_for('hello', name=name, mail=mail)))
        response.set_cookie('username', name)
        response.set_cookie('usermail', mail)
        return response
    return render_template('index.html')


@app.route('/hello/<name>/<mail>/', methods=["GET", "POST"])
def hello(name, mail):
    if request.method == 'POST':
        response = make_response(redirect(url_for('form')))
        response.set_cookie('username', '', max_age=0)
        response.set_cookie('usermail', '', max_age=0)
        return response
    return render_template('hello.html', name=name, mail=mail)


if __name__ == '__main__':
    app.run(debug=True)