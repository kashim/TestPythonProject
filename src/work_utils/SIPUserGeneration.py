__author__="kashim"
__date__ ="$Oct 31, 2010 8:58:34 PM$"

#[asip7867]


def generateSIPUser(userNum):
    print "[asip" + str( userNum ) + "]"
    print "type=friend"
    print "secret=asip" + str( userNum )
    print "nat=yes"
    print "host=dynamic"
    print "username=asip" + str( userNum )
    print "dtmfmode=rfc2833"
    print "disallow=all"
    print "allow=gsm"
    print "context=default_sip"
    print "callerid=" + str( userNum )
    print ""

def generateRangeUser(startNum, endNum):
    for i in range( startNum, endNum + 1 ):
        generateSIPUser(i)


