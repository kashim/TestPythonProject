'''
Created on Feb 8, 2011

@author: kashim
'''

from sqlalchemy.orm import mapper
from db_test.dao import UserDAO, Address
from db_test.dm_my import DbMainTest
    

if __name__ == '__main__':
    print "this is db test"
    myDBTester = DbMainTest()
    myDBTester.createInitialDB()
    sess = myDBTester.getNewSession()

    
#    mapper(UserDAO, myDBTester.getUserTable())

    i = 1
    queryUsr = sess.query(UserDAO).order_by(UserDAO.name)
    queryAddress = sess.query(Address).order_by( Address.email )
    print "count of users = " +  str(queryUsr.count())
    print "count of addresses = " + str(queryAddress.count())
    for val in queryUsr:
        print "iteration #" + str(i)
        print val.name 
        i = i + 1
        
    print queryUsr.first().address
    print queryAddress.all()