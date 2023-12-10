from flask import Flask
from models import db, User
from flask_wtf.csrf import CSRFProtect
from flask import render_template, request
from form import LoginForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
app.config['SECRET_KEY'] = 'secret_key'
csrf = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])
@csrf.exempt
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        print(request)
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = hash(form.password.data)
        print(name, surname, email, password)
        new_user = User(name=name, email=email, password=password, surname=surname)
        db.session.add(new_user)
        db.session.commit()
        print('Пользователь добавлен в БД.')
    return render_template('login.html', form=form)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('База данных создана.')