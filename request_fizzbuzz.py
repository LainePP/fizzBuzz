import requests
import json

def request_fizzbuzz():
    dados = requests.get('http://127.0.0.1:5000/fizzbuzz')
    lista = json.loads(dados.content.decode('utf8').replace("'", '"'))
    par = 0
    impar = 0
    fizz = 0
    buzz = 0
    fizzbuzz = 0
    for i in lista['lista']:
        if type(i) is str:
            if i == 'Fizz':
                fizz += 1
            elif i == 'Buzz':
                buzz += 1
            elif i == 'FizzBuzz':
                fizzbuzz += 1
        else:
            if i%2 == 0:
                par += 1
            else:
                impar += 1

    print("Quantidades pares: ", par)
    print("Quantidades impares: ", impar)
    print("Quantidades fizz: ", fizz)
    print("Quantidades buzz: ", buzz)
    print("Quantidades fizzbuzz: ", fizzbuzz)

if __name__ == '__main__':
    request_fizzbuzz()