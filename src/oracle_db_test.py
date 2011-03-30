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
   
    qryAllData = sess.query( ProcCallLog ).order_by( ProcCallLog.callDate.desc() )
    print "Tatal record count"
    print qryAllData.count()
    print "limit test"
    i = 0
    for rec in qryAllData[1:5]:
        print "iteration num = " + str(i)
        print rec
        i = i + 1
    
#NLS_LANG="AMERICAN_AMERICA.CL8MSWIN1251"
#     
#    print os.environ["DYLD_LIBRARY_PATH" ]
#    con = cx_Oracle.connect('access_panel/1@62.149.9.103:1521/XE')
#    print con.version
##    con.close()