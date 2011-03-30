'''
Created on Mar 31, 2011

@author: kashim
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class MySQLTestManager(object):
    __engine = None

    def __init__(self):
#        self.initData()
        self.__Session = sessionmaker( bind = self.getEngine() )
        print self.__engine
    
    def initEngine(self):
        #mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
        self.__engine = create_engine('mysql+mysqldb://remote_root:123123@192.168.56.101:3306/tel_number', echo=True)
        
        return 
    def getEngine(self):
        if self.__engine is None:
            self.initEngine()
        
        return self.__engine
    
    def getNewSession(self):
        return self.__Session()
    
    def createInitialDB(self):
        pass
