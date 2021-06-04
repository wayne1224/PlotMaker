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
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_plotName = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_plotName.setFont(font)
        self.lbl_plotName.setObjectName("lbl_plotName")
        self.horizontalLayout.addWidget(self.lbl_plotName)
        self.lbl_impPlotName = QtWidgets.QLabel()
        self.lbl_impPlotName.setContentsMargins(-1, -1, 10, -1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_impPlotName.setFont(font)
        self.lbl_impPlotName.setObjectName("lbl_impPlotName")
        self.horizontalLayout.addWidget(self.lbl_impPlotName)
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
        self.btn_addScene = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_addScene.setFont(font)
        self.btn_addScene.setObjectName("btn_addScene")
        self.horizontalLayout.addWidget(self.btn_addScene)
        self.btn_deleteScene = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_deleteScene.setFont(font)
        self.btn_deleteScene.setObjectName("btn_deleteScene")
        self.horizontalLayout.addWidget(self.btn_deleteScene)
        layout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(10, -1, 10, -1)
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
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, 25)
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
        self.txt_sceneOutline = QtWidgets.QTextEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_sceneOutline.sizePolicy().hasHeightForWidth())
        self.txt_sceneOutline.setSizePolicy(sizePolicy)
        self.txt_sceneOutline.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_sceneOutline.setFont(font)
        self.txt_sceneOutline.setObjectName("txt_sceneOutline")
        self.horizontalLayout_2.addWidget(self.txt_sceneOutline)
        layout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        layout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(10, 25, 10, 0)
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
        self.horizontalLayout_4.setContentsMargins(10, -1, 10, -1)
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
        self.horizontalLayout_5.setContentsMargins(10, -1, 10, -1)
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
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
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
        self.horizontalLayout_6.setContentsMargins(10, -1, 10, -1)
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
        self.cmb_sceneNum.currentIndexChanged.connect(self.changeScene)
        self.btn_addScene.clicked.connect(self._addScene)
        self.btn_deleteScene.clicked.connect(self._deleteScene)
        self.btn_save.clicked.connect(self.save)
        self.btn_add.clicked.connect(self._addRow)
        self.input_utterance.returnPressed.connect(self._addRow)
        self.input_scenario.returnPressed.connect(self._addRow)
        self.btn_deleteRow.clicked.connect(self._deleteRow)

        # 視窗
        # 輸入數字以外的幕數
        self.msg_sceneNotNum = QtWidgets.QMessageBox()
        self.msg_sceneNotNum.setWindowTitle("提示")
        self.msg_sceneNotNum.setText("幕數只能輸入數字！")
        self.msg_sceneNotNum.setIcon(QtWidgets.QMessageBox.Information)
        # 只剩一幕的話不能刪除
        self.msg_oneLeftSceneDelete = QtWidgets.QMessageBox()
        self.msg_oneLeftSceneDelete.setWindowTitle("提示")
        self.msg_oneLeftSceneDelete.setText("只剩一幕不能刪除！")
        self.msg_oneLeftSceneDelete.setIcon(QtWidgets.QMessageBox.Information)
        # 未選擇角色
        self.msg_characterNotSelect = QtWidgets.QMessageBox()
        self.msg_characterNotSelect.setWindowTitle("提示")
        self.msg_characterNotSelect.setText("請選擇角色！")
        self.msg_characterNotSelect.setIcon(QtWidgets.QMessageBox.Information)
        # 未輸入台詞
        self.msg_noUtterance = QtWidgets.QMessageBox()
        self.msg_noUtterance.setWindowTitle("提示")
        self.msg_noUtterance.setText("請輸入台詞！")
        self.msg_noUtterance.setIcon(QtWidgets.QMessageBox.Information)
        # 未選取刪除列
        self.msg_deleteNotSelect = QtWidgets.QMessageBox()
        self.msg_deleteNotSelect.setWindowTitle("提示")
        self.msg_deleteNotSelect.setText("請選取至少一整列刪除！")
        self.msg_deleteNotSelect.setIcon(QtWidgets.QMessageBox.Information)
        # 儲存成功
        self.msg_save = QtWidgets.QMessageBox()
        self.msg_save.setWindowTitle("提示")
        self.msg_save.setText("儲存成功！")
        self.msg_save.setIcon(QtWidgets.QMessageBox.Information)

        self.basicID = None  # BasicID
        self.plotName = ""  # 劇名
        self.sceneNum = 1  # 幕數
        self.currentSceneNum = 1  # 目前所選的幕
        self.title = ""  # 標題
        self.outline = ""  # 劇情內容
        self.character = []  # 角色
        self.currentSceneContent = {}  # 目前幕的所有內容
        self.allScenes = []  # 全部幕的內容
        self.DBContent = {}  # 匯入的資料

        self.setStyleSheet(open("QSS/Tab3.qss", "r").read())

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_plotName.setText(_translate("", "劇名："))
        self.lbl_di.setText(_translate("", "第"))
        self.cmb_sceneNum.setItemText(0, _translate("", "1"))
        self.lbl_mu.setText(_translate("", "幕"))
        self.btn_addScene.setText(_translate("", "新增一幕"))
        self.btn_deleteScene.setText(_translate("", "刪除此幕"))
        self.lbl_sceneTitle.setText(_translate("", "標題："))
        self.lbl_scenePlot.setText(_translate("", "詳細劇情："))
        self.lbl_role.setText(_translate("", "角色："))
        self.cmb_character.setItemText(1, _translate("", "語境"))
        self.lbl_utterance.setText(_translate("", "台詞："))
        self.lbl_scenario.setText(_translate("", "語境："))
        self.btn_add.setText(_translate("", "新增"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("", "角色"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("", "台詞"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("", "語境"))
        self.btn_deleteRow.setText(_translate("", "刪除列"))
        self.btn_save.setText(_translate("", "儲存內容"))

    # 清空輸入欄
    def clearInput(self):
        self.input_utterance.clear()
        self.input_scenario.clear()

    # 換幕時清空
    def clearSceneInput(self):
        self.input_sceneTitle.clear()
        self.txt_sceneOutline.clear()
        self.cmb_character.clear()
        self.cmb_character.addItem("")
        self.cmb_character.addItem("語境")
        self.tableWidget.setRowCount(0)

    # Tab1查詢匯入
    @QtCore.pyqtSlot(dict)
    def importSearchContent(self, content):
        self.cmb_sceneNum.blockSignals(True)

        self.clearInput()
        self.clearSceneInput()

        self.DBContent = content
        self.basicID = self.DBContent["BasicID"]
        self.plotName = self.DBContent["plotName"]
        self.lbl_impPlotName.setText(self.plotName)
        self.character = self.DBContent["characters"]
        if self.character:  # 更新角色
            for i in range(self.character.__len__()):
                self.cmb_character.addItem(self.character[i])
        
        if self.DBContent["scene"]:
            self.cmb_sceneNum.clear()
            self.sceneNum = self.DBContent["scene"].__len__()
            for i in range(self.sceneNum):
                self.cmb_sceneNum.addItem(self.DBContent["scene"][i]["num"].__str__())
            self.currentSceneNum = self.DBContent["scene"][0]["num"]
            self.title = self.DBContent["scene"][0]["title"]
            self.outline = self.DBContent["scene"][0]["outline"]
            self.input_sceneTitle.setText(self.title)
            self.txt_sceneOutline.setText(self.outline)
            self.currentSceneContent = self.DBContent["scene"][0]
            self.setTable(self.currentSceneContent["content"])
            self.allScenes = self.DBContent["scene"]
        
        self.cmb_sceneNum.blockSignals(False)

    # Tab2儲存匯入
    @QtCore.pyqtSlot(dict)
    def getCont(self, content):
        self.basicID = content["BasicID"]
        self.plotName = content["plotName"]
        self.lbl_impPlotName.setText(self.plotName)
        self.character = content["characters"]
        self.cmb_character.clear()
        self.cmb_character.addItem("")
        self.cmb_character.addItem("語境")
        if self.character:
            for i in range(self.character.__len__()):
                self.cmb_character.addItem(self.character[i])

    # change scene
    def changeScene(self):
        self.saveSceneContent()
        self.currentSceneNum = int(self.cmb_sceneNum.currentText())
        self.setScene()

    # save scene content
    def saveSceneContent(self):
        content = []
        for rowIndex in range(self.tableWidget.rowCount()):
            rowContent = {'role': '', 'utterance': '', 'scenario': ''}
            rowContent['role'] = self.tableWidget.item(rowIndex, 0).text()
            rowContent['utterance'] = self.tableWidget.item(rowIndex, 1).text()
            rowContent['scenario'] = self.tableWidget.item(rowIndex, 2).text()
            content.append(rowContent)
        self.currentSceneContent['num'] = self.currentSceneNum
        self.currentSceneContent['title'] = self.input_sceneTitle.text()
        self.currentSceneContent['outline'] = self.txt_sceneOutline.toPlainText()
        self.currentSceneContent['content'] = content

        isNew = True
        print(self.currentSceneContent['num'])
        for i in range(self.allScenes.__len__()):
            if self.allScenes[i]['num'] == self.currentSceneContent['num']:  # 舊的一幕
                self.allScenes[i] = self.currentSceneContent
                isNew = False
        if isNew:  # 新的一幕
            self.allScenes.append(self.currentSceneContent)
        print(self.allScenes)

    # set scene
    def setScene(self):
        self.currentSceneContent = {}
        for item in self.allScenes:
            if item['num'] == self.currentSceneNum:
                self.currentSceneContent = item

        self.clearSceneInput()
        for i in range(self.character.__len__()):
            self.cmb_character.addItem(self.character[i])
        if self.currentSceneContent:
            self.input_sceneTitle.setText(self.currentSceneContent['title'])
            self.txt_sceneOutline.setText(self.currentSceneContent['outline'])
            self.setTable(self.currentSceneContent['content'])

    # 新增一幕
    def _addScene(self):
        self.cmb_sceneNum.blockSignals(True)
        
        self.saveSceneContent()
        self.sceneNum += 1
        self.currentSceneNum = self.sceneNum
        self.currentSceneContent = {}
        self.cmb_sceneNum.addItem(self.sceneNum.__str__())
        self.cmb_sceneNum.setCurrentIndex(self.sceneNum - 1)
        self.clearSceneInput()
        for i in range(self.character.__len__()):
            self.cmb_character.addItem(self.character[i])
        self.saveSceneContent()

        self.cmb_sceneNum.blockSignals(False)

    # 刪除此幕
    def _deleteScene(self):
        self.cmb_sceneNum.blockSignals(True)

        if self.cmb_sceneNum.count() > 1:
            self.sceneNum -= 1
            temp = None
            for item in self.allScenes:
                if item['num'] == self.currentSceneNum:
                    temp = item
                    break
            if temp:
                self.allScenes.remove(temp)
            self.cmb_sceneNum.removeItem(self.cmb_sceneNum.findText(self.currentSceneNum.__str__()))
            self._resetSceneNum()
            self.cmb_sceneNum.setCurrentIndex(0)
            self.currentSceneNum = int(self.cmb_sceneNum.currentText())
            self.setScene()
            print(self.allScenes)
        else:
            self.msg_oneLeftSceneDelete.exec_()
        
        self.cmb_sceneNum.blockSignals(False)

    # 更新第幾幕的數字
    def _resetSceneNum(self):
        for i in range(self.cmb_sceneNum.__len__()):
            newNum = i + 1
            self.cmb_sceneNum.setItemText(i, newNum.__str__())
            self.allScenes[i]["num"] = newNum

    # 儲存內容
    def save(self):
        self.saveSceneContent()
        db.updateContent(self.basicID, self.allScenes)
        self.msg_save.exec_()

    # set table
    def setTable(self, content):
        if content.__len__() > 0:
            for i in range(content.__len__()):
                character = QtWidgets.QTableWidgetItem(content[i]['role'])
                utterance = QtWidgets.QTableWidgetItem(content[i]['utterance'])
                scenario = QtWidgets.QTableWidgetItem(content[i]['scenario'])
                rowCount = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowCount)
                self.tableWidget.setItem(rowCount, 0, character)
                self.tableWidget.setItem(rowCount, 1, utterance)
                self.tableWidget.setItem(rowCount, 2, scenario)

    # 新增一列
    def _addRow(self):
        if not self.cmb_character.currentText() == "":
            if self.cmb_character.currentText() == "語境":
                character = QtWidgets.QTableWidgetItem("")
                utterance = QtWidgets.QTableWidgetItem("")
            else:
                character = QtWidgets.QTableWidgetItem(self.cmb_character.currentText())
                if not self.input_utterance.text() == "":
                    utterance = QtWidgets.QTableWidgetItem(self.input_utterance.text())
                else:
                    self.msg_noUtterance.exec_()
                    return
            scenario = QtWidgets.QTableWidgetItem(self.input_scenario.text())

            rowCount = self.tableWidget.rowCount()  # 取得目前總列數
            self.tableWidget.insertRow(rowCount)  # 插入一列
            self.tableWidget.setItem(rowCount, 0, character)
            self.tableWidget.setItem(rowCount, 1, utterance)
            self.tableWidget.setItem(rowCount, 2, scenario)

            if not self.cmb_character.currentText() in self.character and not self.cmb_character.currentText() == '語境':  # 新的角色
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
        else:  # 未選取刪除列
            self.msg_deleteNotSelect.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Tab3()
    ui.show()
    sys.exit(app.exec_())
