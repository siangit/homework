from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

book_blp = Blueprint("books", "books", url_prefix="/books", description="Operations on books")

books = []

@book_blp.route("/")
class BookList(MethodView):
    @book_blp.response(200)
    def get(self):
        # 모든 아이템을 반환하는 GET 요청 처리
        return books

    @book_blp.arguments(BookSchema)
    @book_blp.response(201, description="Book added")
    def post(self, new_data):
        # 새 아이템을 추가하는 POST 요청 처리
        books.append(new_data)
        return new_data

# 'Item' 클래스 - GET, PUT, DELETE 요청을 처리
@book_blp.route("/<int:book_id>")
class Book(MethodView):
    @book_blp.response(200)
    def get(self, book_id):
        # 특정 ID를 가진 아이템을 반환하는 GET 요청 처리
				# next() => 반복문에서 값이 있으면 값을 반환하고 없으면 None을 반환
				# next는 조건을 만족하는 첫 번째 아이템을 반환하고, 그 이후의 아이템은 무시합니다.
        book = next((book for book in books if book["id"] == book_id), None)
        if book is None:
            abort(404, message="Item not found")
        return book

    @book_blp.arguments(BookSchema)
    @book_blp.response(200, description="Book updated")
    def put(self, new_data, book_id):
        # 특정 ID를 가진 아이템을 업데이트하는 PUT 요청 처리
        book = next((book for book in books if book["id"] == book_id), None)
        if book is None:
            abort(404, message="Item not found")
        book.update(new_data)
        return book

    @book_blp.response(204, description="Book deleted")
    def delete(self, book_id):
        # 특정 ID를 가진 아이템을 삭제하는 DELETE 요청 처리
        global books
        if not any(book for book in books if book["id"] == book_id):
            abort(404, message="Item not found")
        books = [book for book in books if book["id"] != book_id]
        return ''