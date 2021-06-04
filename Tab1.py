# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'Tab1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import Database.DBapi
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from functools import partial



class Tab1(QtWidgets.QWidget):
    procDoc = QtCore.pyqtSignal(dict)
    procCont = QtCore.pyqtSignal(dict)
    procFind = QtCore.pyqtSignal()
    procMain = QtCore.pyqtSignal()

    def __init__(self):
        super(Tab1, self).__init__()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.setLayout(self.gridLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.label_SLP = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_SLP.setFont(font)
        self.label_SLP.setObjectName("label_SLP")
        self.horizontalLayout.addWidget(self.label_SLP)
        self.input_SLP = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_SLP.sizePolicy().hasHeightForWidth())
        self.input_SLP.setSizePolicy(sizePolicy)
        self.input_SLP.setObjectName("input_SLP")
        self.input_SLP.setFont(font)
        self.horizontalLayout.addWidget(self.input_SLP)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.label_caseID = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_caseID.setFont(font)
        self.label_caseID.setObjectName("label_caseID")
        self.horizontalLayout_5.addWidget(self.label_caseID)
        self.input_caseID = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_caseID.sizePolicy().hasHeightForWidth())
        self.input_caseID.setSizePolicy(sizePolicy)
        self.input_caseID.setObjectName("input_caseID")
        self.input_caseID.setFont(font)
        
        self.horizontalLayout_5.addWidget(self.input_caseID)
        

        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label_actor = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_actor.setFont(font)
        self.label_actor.setObjectName("label_actor")
        self.horizontalLayout_3.addWidget(self.label_actor)
        self.input_actor = QtWidgets.QLineEdit()
        self.input_actor.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_actor.sizePolicy().hasHeightForWidth())
        self.input_actor.setSizePolicy(sizePolicy)
        self.input_actor.setObjectName("input_actor")
        self.horizontalLayout_3.addWidget(self.input_actor)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.button_search = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_search.sizePolicy().hasHeightForWidth())
        self.button_search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_search.setFont(font)
        self.button_search.setObjectName("button_search")
        self.horizontalLayout_4.addWidget(self.button_search)

        self.button_search.clicked.connect(self.search)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)

        self.horizontalLayout_4.setContentsMargins(20, 20, 30, 0)
        self.gridLayout.setContentsMargins(20, 0, 20, 0)

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 1)

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.setContentsMargins(20, 0, 20, 0)

        self.setStyleSheet(open("QSS/Tab1.qss", "r").read())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_SLP.setText(_translate("self", "劇名："))
        self.label_caseID.setText(_translate("self", "作者："))
        self.label_actor.setText(_translate("self", " 演員："))
        self.button_search.setText(_translate("self", "  查詢  "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("self", "劇名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("self", "作者"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("self", "演員"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("self", "劇本類型"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("self", "建立時間"))

    def search(self) :
        self.procFind.emit()
        Docs = Database.DBapi.findDocs(self.input_SLP.text(), self.input_caseID.text(), self.input_actor.text())
        
        #再翻新的話要清除舊的
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(self.tableWidget.rowCount()-1)

        if Docs :
            for i, doc in enumerate(Docs):
                self.tableWidget.insertRow(i)

                item = QtWidgets.QTableWidgetItem()
                item.setText(doc['plotName'])
                self.tableWidget.setItem(i , 0 , item)

                item = QtWidgets.QTableWidgetItem()
                item.setText(doc['author'])
                self.tableWidget.setItem(i , 1 , item)

                item = QtWidgets.QTableWidgetItem()
                strCharacters = ''
                for x, y in enumerate(doc['characters']) :
                    strCharacters += y['actor']
                    if x != len(doc['characters']) - 1:
                        strCharacters += ', '
                item.setText(strCharacters)
                self.tableWidget.setItem(i , 2 , item)

                item = QtWidgets.QTableWidgetItem()
                strType = ''
                for x, y in enumerate(doc['type']) :
                    strType += y
                    if x != len(doc['type']) - 1:
                        strType += ', '
                item.setText(strType)
                self.tableWidget.setItem(i , 3 , item)

                item = QtWidgets.QTableWidgetItem()
                item.setText(doc['createTime'])
                self.tableWidget.setItem(i , 4 , item)

                importBtn = QtWidgets.QPushButton('匯入')
                deleteBtn = QtWidgets.QPushButton('刪除')
                self.tableWidget.setCellWidget(i,5,importBtn)
                self.tableWidget.setCellWidget(i,6,deleteBtn)

                content = Database.DBapi.findContent(doc['_id'])
                importBtn.clicked.connect(partial(self.importDoc , doc, content))
                deleteBtn.clicked.connect(partial(self.deleteDoc , doc['_id'] , i))
        else :
            informBox = QtWidgets.QMessageBox.information(self, '查詢','查無資料', QtWidgets.QMessageBox.Ok)

    @QtCore.pyqtSlot()
    def importDoc (self, obj, content):
        self.procDoc.emit(obj)
        self.procCont.emit(content)
        informBox = QtWidgets.QMessageBox.information(self, '通知','匯入完成', QtWidgets.QMessageBox.Ok)
        self.procMain.emit()

    def deleteDoc (self, objID , i):
        delete = QtWidgets.QMessageBox.warning(self,
                            "PlotMaker",
                            '<p style="font-size:13pt; color: red;">確定要刪除此資料嗎?</p>',
                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        if delete == QtWidgets.QMessageBox.Yes:
            if Database.DBapi.deleteDocs(objID):
                self.tableWidget.removeRow(i)
                informBox = QtWidgets.QMessageBox.information(self, '成功','成功刪除個案', QtWidgets.QMessageBox.Ok)
            else:
                informBox = QtWidgets.QMessageBox.critical(self, '失敗','刪除個案失敗', QtWidgets.QMessageBox.Ok)
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen = Tab1()
    screen.show()
    sys.exit(app.exec_())
