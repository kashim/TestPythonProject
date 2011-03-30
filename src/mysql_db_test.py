'''
Created on Mar 31, 2011

@author: kashim
'''
from db_test_mysql.mysql_test_manager import MySQLTestManager
from db_test_mysql.dao import Workplace

if __name__ == '__main__':
    manager = MySQLTestManager()
    
    sess = manager.getNewSession()
    qryPlace = sess.query( Workplace ).order_by( Workplace.lineNumber )
    
    for rec in qryPlace.all():
        print repr( rec );
        print ""
    
    sess.close()
    print "session closed"