from Tab2 import Character
from PyQt5 import QtCore, QtGui, QtWidgets
import Database.DBapi as db
import sys
import os


class Tab3(QtWidgets.QWidget):
    def __init__(self):
        super(Tab3, self).__init__()
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_di = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_di.setFont(font)
        self.lbl_di.setObjectName("lbl_di")
        self.horizontalLayout.addWidget(self.lbl_di)
        self.cmb_sceneNum = QtWidgets.QComboBox()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmb_sceneNum.setFont(font)
        self.cmb_sceneNum.setEditable(True)
        self.cmb_sceneNum.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmb_sceneNum.setObjectName("cmb_sceneNum")
        self.cmb_sceneNum.addItem("")
        self.horizontalLayout.addWidget(self.cmb_sceneNum)
        self.lbl_mu = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_mu.setFont(font)
        self.lbl_mu.setObjectName("lbl_mu")
        self.horizontalLayout.addWidget(self.lbl_mu)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_deleteScene = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_deleteScene.setFont(font)
        self.btn_deleteScene.setObjectName("btn_deleteScene")
        self.horizontalLayout.addWidget(self.btn_deleteScene)
        layout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(47)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbl_sceneTitle = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_sceneTitle.sizePolicy().hasHeightForWidth())
        self.lbl_sceneTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_sceneTitle.setFont(font)
        self.lbl_sceneTitle.setObjectName("lbl_sceneTitle")
        self.horizontalLayout_7.addWidget(self.lbl_sceneTitle)
        self.input_sceneTitle = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_sceneTitle.sizePolicy().hasHeightForWidth())
        self.input_sceneTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_sceneTitle.setFont(font)
        self.input_sceneTitle.setObjectName("input_sceneTitle")
        self.horizontalLayout_7.addWidget(self.input_sceneTitle)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        layout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_scenePlot = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_scenePlot.sizePolicy().hasHeightForWidth())
        self.lbl_scenePlot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_scenePlot.setFont(font)
        self.lbl_scenePlot.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lbl_scenePlot.setObjectName("lbl_scenePlot")
        self.horizontalLayout_2.addWidget(self.lbl_scenePlot)
        self.txt_scenePlot = QtWidgets.QTextEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_scenePlot.sizePolicy().hasHeightForWidth())
        self.txt_scenePlot.setSizePolicy(sizePolicy)
        self.txt_scenePlot.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_scenePlot.setFont(font)
        self.txt_scenePlot.setObjectName("txt_scenePlot")
        self.horizontalLayout_2.addWidget(self.txt_scenePlot)
        layout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 25)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.btn_saveScene = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_saveScene.setFont(font)
        self.btn_saveScene.setObjectName("btn_saveScene")
        self.horizontalLayout_8.addWidget(self.btn_saveScene)
        layout.addLayout(self.horizontalLayout_8)
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        layout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 25, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_role = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_role.setFont(font)
        self.lbl_role.setObjectName("lbl_role")
        self.horizontalLayout_3.addWidget(self.lbl_role)
        self.cmb_character = QtWidgets.QComboBox()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmb_character.setFont(font)
        self.cmb_character.setEditable(True)
        self.cmb_character.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmb_character.setObjectName("cmb_character")
        self.cmb_character.addItem("")
        self.cmb_character.addItem("")
        self.horizontalLayout_3.addWidget(self.cmb_character)
        self.lbl_utterance = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_utterance.setFont(font)
        self.lbl_utterance.setObjectName("lbl_utterance")
        self.horizontalLayout_3.addWidget(self.lbl_utterance)
        self.input_utterance = QtWidgets.QLineEdit()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_utterance.setFont(font)
        self.input_utterance.setObjectName("input_utterance")
        self.horizontalLayout_3.addWidget(self.input_utterance)
        layout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_scenario = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_scenario.setFont(font)
        self.lbl_scenario.setObjectName("lbl_scenario")
        self.horizontalLayout_4.addWidget(self.lbl_scenario)
        self.input_scenario = QtWidgets.QLineEdit()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_scenario.setFont(font)
        self.input_scenario.setObjectName("input_scenario")
        self.horizontalLayout_4.addWidget(self.input_scenario)
        layout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.btn_add = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_5.addWidget(self.btn_add)
        layout.addLayout(self.horizontalLayout_5)
        self.tableWidget = QtWidgets.QTableWidget()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        layout.addWidget(self.tableWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_deleteRow = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_deleteRow.setFont(font)
        self.btn_deleteRow.setObjectName("btn_deleteRow")
        self.horizontalLayout_6.addWidget(self.btn_deleteRow)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.btn_save = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_6.addWidget(self.btn_save)
        layout.addLayout(self.horizontalLayout_6)

        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName()

        # table header size
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            2, QtWidgets.QHeaderView.Stretch)

        # 事件
        self.cmb_sceneNum.currentIndexChanged.connect(self.setScene)
        self.btn_deleteScene.clicked.connect(self._deleteScene)
        self.btn_saveScene.clicked.connect(self.saveScene)
        self.btn_add.clicked.connect(self._addRow)
        self.input_utterance.returnPressed.connect(self._addRow)
        self.input_scenario.returnPressed.connect(self._addRow)
        self.btn_deleteRow.clicked.connect(self._deleteRow)
        self.tableWidget.cellClicked.connect(self._checkCharacter)

        # 視窗
        # 未輸入、選擇角色
        self.msg_characterNotSelect = QtWidgets.QMessageBox()
        self.msg_characterNotSelect.setWindowTitle("提示")
        self.msg_characterNotSelect.setText("請輸入、選擇角色！")
        self.msg_characterNotSelect.setIcon(QtWidgets.QMessageBox.Information)
        # 未選取刪除列
        self.msg_deleteNotSelect = QtWidgets.QMessageBox()
        self.msg_deleteNotSelect.setWindowTitle("提示")
        self.msg_deleteNotSelect.setText("請選取至少一整列刪除！")
        self.msg_deleteNotSelect.setIcon(QtWidgets.QMessageBox.Information)

        self.sceneNum = ["1"]  # 幕
        self.currentScene = "1"  # 目前所選的幕
        self.sceneTitle = ""  # 標題
        self.sceneContent = ""  # 劇情內容
        self.character = []  # 角色

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_di.setText(_translate("", "第"))
        self.cmb_sceneNum.setItemText(0, _translate("", "1"))
        self.lbl_mu.setText(_translate("", "幕"))
        self.btn_deleteScene.setText(_translate("", "刪除此幕"))
        self.lbl_sceneTitle.setText(_translate("", "標題："))
        self.lbl_scenePlot.setText(_translate("", "詳細劇情："))
        self.btn_saveScene.setText(_translate("", "儲存此幕"))
        self.lbl_role.setText(_translate("", "角色："))
        self.cmb_character.setItemText(1, _translate("", "語境"))
        self.lbl_utterance.setText(_translate("", "對話："))
        self.lbl_scenario.setText(_translate("", "語境："))
        self.btn_add.setText(_translate("", "新增"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("", "角色"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("", "對話內容"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("", "語境"))
        self.btn_deleteRow.setText(_translate("", "刪除列"))
        self.btn_save.setText(_translate("", "儲存"))

    # 清空輸入欄
    def clearInput(self):
        self.input_utterance.clear()
        self.input_scenario.clear()

    # set scene
    def setScene(self):
        self.currentScene = self.cmb_sceneNum.currentText()

    # 刪除幕
    def _deleteScene(self):
        self.sceneNum.remove(self.currentScene)
        self.cmb_sceneNum.removeItem(self.cmb_sceneNum.findText(self.currentScene))
        self.cmb_sceneNum.setCurrentIndex(0)

    # 儲存幕
    def saveScene(self):
        if not self.cmb_sceneNum.currentText() == "":
            if self.cmb_sceneNum.findText(self.cmb_sceneNum.currentText()) < 0:  # 新的一幕
                self.sceneNum.append(self.cmb_sceneNum.currentText())
                self.cmb_sceneNum.addItem(self.cmb_sceneNum.currentText())
                self.cmb_sceneNum.setCurrentIndex(self.cmb_sceneNum.count()-1)
                self.currentScene = self.cmb_sceneNum.currentText()

    # 檢查、更新角色選單
    def _checkCharacter(self):
        checkCharacter = []
        for index in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(index, 0):
                if not self.tableWidget.item(index, 0).text().__len__() == 0:  # 不是空字串
                    if not self.tableWidget.item(index, 0).text() in checkCharacter:
                        checkCharacter.append(self.tableWidget.item(index, 0).text())

        self.cmb_character.clear()
        self.cmb_character.addItem("")
        self.cmb_character.addItem("語境")
        for i in checkCharacter:
            self.cmb_character.addItem(i)
        self.character = checkCharacter  # 更新角色

    # 新增一列
    def _addRow(self):
        if not self.cmb_character.currentText() == "":
            if self.cmb_character.currentText() == "語境":
                character = QtWidgets.QTableWidgetItem("")
            else:
                character = QtWidgets.QTableWidgetItem(self.cmb_character.currentText())
            utterance = QtWidgets.QTableWidgetItem(self.input_utterance.text())
            scenario = QtWidgets.QTableWidgetItem(self.input_scenario.text())

            rowCount = self.tableWidget.rowCount()  # 取得目前總列數
            self.tableWidget.insertRow(rowCount)  # 插入一列
            self.tableWidget.setItem(rowCount, 0, character)
            self.tableWidget.setItem(rowCount, 1, utterance)
            self.tableWidget.setItem(rowCount, 2, scenario)

            if not self.cmb_character.currentText() in self.character:  # 新的角色
                self.character.append(self.cmb_character.currentText())
                self.cmb_character.addItem(self.cmb_character.currentText())  # 在角色選單新增新的角色

            self.clearInput()
            self.cmb_character.setCurrentIndex(0)
            self.cmb_character.setFocus()
        else:  # 未輸入、選擇角色
            self.msg_characterNotSelect.exec_()

    # 刪除一列
    def _deleteRow(self):
        indexes = self.tableWidget.selectionModel().selectedRows()
        if indexes:
            for index in sorted(indexes, reverse=True):
                self.tableWidget.removeRow(index.row())
            self._checkCharacter()
        else:  # 未選取刪除列
            self.msg_deleteNotSelect.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Tab3()
    ui.show()
    sys.exit(app.exec_())
