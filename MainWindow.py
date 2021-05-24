import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Tab2 import Tab2
from Tab3 import Tab3

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1393, 870)
        self.setWindowTitle("CLSA")
        self.mainTab = QtWidgets.QTabWidget()
        self.setCentralWidget(self.mainTab)

        #創建3個tab
        self.tab2 = Tab2()
        self.tab3 = Tab3()

        #設定tab的css
        self.setStyleSheet( "QTabBar::tab { height: 40px; width: 250px; }")
  
        #將tab加入MainWindow中
        self.mainTab.addTab(self.tab2, "簡介與角色")
        self.mainTab.addTab(self.tab3, "劇情內容")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()