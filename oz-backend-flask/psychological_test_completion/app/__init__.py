from flask import Flask
from flask_migrate import Migrate
from flask.cli import with_appcontext
import os
import click
from .database import db
from .models import Question, Admin, User, Participant  # Question 모델 임포트
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta


def create_app():
    app = Flask(__name__)
    app.secret_key = "oz_coding_secret"

    # 데이터베이스 파일 경로 설정 및 앱 설정
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    dbfile = os.path.join(basedir, "db.sqlite")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + dbfile
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # 데이터베이스 및 마이그레이션 초기화
    db.init_app(app)
    migrate = Migrate(app, db)

    # 라우트(블루프린트) 등록
    from .routes import main as main_blueprint
    from .routes import admin as admin_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(admin_blueprint)

    # 초기화 명령어 정의
    def add_initial_questions():
        initial_questions = [
            "다른사람이 울고있는 모습을 보면 자신도 울고 싶어질때가 많다.",
            "단체에서 지도자 역할을 맡는일은 가능한 피하고싶다.",
            "자신만큼 효율적이지 못한 사람을 보면 짜증이 난다",
            "다른사람의 감정을 이해하기 힘들떄가 많다.",
            "자신보다 다른사람에게 더 필요한 기회라고 생각되면 기회를 포기할수있다.",
            "자신의 의견과 매우 다른 의견을 이해하기 위해 많은 시간을 할애하곤한다"
        ]
        yesterday = datetime.utcnow() - timedelta(days=1)  # 어제 날짜 계산

        existing_main = User.query.filter_by(username="sian").first()
        if not existing_main:
            hashed_password = generate_password_hash("best")  # 비밀번호를 해시 처리
            new_main = User(username="sian", password=hashed_password)
            db.session.add(new_main)

        # 관리자 계정 추가 로직, 비밀번호 해시 처리 적용
        existing_admin = Admin.query.filter_by(username="admin").first()
        if not existing_admin:
            hashed_password = generate_password_hash("1111")  # 비밀번호를 해시 처리
            new_admin = Admin(username="admin", password=hashed_password)
            db.session.add(new_admin)

        participants_without_created_at = Participant.query.filter(
            Participant.created_at == None
        ).all()

        for participant in participants_without_created_at:
            participant.created_at = yesterday

        for question_content in initial_questions:
            existing_question = Question.query.filter_by(
                content=question_content
            ).first()
            if not existing_question:
                new_question = Question(content=question_content)
                db.session.add(new_question)
        questions = Question.query.all()
        for question in questions:
            question.order_num = question.id
            question.is_active = True  # 모든 질문을 활성화 상태로 설정
        db.session.commit()

    @click.command("init-db")
    @with_appcontext
    def init_db_command():
        db.create_all()
        add_initial_questions()
        click.echo("Initialized the database.")

    app.cli.add_command(init_db_command)

    return app
