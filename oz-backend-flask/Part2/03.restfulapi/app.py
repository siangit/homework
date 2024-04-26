from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# 간단한 DB 역할
items = []

class Item(Resource):
    # 특정 아이템 조회
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {"msg": "item not found"}, 404

    # 특정 아이템 생성
    def post(self, name):
        for item in items:
            if item['name'] == name:
                return {"msg": "item already exists"}, 400  # 수정됨
    
        data = request.get_json()
        new_item = {'name': name, 'price': data['price']}  # name은 URL로부터 직접 받아온 값으로 사용
        items.append(new_item)  # 오타 수정됨
        return new_item, 201  # 생성된 아이템과 함께 201 Created 상태 코드 반환

    # 특정 아이템 업데이트
    def put(self, name):
        data = request.get_json()
        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return item
    
        new_item = {'name': name, 'price': data['price']}
        items.append(new_item)  # 오타 수정됨
        return new_item, 201  # 새로운 아이템이 생성되었을 때 201 Created 반환

    # 특정 아이템 삭제
    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        return {"msg": "Item deleted"}

# 경로 추가
api.add_resource(Item, '/item/<string:name>')

if __name__ == "__main__":
    app.run(debug=True)
