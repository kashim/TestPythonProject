'''
Created on Jun 23, 2011

@author: kashim
'''

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MyServerHandler(BaseHTTPRequestHandler):
    '''
    classdocs
    '''

    def do_GET(self):
        print "do_GET is called " + self.path

    def do_POST(self):
        print "do_POST is called"
        pass
    
def main():
    try:
        server = HTTPServer(("", 8899), MyServerHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print "Keyboard interrupted"
        server.socket.close()
        
if __name__ == "__main__":
    main()