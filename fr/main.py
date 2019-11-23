from setting import session

from user import *

user = User()
user.name = 'tky'
session.add(user)
session.commit()

users = session.query(User).all()
for user in users:
  print(user.name)







