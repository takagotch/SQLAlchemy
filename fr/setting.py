from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
  "user_name",
  "password",
  "host_ip",
  "db_name",
)
ENGINE = create_engine(
  DATABASE,
  encoding = "utf-8",
  echo=TRUE
)

session = scoped_session(
  sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = ENGINE
  )        
)

Base = declarative_base()
Base.query = session.query_property()



