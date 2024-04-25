from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, This is Main Page!"

@app.route('/about')
def about():
    return "Hello, This is about Page!"

# 동적으로 url parameter value를 받아서 처리
# http://127.0.0.1:5001/user/sian
@app.route('/user/<username>')
def user_profile(username):
    return f'UserName: {username}'


@app.route('/number/<int:number>')
def number(number):
    return f'number: {number}'


#post 요청 날리기
# 1. postman
# 2. requests
import requests  #pip install requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5001/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)

    return "success"


@app.route('/submit', methods=['GET','POST','PUT','DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET method")
  
    if request.method == 'POST':
        print("***POST method",request.data)

    return ' '



if __name__ == '__main__':
    app.run(debug=True, port=5001)