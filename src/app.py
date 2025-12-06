from flask import Flask
from flask import request
import math

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello World!'

@app.route('/calc_rect', methods=['GET'])
def calc_square_rect():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return 'a и b - НЕ числа'
    return str(a * b)

@app.route('/calc_triangle', methods=['GET'])
def calc_square_triangle():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        c = float(request.args.get('c'))
    except (TypeError, ValueError):
        return 'a, b, c - НЕ числа'
    
    if (a + b < c or a + c < b or b + c < a):
        return 'такого треугольника не существует'
    
    p = (a + b + c) / 2
    return str(math.sqrt(p*(p-a)*(p-b)*(p-c)))

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()