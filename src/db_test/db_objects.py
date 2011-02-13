'''
Created on Feb 12, 2011

@author: kashim
'''
from sqlalchemy import Table, Column, String, Integer

_user_table = None
_address_table = None

def createUserTable(metaData):
    _user_table = Table(
                    'users', metaData,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('fullName', String),
                    Column('password', String)
              )
    
    
    return

def getUserTable():
    return _user_table
