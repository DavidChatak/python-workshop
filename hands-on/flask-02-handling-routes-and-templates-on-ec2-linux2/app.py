from flask import Flask, url_for,redirect, render_template
app=Flask(__name__)

@app.route('/')
def home():
    return "this is home page for no path <h1> Welcome Home </h1>"
@app.route('/about')
def about():
    return '<h1> This is my about page </h1>'
@app.route('/error')
def error():
    return ' <h1> error page: you..... </h1>'

@app.route('/hello')
def hello():
    return '<h1>hello world </h1>'
@app.route('/admin')
def admin():
    return redirect(url_for('error'))
# @app.route('/<name>')
# def greet(name):
#     greet_format=f"""
#     <!DOCTYPE html>
# <html>
# <head>
#     <title>Greeting Page</title>
# </head>
# <body>
#     <h1>Hello, { name }!</h1>
#     <h1>Welcome to my Greeting Page</h1>
# </body>
# </html>
# """
#     return greet_format
@app.route('/<username>')
def greet(username):
    return render_template('greet.html',name=username)

@app.route('/list10:<n>')
def list10(n):
    n=int(n)
    return render_template('list10.html',x=n)

@app.route('/evens')
def evens():
    return render_template('evens.html')



@app.route('/greet_admin')
def greet_admin():
    return redirect(url_for('greet',name='Master Admin'))

if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
