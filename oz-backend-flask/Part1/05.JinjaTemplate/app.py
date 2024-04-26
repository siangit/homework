from flask import Flask, render_template
#it's easy to create the web page through python
#render_template is smoothe to make the html in flask
#since i called out  the flask class, i need to initialize the variables.
app = Flask(__name__)

#route is for the user who want to move to the exact url directly with the url address
@app.route("/")
def index():
    data = {
        'title':'Flask Jinja Template',
        'user':'sian',
        # if it is true, that means that the user has the admin previliage
        'is_admin':True,
        'items_list': ["Item1","Item2","Item3"]
    }
    # 1. rendering할 html 파일명 입력
    # 2. html로 넘겨줄 데이터 입력
    return render_template('index.html',data=data)



@app.route("/users")
def users():
    users = {
    "username_list": ["traveler","photographer" ,"gourmet"], 
    "name_list": ["Alex","Sam","Chris"]
    }

    return render_template('index.html',users=users)
    
if __name__ == "__main__":
    app.run(debug=True, port=5001)