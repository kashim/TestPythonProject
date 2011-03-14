'''
Created on Mar 13, 2011

@author: kashim
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao import Base

class OracleTestManager(object):
    __engine = None

    def initData(self):
#        Base.metadata.create_all( self.getEngine() )
        pass
        
    
    def __init__(self):
        self.initData()
        self.__Session = sessionmaker( bind = self.getEngine() )
        print self.__engine
        pass
    
    
    def initEngine(self):
#        oracle://user:pass@host:port/dbname[?key=value&key=value...]
        self.__engine = create_engine('oracle://ap_user:1@62.149.9.103:1521/XE', echo=True)
        
        return 
    def getEngine(self):
        if self.__engine is None:
            self.initEngine()
        
        return self.__engine
    
    def getNewSession(self):
        return self.__Session()
    
    def createInitialDB(self):
        pass
#        test = UserDAO("name", "Cool Full Name", "Password")
#        test2 = UserDAO( "second", "Second Name", "pass" )
#        test3 = UserDAO( "first", "First Name", "111pass" )
#        test.address = [ AddressDAO( "top@secret.com" ), AddressDAO( "sercret@top.com" ) ]
#        test2.address = [ AddressDAO( "mail@secret.com" ), AddressDAO( "mail@top.com" ) ]
#
#        currSession = self.getNewSession()
#        currSession.add_all( [test, test2, test3] )
#        currSession.commit()
