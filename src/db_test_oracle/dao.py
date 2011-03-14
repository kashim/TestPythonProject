'''
Created on Mar 13, 2011

@author: kashim
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()
SCHEMA_NAME = "access_panel"


class ProcCallLog(Base):
    __tablename__ = "access_panel.proc_call_log"
    
    proc_call_log_id = Column( Integer, primary_key=True )
    proc_name = Column( String )
    call_date = Column( DateTime )
    param_str = Column( String )
    out_param_str = Column( String )
    error_str = Column( String )
    
    def __init__(self, procName, callDate, paramStr, outParamStr, errorStr):
        self.proc_name = procName
        self.call_date = callDate
        self.param_str = paramStr
        self.out_param_str = outParamStr
        self.error_str = errorStr