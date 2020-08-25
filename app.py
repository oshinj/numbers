from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'SAP SVNT Tech Interview'

@app.route('/<int:number>')
def displayInts(number):
    return render_template('allNums.html', number=number)

@app.route('/<int:number>/odd')
def displayOdd(number):
    return render_template('oddNums.html', number=number)

@app.route('/<int:number>/prime')
def displayPrime(number):
    return render_template('primeNums.html', number=number)