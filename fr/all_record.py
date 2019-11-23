/*
SELECT
WHERE
LIMIT
IN 
ORDER BY
Distinct
JOIN
LEFT JOIN
UNION
UNION ALL
sql_statement
INSERT 
UPDATE
DELETE
select

*/

users = session.query(User.name, User.email).all()

for user in users:
  print(user.name)


users = session.query(User).\
        filter(User.name=="name")/\
        all()

for user in users:
    print(user.name, user.age)


user_name = session.query(User).\
        limit(10).\
        all()


names = ['tky', 'tkgcci', 'takagotch']
brothers = session.query(User).\
        filter(names).\
        all()

from sqlalchemy import desc

users = session.query(User).\
        order_by(desc(User.created_at)).\
        all()

from sqlalchemy import distinct

user_name = session.query(User).\
        distinct(User.name).\
        all()

from sqlalchemy import distinct

user_name = session.query(distinct(User.name)).\
        all()


user_name = session.query(User, UserSocial).\
        join(UserSocial, User.id==UserSocial.user_id).\
        all()

user_name = session.query(User, UserSocial).\
        outerjoin(UserSocial, User.id==UserSocial.user_id).\
        all()

tag_genre = session.query(Tag).\
        union(session.query(Genre)).\
        all()

tag_genre = session.query(Tag).\
        union_all(session.query(Genre)).\
        all()

user_name = session.query(User)
sql_statement = user_name.statement
print(sql_statement)


user_name = User()
user_name.name = 'tky'
session.add(user_name)
session.commit()


user_name = session.query(User).\
        filter(User.id==1).\
        first()
    user_name.name = 'tky'
    session.commit()


session.query(User).\
    filter(User.id==1).\
    delete()
session.commit()


user_id = 1
sql = "select name from users where id = %s" % (user_id)
res = session.execute(sql)

for v in res:
     print(v.name)


users = session.query(User).limit(100)

for user in users:
    print(user.name)





