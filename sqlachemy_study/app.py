from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

# user = User(name="Sian Lee", age=30)
# user_2 = User(name="승현", age=28)
# user_3 = User(name="성우", age=30)
# user_4 = User(name="준호", age=29)

#create database
# session.add_all([user_2,user_3,user_4])

# session.commit()


users = session.query(User).all()
user = users[0]

print(user.id)
print(user.name)
print(user.age)