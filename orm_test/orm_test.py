from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__='test1'

    id=Column(String(20),primary_key=True)
    username=Column(String(20))

engine=create_engine('mysql+pymysql://root:password@localhost:3306/test')

DBSession=sessionmaker(bind=engine)

# session=DBSession()
# new_user=User(id='8',username='Bob2')
# session.add(new_user)
# session.commit()
# session.close()

session=DBSession()
user =session.query(User).filter(User.id=='2').one()
print('type:',type(user))
print('name:',user.username)
session.close()