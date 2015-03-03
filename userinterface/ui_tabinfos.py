__author__ = '1010425'

from PySide import QtGui,QtCore

class UI_tabInfo(object):

    def __init__(self):
        self.createTabInfo()


    def createTabInfo(self):
        self.tabInfo = QtGui.QTabWidget()
        self.tabInfo.setFixedHeight(500)
        self.tabInfo.addTab(SubTConsole(),u'콘솔')
        self.tabInfo.addTab(SubTData(),u'데이터')
        self.tabInfo.addTab(SubTResult(),u'결과')

class SubTConsole(QtGui.QWidget):
    def __init__(self,parent=None):
        super(SubTConsole,self).__init__(parent)

class SubTData(QtGui.QWidget):
    def __init__(self,parent=None):
        super(SubTData,self).__init__(parent)

class SubTResult(QtGui.QWidget):
    def __init__(self,parent=None):
        super(SubTResult,self).__init__(parent)