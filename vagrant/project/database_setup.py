import sys
from sqlalchemy import Column , ForeignKey , Integer , String
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

class Restaurent(Base):
    __tablename__ = 'restaurent'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    prise = Column(String(8))
    restaurent_id = Column(Integer, ForeignKey('restaurent.id'))
    restaurent = relationship(Restaurent)


engine = create_engine('sqlite:///restaurentmenu.db')
Base.metadata.create_all(engine)
