from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():

    return render_template('index.html')

@app.route('/blog')
def blog():
    return 'These  are my thoughts'

@app.route('/submit_form',methods=['POST','GET'])
#@app.route('/favicon.ico')
#def blog():
 #   return 'These  are my thoughts'
