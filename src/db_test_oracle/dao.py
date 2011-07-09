'''
Created on Mar 13, 2011

@author: kashim
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class ProcCallLog(Base):
    __tablename__ = "proc_call_log"
    __schema__ = "access_panel"
    
    proc_call_log_id = Column( Integer, primary_key=True )
    procName = Column( "proc_name", String )
    callDate = Column( "call_date", DateTime )
    paramStr = Column( "param_str", String )
    outParamStr = Column( "out_param_str", String )
    errorStr = Column( "error_str", String )
    
    def __init__(self, procName, callDate, paramStr, outParamStr, errorStr):
        self.proc_name = procName
        self.call_date = callDate
        self.param_str = paramStr
        self.out_param_str = outParamStr
        self.error_str = errorStr
        
    def __repr__(self):
        return "proc_call_log: proc_name=" + self.procName + " call_date=" + str( self.callDate )