'''
Created on Feb 11, 2011

@author: kashim
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

#class UserDAO(object):
#    def __init__(self, name, fullName, password):
#        self.name = name
#        self.fullName = fullName
#        self.password = password
#    
#    def __repr__(self):
#        return "<User( \"%s\" \"%s\" \"%s\" )>" % ( self.name, self.fullName, self.password )

Base = declarative_base()
class UserDAO(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullName = Column(String)
    password = Column(String)
    
    address = relationship("Address", order_by = "Address.id", backref = "users")
    
    def __init__(self, name, fullName, password):
        self.name = name
        self.fullName = fullName
        self.password = password
    
    def __repr__(self):
        return "<User( \"%s\" \"%s\" \"%s\" )>" % ( self.name, self.fullName, self.password )

class Address(Base):
    __tablename__ = "address"
    id = Column( Integer, primary_key = True )
    email = Column( String )
    user_id = Column( Integer, ForeignKey( "users.id" ) )
    
    user = relationship(UserDAO, order_by = "UserDAO.id")
    
    def __init__(self, email):
        self.email = email
        
    def __repr__(self):
        return "<Address = \"%s\" >" % ( self.email )