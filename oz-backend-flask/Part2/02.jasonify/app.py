#server 준비
from flask import Flask, jsonify, request

app = Flask(__name__)


#1. 전체 게시글을 불러오는 API (read)
    #GET
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    data = {'result':'success', 'data':{'feed1':'data1','feed2':'data2'}}

    #***jsonify로 () 안해줘도됨, dict 타입이라서 자동으로 변환가능
    return data


#특정 게시글을 불러오는 API
    # GET
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    data = {'result':'success', 'data':{'feed1':'data1'}}

    return data



#POST 실습
# 1. 게시글을 작성하는 API
@app.route('/api/v1/feeds', methods=['POST'])
def crerate_one_feed():
    name = request.form['name']
    age = request.form['age']

    print(name,age)

    return jsonify({'result':'success'})






datas = [{"items": [{"name":"item1", "price":10}]}]

@app.route('/api/v1/datas', methods=['GET'])
def get_datas():
    return {"datas":datas}

@app.route('/api/v1/datas', methods=['POST'])
def create_data():
    request_data = request.get_json()

    new_data = {'items': request_data.get("items",[])}
    datas.append(new_data)

    return new_data, 201




# port 겹쳐서 안될때 사용
if __name__ == "__main__":
    app.run(debug=True, port=5002)