from app import app
from flask import render_template
from app.views.forms import LoginForm
from flask import flash
from flask import redirect

@app.route('/')
def index():
    user = {'nickname':'zuodw'} # fake user
    return render_template('index.html', title='Home', user=user)

@app.route('/posts')
def post():
    user = {'nickname':'fanhx'}
    posts = [{'author':{'nickname':'Sylar'}, 'body':'Beautiful day inPortland!'},
             {'author':{'nickname':'Peter'}, 'body':'The Avengers movie was so cool!'},
             {'author':{'nickname':'Susan'}, 'body':'I am so bueatiful!'}]
    return render_template('posts.html', title='Posts', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('username="' + form.username.data + '",password=' + str(form.password.data))
        return redirect('/')
    else:
        return render_template('login.html', title='Sign In', form=form)