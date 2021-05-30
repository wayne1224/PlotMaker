from PyQt5 import QtCore, QtGui, QtWidgets
import Database.DBapi as db
import sys
import os
import qtawesome as qta
from datetime import datetime as dt

class CheckableComboBox(QtWidgets.QComboBox):
    def __init__(self):
        super(CheckableComboBox, self).__init__()
        self.view().pressed.connect(self.handle_item_pressed)
        self.setModel(QtGui.QStandardItemModel(self))

        self.types = ['動作','喜劇','愛情','恐怖','科幻','其他']
        for i, type in enumerate(self.types):
            self.addItem(type)
            item = self.model().item(i, 0)
            # setting item unchecked
            item.setCheckState(QtCore.Qt.Unchecked)
  
    # when any item get pressed
    def handle_item_pressed(self, index):
        # getting which item is pressed
        item = self.model().itemFromIndex(index)
        # make it check if unchecked and vice-versa
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)
  
    # method called by check_items
    def item_checked(self, index):
        # getting item at index
        item = self.model().item(index, 0)
        # return true if checked else false
        return item.checkState() == QtCore.Qt.Checked
    
    def getName(self, index):
        return self.model().item(index, 0).text()

    # calling method
    def getItems(self):
        checkedItems = []
        # traversing the items
        for i in range(self.count()):
            # if item is checked add it to the list
            if self.item_checked(i):
                checkedItems.append(self.getName(i))
        return checkedItems

    def setCheckState(self, checkedItems):
        for i in checkedItems:
            idx = self.types.index(i)
            item = self.model().item(idx, 0)
            item.setCheckState(QtCore.Qt.Checked)

    def isEmpty(self):
        for i in range(self.count()):
            if self.item_checked(i):
                return False
        return True

    def clear(self):
        for i in range(self.count()):
            if self.item_checked(i):
                item = self.model().item(i, 0)
                item.setCheckState(QtCore.Qt.Unchecked)
        
    # flush
    sys.stdout.flush()

class Character(QtWidgets.QGroupBox):
    def __init__(self):
        QtWidgets.QGroupBox.__init__(self)
        #self.setTitle("Title") 
        self.verticalLayoutWidget_4 = QtWidgets.QWidget()
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 6, 311, 461))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.characterLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.characterLayout.setContentsMargins(0, 0, 0, 0)
        self.characterLayout.setObjectName("characterLayout")
        self.setLayout(self.characterLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.input_Role = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.input_Role.setFont(font)
        self.input_Role.setObjectName("input_Role")
        self.verticalLayout.addWidget(self.input_Role)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.input_Actor = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.input_Actor.setFont(font)
        self.input_Actor.setObjectName("input_Actor")
        self.verticalLayout.addWidget(self.input_Actor)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        icon = qta.icon('fa5.folder-open')
        self.photo_btn = QtWidgets.QPushButton()
        self.photo_btn.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.photo_btn.setFont(font)
        self.photo_btn.setObjectName("photo_btn")
        icon = qta.icon('fa5s.trash')
        self.deletePhoto_btn = QtWidgets.QPushButton()
        self.deletePhoto_btn.setIcon(icon)
        self.horizontalLayout_6.addWidget(self.photo_btn)
        self.horizontalLayout_6.addWidget(self.deletePhoto_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.label_photo = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_photo.setMaximumSize(QtCore.QSize(150, 200))
        self.label_photo.setMinimumSize(QtCore.QSize(150, 200))
        self.label_photo.setAutoFillBackground(False)
        self.label_photo.setFrameShape(QtWidgets.QFrame.Box)
        self.label_photo.setText("")
        self.label_photo.setPixmap(QtGui.QPixmap(""))
        self.label_photo.setScaledContents(True)
        self.label_photo.setObjectName("label_photo")
        photoSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.photoLayout = QtWidgets.QHBoxLayout()
        self.photoLayout.addItem(photoSpacer)
        self.photoLayout.addWidget(self.label_photo)
        self.verticalLayout_4.addLayout(self.photoLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.characterLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.input_Desc = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.input_Desc.setObjectName("input_Desc")
        self.input_Desc.setFont(font)
        self.verticalLayout_3.addWidget(self.input_Desc)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.delete_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.delete_btn.setFont(font)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout.addWidget(self.delete_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.characterLayout.addLayout(self.verticalLayout_3)
        self.retranslateUi()

        self.cwd = os.getcwd() #目前檔案位置

        #signals
        self.photo_btn.clicked.connect(self.selectPhoto)
        self.delete_btn.clicked.connect(self.delete)
        self.deletePhoto_btn.clicked.connect(self.deletePhoto)
        self.photoPath = None
        self.photoID = None
    
    def setup(self, char):
        self.input_Role.setText(char['name'])
        self.input_Actor.setText(char['actor'])
        self.input_Desc.setPlainText(char['description'])
        try:
            self.photoID = char['photo']
            photoBytes = db.findImg(char['photo'])
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(photoBytes)
            self.label_photo.setPixmap(pixmap)
        except:
            self.photoID = None

        #清除CSS
        self.input_Role.setStyleSheet("")
        self.input_Actor.setStyleSheet("")

    def getName(self):
        if self.input_Role.text() != '':
            return self.input_Role.text()
        

    def selectPhoto(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(None,  
                                    "開啟圖片",  
                                    self.cwd, # 起始路径 
                                    "Image Files(*.png *.jpg *.bmp)")
        if filePath and os.path.exists(filePath):
            self.label_photo.setPixmap(QtGui.QPixmap(filePath))
            self.photoPath = filePath

    def deletePhoto(self):
        self.label_photo.clear()
        self.photoPath = None
        self.photoID = None

    def save(self):
        profile = {}
        
        profile['name'] = self.input_Role.text()
        profile['actor'] = self.input_Actor.text()
        profile['description'] = self.input_Desc.toPlainText()

        if self.photoPath != None: #新圖片或換圖片
            photoID =  db.insertImg(self.photoPath)
            profile['photo'] = photoID
        
        elif self.photoID != None: #原圖片
            profile['photo'] = self.photoID

        if all(value == '' for value in profile.values()):
            return

        #清除CSS
        self.input_Role.setStyleSheet("")
        self.input_Actor.setStyleSheet("")

        return profile
    
    def delete(self):
        if (self.input_Role.text() != '' or self.input_Actor.text() != '' or self.input_Desc.toPlainText() != ''
            or self.photoPath != None or self.photoID != None):
            close = QtWidgets.QMessageBox.warning(self,
                            "CLSA",
                            '<p style="font-size:13pt; color: #3778bf;">確定要刪除角色嗎?</p>',
                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if close == QtWidgets.QMessageBox.Yes:
                self.deleteLater()
            elif close == QtWidgets.QMessageBox.No:
                return
        else:
            self.deleteLater()

        
    def isEmpty(self):
        check = False

        if self.input_Role.text() == '' and self.input_Actor.text() != '':
            self.input_Role.setStyleSheet("border: 1px solid red;")
            check = True
        if self.input_Role.text() != '' and self.input_Actor.text() == '':
            self.input_Actor.setStyleSheet("border: 1px solid red;")
            check = True

        return check

    def clear(self):
        self.input_Role.clear()
        self.input_Actor.clear()
        self.input_Desc.clear()
        self.label_photo.clear()

        #清除CSS
        self.input_Role.setStyleSheet("")
        self.input_Actor.setStyleSheet("")
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("", "角色名稱："))
        self.label_2.setText(_translate("", "演員："))
        # self.photo_btn.setText(_translate("", "選擇相片"))
        self.label_3.setText(_translate("", "描述："))
        self.delete_btn.setText(_translate("", "刪除角色"))

class Tab2(QtWidgets.QWidget):
    procCont = QtCore.pyqtSignal(dict)
    def __init__(self):
        super(Tab2, self).__init__()
        self.verticalLayoutWidget = QtWidgets.QWidget()
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 991, 741))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.setLayout(self.verticalLayout_3) #set Widget Layout
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.input_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_name.sizePolicy().hasHeightForWidth())
        self.input_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_name.setFont(font)
        self.input_name.setObjectName("input_name")
        self.horizontalLayout.addWidget(self.input_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.input_author = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_author.sizePolicy().hasHeightForWidth())
        self.input_author.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_author.setFont(font)
        self.input_author.setObjectName("input_author")
        self.horizontalLayout_2.addWidget(self.input_author)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox = CheckableComboBox()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.addRole_btn = QtWidgets.QPushButton()
        self.addRole_btn.setFont(font)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout_action = QtWidgets.QHBoxLayout()
        self.horizontalLayout_action.addWidget(self.label_5)
        self.horizontalLayout_action.addItem(spacerItem)
        self.horizontalLayout_action.addWidget(self.addRole_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_action)

        #角色列表
        self.rolesLayout = QtWidgets.QHBoxLayout()
        self.rolesLayout.setSpacing(20)
        self.rolesLayout.addWidget(Character())
        self.rolesLayout.addWidget(Character())
        self.rolesLayout.addWidget(Character())
       
        #ScrollArea
        self.scroll = QtWidgets.QScrollArea() 
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.widget = QtWidgets.QWidget() #contain hbox
        self.widget.setLayout(self.rolesLayout)
        self.scroll.setWidget(self.widget)
        self.verticalLayout_3.addWidget(self.scroll)
        
        #Action Button
        self.actionLayout = QtWidgets.QHBoxLayout()
        self.clear_btn = QtWidgets.QPushButton()
        self.clear_btn.setFont(font)
        self.save_btn = QtWidgets.QPushButton()
        self.save_btn.setFont(font)
        self.actionLayout.addWidget(self.clear_btn)
        self.actionLayout.addItem(spacerItem)
        self.actionLayout.addWidget(self.save_btn)
        self.verticalLayout_3.addLayout(self.actionLayout)

        #劇照
        self.photoLayout = QtWidgets.QVBoxLayout()
        self.label_P = QtWidgets.QLabel()
        self.label_P.setFont(font)
        icon = qta.icon('fa5.folder-open')
        self.selectPhoto_btn = QtWidgets.QPushButton()
        self.selectPhoto_btn.setIcon(icon)
        icon = qta.icon('fa5s.trash')
        self.deletePhoto_btn = QtWidgets.QPushButton()
        self.deletePhoto_btn.setIcon(icon)
        self.PLayout = QtWidgets.QHBoxLayout()
        self.PLayout.addWidget(self.label_P)
        self.PLayout.addWidget(self.selectPhoto_btn)
        self.PLayout.addWidget(self.deletePhoto_btn)

        self.label_photo = QtWidgets.QLabel()
        self.label_photo.setMinimumSize(QtCore.QSize(180, 240))
        self.label_photo.setMaximumSize(QtCore.QSize(180, 240))
        self.label_photo.setAutoFillBackground(False)
        self.label_photo.setFrameShape(QtWidgets.QFrame.Box)
        self.label_photo.setPixmap(QtGui.QPixmap(""))
        self.label_photo.setScaledContents(True)
        self.label_photo.setObjectName("label_photo")

        self.photoLayout.addLayout(self.PLayout)
        self.photoLayout.addWidget(self.label_photo)
        self.horizontalLayout_4.addLayout(self.photoLayout)


        #signals
        self.addRole_btn.clicked.connect(self._addCharacter)
        self.save_btn.clicked.connect(self.save)
        self.clear_btn.clicked.connect(self.clear)
        self.selectPhoto_btn.clicked.connect(self.selectPhoto)
        self.deletePhoto_btn.clicked.connect(self.deletePhoto)

        #save object_id
        self._id = None
        self.photoID = None
        self.photoPath = None
        self.cwd = os.getcwd() #目前檔案位置
        self.currentDoc = {'plotName': '', 'author': '', 'outline': '', 'type': [], 'characters': []} #檢查是否修改

        self.retranslateUi()

    def _addCharacter(self):
        self.rolesLayout.addWidget(Character())
       
    def _getCurrentDoc(self):
        Basic = {}
        characters = []

        #Iterate over Characters
        for i in range(self.rolesLayout.count()):
            char = self.rolesLayout.itemAt(i).widget().save()
            if char != None:
                characters.append(char)

        Basic['plotName'] = self.input_name.text()
        Basic['author'] = self.input_author.text()
        Basic['outline'] = self.textEdit.toPlainText()
        Basic['type'] = self.comboBox.getItems()
        Basic['characters'] = characters

        if self.photoPath != None: #新圖片或換圖片
            photoID =  db.insertImg(self.photoPath)
            Basic['photo'] = photoID
        elif self.photoID != None: #原圖片
            Basic['photo'] = self.photoID
        else:
            Basic['photo'] = None
        
        return Basic

    def checkChanged(self):
        if self._getCurrentDoc() != self.currentDoc:
            return True
        else:
            return False

    def getCharacterNames(self):
        characterNames = []
        for i in range(self.rolesLayout.count()):
            char = self.rolesLayout.itemAt(i).widget()
            if char != None:
                characterNames.append(char.getName())
        return list(filter(None, characterNames))
  
    def save(self):
        if self.isEmpty() == False:
            Basic = self._getCurrentDoc()

            if self._id == None:
                Basic['createTime'] = dt.now().strftime("%Y/%m/%d %H:%M:%S")

            if self._id != None:
                if db.upsertBasic(Basic, self._id):
                    QtWidgets.QMessageBox.information(self, '通知','資料更新成功', QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.information(self, '通知','資料更新失敗', QtWidgets.QMessageBox.Ok)
            else:
                if db.upsertBasic(Basic):
                    QtWidgets.QMessageBox.information(self, '通知','資料新增成功', QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.information(self, '通知','資料新增失敗', QtWidgets.QMessageBox.Ok)

            if self._id == None:
                self._id = Basic['_id']

            #存目前的進度
            self.currentDoc = Basic
            self.currentDoc.pop('createTime', None)

            #CSS改回來
            self.input_name.setStyleSheet("")
            self.input_author.setStyleSheet("")
            self.comboBox.setStyleSheet("")
            print(self.getCharacterNames())
            content = {'BasicID': self._id, 'plotName':Basic['plotName'], 'characters': self.getCharacterNames()}
            self.procCont.emit(content)

        else:
            QtWidgets.QMessageBox.warning(self, '通知','紅框為必填項目', QtWidgets.QMessageBox.Ok)
    
    @QtCore.pyqtSlot(dict)
    def import_Doc(self, doc):
        #先清除
        self.clear()
        #匯入
        self._id = doc['_id']
        self.input_name.setText(doc['plotName'])
        self.input_author.setText(doc['author'])
        self.textEdit.setPlainText(doc['outline'])
        self.comboBox.setCheckState(doc['type'])

        #匯入照片
        try:
            self.photoID = doc['photo']
            photoBytes = db.findImg(doc['photo'])
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(photoBytes)
            self.label_photo.setPixmap(pixmap)
        except:
            self.photoID = None

        for i, char in enumerate(doc['characters']):
            if i >= self.rolesLayout.count():
                self._addCharacter()
            self.rolesLayout.itemAt(i).widget().setup(char)
        
        #存目前的進度
        self.currentDoc = doc
        self.currentDoc.pop('createTime', None)

        #CSS改回來
        self.input_name.setStyleSheet("")
        self.input_author.setStyleSheet("")
        self.comboBox.setStyleSheet("")
        
    def selectPhoto(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(None,  
                                    "開啟圖片",  
                                    self.cwd, # 起始路径 
                                    "Image Files(*.png *.jpg *.bmp)")
        if filePath and os.path.exists(filePath):
            self.label_photo.setPixmap(QtGui.QPixmap(filePath))
            self.photoPath = filePath

    def deletePhoto(self):
        self.label_photo.clear()
        self.photoPath = None
        self.photoID = None

    def clear(self):
        self.input_name.clear()
        self.input_author.clear()
        self.textEdit.clear()
        self.comboBox.clear()
        self.label_photo.clear()
        for i in range(self.rolesLayout.count()):
            self.rolesLayout.itemAt(i).widget().clear()
        
        #CSS改回來
        self.input_name.setStyleSheet("")
        self.input_author.setStyleSheet("")
        self.comboBox.setStyleSheet("")
    
    def isEmpty(self):
        check = False
         
        if self.input_name.text() == '':
            self.input_name.setStyleSheet("border: 1px solid red;")
            check = True
        if self.input_author.text() == '':
            self.input_author.setStyleSheet("border: 1px solid red;")
            check = True
        if self.comboBox.isEmpty() == True:
            self.comboBox.setStyleSheet("border: 1px solid red;")
            check = True

        for i in range(self.rolesLayout.count()):
            if self.rolesLayout.itemAt(i).widget().isEmpty():
                check = True

        return check
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("", "劇名："))
        self.label_2.setText(_translate("", "編劇："))
        self.label_3.setText(_translate("", "類型："))
        self.label_4.setText(_translate("", "概要："))
        self.label_5.setText(_translate("", "角色："))
        self.label_P.setText(_translate("", "劇照："))
        self.addRole_btn.setText(_translate("", "新增角色"))
        self.clear_btn.setText(_translate("", "全部清除"))
        self.save_btn.setText(_translate("", "儲存"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen = Tab2()
    screen.show()
    sys.exit(app.exec_())
