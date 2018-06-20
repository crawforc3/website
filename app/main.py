from flask import Flask
from flask import render_template
#from config import Config
#from forms import LoginForm


app = Flask(__name__)
#app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dave'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='redpony', user=user, posts=posts)


#@app.route('/login')
#def login():
#    form = LoginForm()
#    return render_template('login.html', title='Sign in', form=form)


@app.route('/hello')
def hello():
    return "Hello world"

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
