from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, redirect
import os

from loginform import LoginForm
from sign_inform import Sign_inForm

app = Flask(__name__)
#run_with_ngrok(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route("/")
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = Sign_inForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('sign_in.html', title='Регистрация', form=form)


@app.route('/login2', methods=['GET', 'POST'])
def login2():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login_2.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return 'success'


#if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
