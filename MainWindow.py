import sys
import Database.DBapi as db
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from Tab1 import Tab1
from Tab2 import Tab2
from Tab3 import Tab3

class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(int)

    def __init__(self, fn):
        super(Worker, self).__init__()
        self.func = fn

    def run(self):
        if not self.func():
            print("Database Failed")
            sys.exit()
        self.finished.emit()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1393, 870)
        self.setWindowTitle("PlotMaker")
        self.setWindowIcon(QtGui.QIcon("image/PlotMaker.png"))
        self.mainTab = QtWidgets.QTabWidget()
        self.mainTab.tabBar().setDocumentMode(True)
        self.mainTab.tabBar().setExpanding(True)
        self.setCentralWidget(self.mainTab)

        #資料庫連接失敗 直接關閉程式
        self.thread = QtCore.QThread()
        self.worker = Worker(db.connectDB)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

        #創建3個tab
        self.tab1 = Tab1()
        self.tab2 = Tab2()
        self.tab3 = Tab3()

        #設定tab的css
        #self.setStyleSheet( "QTabBar::tab { height: 40px; width: 250px; }")
        self.setStyleSheet(open("QSS/MainWindow.qss", "r").read())
  
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

        #跳頁
        self.tab1.procMain.connect(partial(self.mainTab.setCurrentIndex, 1))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()