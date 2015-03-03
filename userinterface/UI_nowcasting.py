__author__ = '병천'

import sys
from PySide import QtGui, QtCore

from userinterface.ui_tabinfo import UI_tabInfo

class UiNowcasting(QtGui.QDialog):

    def __init__(self):
        super(UiNowcasting,self).__init__()

        self.tabs = UI_tabInfo()

        self.setFixedWidth(700)
        self.setFixedHeight(900)
        self.createMenu()
        self.createGridLayoutTop()

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.setMenuBar(self.menuBar)
        mainLayout.addLayout(self.lOutTop)

        self.setLayout(mainLayout)
        self.setWindowTitle("Nowcasting Simulator, Bank of Korea")

    def createMenu(self):
        self.menuBar = QtGui.QMenuBar()

        self.fileMenu = QtGui.QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("E&xit")
        self.menuBar.addMenu(self.fileMenu)

        self.exitAction.triggered.connect(self.accept)

    def createGridLayoutTop(self):
        self.lOutTop = QtGui.QGridLayout()
        _label1 = QtGui.QLabel(u'Nowcasting 지표')
        _label2 = QtGui.QLabel(u'Nowcasting 시점')
        self.cmbDepIdx = QtGui.QComboBox()
        self.txaNwcDate = QtGui.QDateEdit()
        self.btnExec = QtGui.QPushButton('GO');self.btnExec.setFixedWidth(100)
        self.lOutTop.addWidget(_label1,0,0)
        self.lOutTop.addWidget(_label2,1,0)
        self.lOutTop.addWidget(self.cmbDepIdx,0,1)
        self.lOutTop.addWidget(self.txaNwcDate,1,1)
        self.lOutTop.addWidget(self.btnExec,1,2,1,3)
        self.lOutTop.addWidget(self.createPeriodGBox(),2,0,4,1)
        self.lOutTop.addWidget(self.createTrrGBox(),2,1,4,2)
        self.lOutTop.addWidget(self.createEveGBox(),2,3,5,2)
        self.lOutTop.addWidget(self.createRlUpGBox(),6,0,8,1)
        self.lOutTop.addWidget(self.createAglmGBox(),6,1,8,2)
        self.lOutTop.addWidget(self.createTrSlrGBox(),7,3,7,2)
        self.lOutTop.addWidget(self.tabs.tabInfo,14,0,10,5)



    def createPeriodGBox(self):
        periodGroupBox = QtGui.QGroupBox(u'[변수주기]')
        _layout = QtGui.QVBoxLayout()
        self.chkPrdDd = QtGui.QCheckBox('Daily')
        self.chkPrdWw = QtGui.QCheckBox('Weekly')
        self.chkPrdMm = QtGui.QCheckBox('Monthly')
        _layout.addWidget(self.chkPrdDd)
        _layout.addWidget(self.chkPrdWw)
        _layout.addWidget(self.chkPrdMm)
        periodGroupBox.setLayout(_layout)
        return periodGroupBox

    def createTrrGBox(self):
        _trainingGroupBox = QtGui.QGroupBox(u'[훈련옵션]')
        _layout = QtGui.QGridLayout()
        _label1 = QtGui.QLabel(u'1회당 실험수');_layout.addWidget(_label1,0,0,2,2)
        _label2 = QtGui.QLabel(u'평균설명변수(확률)');_layout.addWidget(_label2,0,2,2,2)
        _label3 = QtGui.QLabel(u'회');_layout.addWidget(_label3,1,1,2,1)
        _label4 = QtGui.QLabel(u'개');_layout.addWidget(_label4,1,3,2,1)
        self.txaGenCnt = QtGui.QLineEdit();_layout.addWidget(self.txaGenCnt,1,0,2,1)
        self.txaAvgVars = QtGui.QLineEdit();_layout.addWidget(self.txaAvgVars,1,2,2,1)
        _trainingGroupBox.setLayout(_layout)
        return _trainingGroupBox

    def createEveGBox(self):
        _evolveProcessGroupBox = QtGui.QGroupBox(u'[진화프로세스]')
        _layout = QtGui.QGridLayout()
        _label1 = QtGui.QLabel(u'(1회 실험 후 결과값 처리기준)');_layout.addWidget(_label1,0,0,1,3)
        _label2 = QtGui.QLabel(u'버림:하위');_layout.addWidget(_label2,1,0,1,1)
        _label3 = QtGui.QLabel(u'남김:상위');_layout.addWidget(_label3,2,0,1,1)
        _label4 = QtGui.QLabel(u'신규 추출');_layout.addWidget(_label4,3,0,1,1)
        _label5 = QtGui.QLabel(u'진화 횟수');_layout.addWidget(_label5,4,0,1,1)
        self.txaCutoffPct = QtGui.QLineEdit();_layout.addWidget(self.txaCutoffPct,1,1,1,1)
        self.txaRetainPct = QtGui.QLineEdit();_layout.addWidget(self.txaRetainPct,2,1,1,1)
        self.txaNewChromePct = QtGui.QLineEdit();_layout.addWidget(self.txaNewChromePct,3,1,1,1)
        self.txaPopulationPct = QtGui.QLineEdit();_layout.addWidget(self.txaPopulationPct,4,1,1,1)
        _label6 = QtGui.QLabel('%');_layout.addWidget(_label6,1,2,1,1)
        _label7 = QtGui.QLabel('%');_layout.addWidget(_label7,2,2,1,1)
        _label8 = QtGui.QLabel('%');_layout.addWidget(_label8,3,2,1,1)
        _label9 = QtGui.QLabel(u'회');_layout.addWidget(_label9,4,2,1,1)
        _evolveProcessGroupBox.setLayout(_layout)
        return _evolveProcessGroupBox

    def createRlUpGBox(self):
        RollUpGroupBox = QtGui.QGroupBox(u'[집계기준]')
        _layout = QtGui.QVBoxLayout()
        self.chkRollAvg = QtGui.QCheckBox('Average');_layout.addWidget(self.chkRollAvg)
        self.chkRollMed = QtGui.QCheckBox('Median');_layout.addWidget(self.chkRollMed)
        self.chkRollMax = QtGui.QCheckBox('Max');_layout.addWidget(self.chkRollMax)
        self.chkRollMin = QtGui.QCheckBox('Min');_layout.addWidget(self.chkRollMin)
        self.chkRollFst = QtGui.QCheckBox('First');_layout.addWidget(self.chkRollFst)
        self.chkRollLst = QtGui.QCheckBox('Last');_layout.addWidget(self.chkRollLst)
        self.chkRollStd = QtGui.QCheckBox('Std');_layout.addWidget(self.chkRollStd)
        RollUpGroupBox.setLayout(_layout)
        return RollUpGroupBox

    def createAglmGBox(self):
        AlgorithmGroupBox = QtGui.QGroupBox(u'[분석 알고리즘]')
        _layout = QtGui.QVBoxLayout()
        self.chkAgmOls = QtGui.QCheckBox(u'최소자승법(OLS)');_layout.addWidget(self.chkAgmOls)
        self.chkAgmNn = QtGui.QCheckBox(u'인접이웃(NN)');_layout.addWidget(self.chkAgmNn)
        self.chkAgmSvm = QtGui.QCheckBox(u'지지벡터머신(SVM)');_layout.addWidget(self.chkAgmSvm)
        self.chkAgmGtb = QtGui.QCheckBox(u'그라디언트트리부스팅(GTB)');_layout.addWidget(self.chkAgmGtb)
        self.chkAgmAnn = QtGui.QCheckBox(u'인공신경망(ANN)');_layout.addWidget(self.chkAgmAnn)
        AlgorithmGroupBox.setLayout(_layout)
        return AlgorithmGroupBox

    def createTrSlrGBox(self):
        TrrSliderGBox = QtGui.QGroupBox(u'[훈련기간설정]')
        _layout = QtGui.QVBoxLayout()
        self.sldrTrrPeriod = QtGui.QSlider(QtCore.Qt.Horizontal);self.sldrTrrPeriod.setRange(1,20)
        _layout.addWidget(self.sldrTrrPeriod)
        TrrSliderGBox.setLayout(_layout)
        return TrrSliderGBox

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog = UiNowcasting()
    sys.exit(dialog.exec_())