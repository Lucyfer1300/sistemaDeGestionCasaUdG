from flask import Flask, render_template, request, redirect, url_for, flash

from flask_mysqldb import MySQL

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


# iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)
# --------------
