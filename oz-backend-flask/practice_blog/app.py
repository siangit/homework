# 웹사이트 만들기위한 도구
from flask import Flask
# API 만드는 도구 (웹사이트 커뮤니케이션)
from flask_smorest import Api
#DB 연결
from flask_mysqldb import MySQL
#html(웹페이지 디자인)
from flask import render_template
from posts_routes import create_posts_blueprint

# db.yaml에 연결
import yaml

app = Flask(__name__)

# db에 app연동

db_info = yaml.load(open('db.yaml'),Loader=yaml.FullLoader)
app.config["MYSQL_HOST"] = db_info['mysql_host']
app.config["MYSQL_USER"] = db_info['mysql_user']
app.config["MYSQL_PASSWORD"] = db_info['mysql_password']
app.config["MYSQL_DB"] = db_info['mysql_db']

# mysql 불러오기
mysql = MySQL(app)

# blueprint 설정하기
app.config['API_TITLE'] = 'Blog API List'
app.config['API_VERSION'] = '1.0'
app.config['OPENAPI_VERSION'] = '3.1.3'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

api=Api(app)
posts_blp = create_posts_blueprint(mysql)
api.register_blueprint(posts_blp)
# route 웹 페이지 링크접속 만들기
@app.route('/blog')
def manage_blog():
    return render_template("posts.html")

if __name__ == "__main__":
    app.run(debug=True)