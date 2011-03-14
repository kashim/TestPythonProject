'''
Created on Mar 13, 2011

@author: kashim
'''
from db_test_oracle.oracle_test_manager import OracleTestManager
from db_test_oracle.dao import ProcCallLog

if __name__ == '__main__':
    print "this is db test"
    myDBTester = OracleTestManager()
    myDBTester.createInitialDB()
    sess = myDBTester.getNewSession()
    print sess
    print dir(sess)
    sess.current_schema = "access_panel"
   
    queryAllData = sess.query( ProcCallLog )

    print "Tatal record count"
    print queryAllData.count()
