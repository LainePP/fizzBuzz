from flask import Flask, jsonify, Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/fizzbuzz')
def fizzbuzz():
    lista = list(metodo_fizz_buzz(1, 100))
    return jsonify({'lista': lista})

def metodo_fizz_buzz(inicio, fim):
    for i in range(inicio, fim+1):
        if i%15 == 0:
            yield 'FizzBuzz'
        elif i%5 == 0:
            yield 'Buzz'
        elif i%3 == 0:
            yield 'Fizz'
        else:
            yield i

if __name__ == '__main__':
    app.run()