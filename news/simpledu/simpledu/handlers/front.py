from flask import Blueprint, render_template
from simpledu.models import Course
from simpledu.forms import LoginForm, RegisterForm
from flask import flash
from flask import redirect, url_for


front = Blueprint('front', __name__)


@front.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)


@front.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@front.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash("注册成功,请登录！", "success")
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)