from app import app

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

@app.route('/hello')
def hello():
    return "Hello world"

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)

