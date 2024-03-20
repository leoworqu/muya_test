from flask import Flask, render_template, url_for, flash, redirect
from forms import registrationForm, loginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '46af1a55a3a3992bdb12d4658e9a96e7'


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = registrationForm()
    if form.validate_on_submit():
        flash(f'Account succesfully created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template("register.html", form=form)


@app.route("/login",  methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        flash('Loggged in succesfully' , 'success')
        return redirect(url_for('index'))
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")