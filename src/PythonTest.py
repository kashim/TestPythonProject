import sys

import types
import __builtin__
from pprint import pprint as pp
import work_utils.SIPUserGeneration
import ClassTest
from test_array import testMod

__author__="kashim"
__date__ ="$Aug 18, 2010 12:46:16 AM$"

def procMapTest():
    print "-----procMapTest()-----"
    tmp = "print full map: " + repr(testMod.getMap())
    print tmp
    print len(tmp)
    print "print \"key1\""
    print testMod.getMap()["key1"]
    print "print keys"
    print testMod.getMap().keys()
    print "print values"
    print testMod.getMap().values()
    print "print items"
    print testMod.getMap().items()
    print "join"
    print [ "pair - %s=%s" % ( i, j ) for i, j in testMod.getMap().items() ]
    
#    return;

def procListTest():
    print "list test"
    lst = testMod.getList()
    print lst[0]
    print lst
    print lst[1:]
    print [ "item=%s" % (i) for i in lst if lst.index(i) < 1 ]
#    return;

def procStringTest():
    print "s before join"
    s = u";".join([ "%s=%s" % ( i, j ) for i, j in testMod.getMap().items() ])
    print "s after join = " + s
    print "s after split"
    print s.split(";")
    print "dir test"
    tmp = dir( s )
    print tmp

def procTupleTest():
    print testMod.getTuple()
    lst = list(testMod.getTuple())
    print [ vals + "__test" for vals in lst ]

def procBuiltInTest():
    print type(testMod) == types.IntType
    print dir( __builtin__ )

def procClassTest():
    clTest = ClassTest.MyTestClass( "My Caption", "BaseCaption" )
    print clTest
    print clTest.getCaption()
    print clTest["test"]
    clTest["test"] = "txt"
    print clTest["test"]
    clTest2 = ClassTest.MyTestClass( "tmp", "tmp2" )
    print clTest2["test"]
    print clTest["test"]

if __name__ == "__main__":
    print testMod.testFunc( "My Caption" )
    print testMod.testFunc.__doc__
    print sys.path

    n = 4
    if n >= 5:
        print n
    else:
        print "n is less then 5"

    
    procMapTest()
    procListTest()
    procStringTest()
    procTupleTest()
    procBuiltInTest()
    procClassTest()
#    SIPUserGeneration.generateRangeUser(7900, 7999)
    print pp(sys.path)
    
