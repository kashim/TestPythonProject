'''
Created on Mar 31, 2011

@author: kashim
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class Workplace(Base):
    __tablename__ = "opers"
    
#    proc_call_log_id = Column( Integer, primary_key=True )
#    procName = Column( "proc_name", String )
    lineNumber = Column( "place", Integer, primary_key=True )
    placeNumber = Column( "wrkplc", Integer )
    surveyCode = Column( "prg", String )
    operCode = Column( "pincode", Integer )
    regDate = Column( "reg_date", DateTime )
    interviewID = Column( "interview_id", Integer )
    ip = Column( "place_ip", String )
    phoneNumber = Column( "phone_number", String )
    isAllowHandCallNoControl = Column( "is_allow_hand_call_no_ctrl", Integer )
    clientSoftwareVersion = Column( "oper_soft_version", String )


    def __init__(self, lineNumber, placeNumber, ip):
        self.lineNumber = lineNumber
        self.placeNumber = placeNumber
        self.ip = ip
    
    def __repr__(self):
        return "lineNumber = " + str(self.lineNumber) + "; ip = " + str(self.ip) + "; current operator = " + str(self.operCode)      