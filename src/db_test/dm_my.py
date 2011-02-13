'''
Created on Feb 11, 2011

@author: kashim
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao import Base
from db_test.dao import UserDAO, AddressDAO

class DbMainTest:
    __engine = None

    def initData(self):
#        db_objects.createUserTable( self.__metaData )
        Base.metadata.create_all( self.getEngine() )
#        self.__metaData.create_all( self.getEngine() )
        
    
    def __init__(self):
        self.initData()
        self.__Session = sessionmaker( bind = self.getEngine() )
        print self.__engine
        pass
    
    
    def initEngine(self):
        self.__engine = create_engine('sqlite:///:memory:', echo=True)
        
        return 
    def getEngine(self):
        if self.__engine is None:
            self.initEngine()
        
        return self.__engine
    
    def getNewSession(self):
        return self.__Session()
    
    def createInitialDB(self):
        test = UserDAO("name", "Cool Full Name", "Password")
        test2 = UserDAO( "second", "Second Name", "pass" )
        test3 = UserDAO( "first", "First Name", "111pass" )
        test.address = [ AddressDAO( "top@secret.com" ), AddressDAO( "sercret@top.com" ) ]
        test2.address = [ AddressDAO( "mail@secret.com" ), AddressDAO( "mail@top.com" ) ]

        currSession = self.getNewSession()
        currSession.add_all( [test, test2, test3] )
        currSession.commit()
