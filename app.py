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
    primes = []
    for num in range (1, number+1, 2):
        if num == 1:
            primes.append(2)
        else:
            prime = True
            for divis in range(3, num//2):
                if num % divis == 0:
                    prime = False
                    break
            if prime:
                primes.append(num)

    return render_template('primeNums.html', primes=primes)