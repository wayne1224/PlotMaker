import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Tab1 import Tab1
from Tab2 import Tab2
from Tab3 import Tab3

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1393, 870)
        self.setWindowTitle("PlotMaker")
        self.mainTab = QtWidgets.QTabWidget()
        self.setCentralWidget(self.mainTab)

        #創建3個tab
        self.tab1 = Tab1()
        self.tab2 = Tab2()
        self.tab3 = Tab3()

        #設定tab的css
        self.setStyleSheet( "QTabBar::tab { height: 40px; width: 250px; }")
  
        #將tab加入MainWindow中
        self.mainTab.addTab(self.tab1, "查詢頁面")
        self.mainTab.addTab(self.tab2, "簡介與角色")
        self.mainTab.addTab(self.tab3, "劇情內容")

        #Signals
        self.tab1.procDoc.connect(self.tab2.import_Doc)
        self.tab1.procCont.connect(self.tab3.importSearchContent)
        self.tab2.procCont.connect(self.tab3.getCont)

        #查詢後清空所有頁面資料
        #self.tab1.procFind.connect(self.tab2)
        #self.tab1.procFind.connect(self.tab3)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()