from flask import Flask
from flask_jwt_extended import JWTManager
from flask import render_template
from routes.user import user_blp

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'

jwt = JWTManager(app)
app.register_blueprint(user_blp, url_prefix='/user')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)