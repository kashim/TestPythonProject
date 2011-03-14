'''
Created on Feb 8, 2011

@author: kashim
'''

from sqlalchemy.orm import mapper, joinedload, contains_eager
from db_test.dao import UserDAO, AddressDAO
from db_test.dm_my import DbMainTest
    

if __name__ == '__main__':
    print "this is db test"
    myDBTester = DbMainTest()
    myDBTester.createInitialDB()
    sess = myDBTester.getNewSession()

    
#    mapper(UserDAO, myDBTester.getUserTable())

    i = 1
    queryUsr = sess.query(UserDAO).order_by(UserDAO.name)
    queryAddress = sess.query(AddressDAO).order_by( AddressDAO.email )
    print "count of users = " +  str(queryUsr.count())
    print "count of addresses = " + str(queryAddress.count())
    for val in queryUsr:
        print "iteration #" + str(i)
        print val.name 
        i = i + 1
        
    print "before queryUsr.first().address"
    print queryUsr.first().address
    print "before queryAddress.all()"
    print queryAddress.all()

    queryTotal = sess.query( UserDAO ).options( joinedload( "address" ) ).all()
    print "queryTotal to run"
    print queryTotal

    queryJoin = sess.query(UserDAO, AddressDAO).filter( AddressDAO.user_id == UserDAO.id ).filter( AddressDAO.email == "mail@secret.com" )

    print "queryJoin to run"
    i = 0
    for u, a in queryJoin.all():
        print "User - %s \nAddress - %s" % (u ,a)
        i = i + 1
        print i

    queryJoin2 = sess.query(UserDAO).join(AddressDAO).filter( AddressDAO.email == "mail@secret.com" ).options(contains_eager(UserDAO.address))
#    queryJoin2 = sess.query(UserDAO, AddressDAO).filter( AddressDAO.user_id == UserDAO.id ).filter( AddressDAO.email == "mail@secret.com" )
    print "queryJoin2 to run"
    i = 0
    for u in queryJoin2.all():
        print "User - %s \nAddress - %s" % (u, 12)
        i = i + 1
        print i

    print "users before delete"
    print queryUsr.all()
    print "Addresses before delete"
    print queryAddress.all()

    firstUser = queryUsr.filter( UserDAO.address.any() ).first()
    sess.delete(firstUser)

    print "users after delete"
    print queryUsr.all()
    print "Addresses after delete"
    print queryAddress.all()
