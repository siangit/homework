from flask import Flask, render_template, request

app = Flask(__name__)

# 첫 번째 블루프린트
my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/hello')
def hello():
    return "Hello from my blueprint!"

@my_blueprint.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

# 두 번째 블루프린트
another_blueprint = Blueprint('another_blueprint', __name__, url_prefix='/another')

# /another/world
@another_blueprint.route('/world')
def world():
    return "Hello, world, from another blueprint!"

# /another/echo
@another_blueprint.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return f"Received: {data}"

# 블루프린트에 템플릿을 사용하는 예제
@another_blueprint.route('/template')
def using_template():
    return render_template('example.html')

# 세 번째 블루프린트
third_blueprint = Blueprint('third_blueprint', __name__, url_prefix='/third')

@third_blueprint.route('/bye')
def goodbye():
    return "Goodbye from the third blueprint!"

# 애플리케이션에 블루프린트 등록
app.register_blueprint(my_blueprint)
app.register_blueprint(another_blueprint)
app.register_blueprint(third_blueprint)

if __name__ == "__main__":
    app.run(debug=True)