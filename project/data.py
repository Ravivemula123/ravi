from flask import * 
app =Flask(__name__)

@app.route ('/')
def data1():
    num1=int(request.json['num1'])
    num2=int(request.json['num2'])
    return f'the sum of{num1} and {num2} is {num1+num2} dfgg'
if __name__ == '__main__':
    app.run(debug=True)
