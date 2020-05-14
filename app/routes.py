from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mike'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'GOd i just had the biggest poop of my life'
        },
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'GOd i just had the biggest poop of my life'
        },
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'GOd i just had the biggest poop of my life'
        } ,
        {
            'author': {'username': 'Susan'},
            'body': 'GOd i just had the biggest poop of my life'
        },
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'GOd i just had the biggest poop of my life'
        },
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'GOd i just had the biggest poop of my life'
        }                

    ] 
    return render_template('index.html', title='Home', user=user, posts=posts)

