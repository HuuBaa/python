# -*- coding:utf-8 -*-

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey
import pymysql.cursors

# 生成基类
Base = declarative_base()
# 创建数据库连接

# 创建表
conn = pymysql.connect(host = 'localhost', user='root', password='password', database='test')
cursor = conn.cursor()
cursor.execute('create table if not exists userspy (id INTEGER PRIMARY KEY, name VARCHAR(20))')
cursor.execute('create table if not exists book (id INTEGER PRIMARY KEY, name VARCHAR(20), user_id INTEGER )')
cursor.close()

# 定义User
class User(Base):
    __tablename__ = 'userspy'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    books = relationship('Book')
# 定义Book
class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    user_id = Column(Integer, ForeignKey('userspy.id'))

engine = create_engine('mysql+pymysql://root:password@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()
#创建新User对象
bob = User(id=1,name='Bob')
session.add(bob)
session.commit()
#创建新Book对象
new_book_1 = Book(id=1,name='Book1',user_id = 1)
session.add(new_book_1)
session.commit()
new_book_2 = Book(id=2,name='Book2',user_id = 1)
session.add(new_book_2)
session.commit()
session.close()

session = DBSession()
user = session.query(User).all()
print(user[0].books)
session.close()