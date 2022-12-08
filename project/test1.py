import requests

url = 'http://127.0.0.1:5000/'
myinp = {'num1': 1,'num2': 2}
x = requests.post(url, json = myinp)
print(x.text)