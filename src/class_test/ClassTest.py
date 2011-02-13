
__author__="kashim"
__date__ ="$Aug 29, 2010 6:20:23 PM$"

class BaseClass:
    
    def __init__(self, mainCaption=""):
        self._mainCaption = ""
        self._item4Test = "item for test"
        self._mainCaption = mainCaption

    def getMainCaption(self):
        return self._mainCaption

    def __getitem__(self, key):
        return self._item4Test
    def __setitem__(self, key, item):
        self._item4Test = item;

class MyTestClass( BaseClass ):
    def __init__(self, caption="", mainCaption=""):
        BaseClass.__init__( self, mainCaption )
        self._caption = caption

    def getCaption(self):
        return self._caption + " " + self.getMainCaption() + " " + self.__testPrivateMethod()
    def __testPrivateMethod(self):
        return "testPrivateMethod"