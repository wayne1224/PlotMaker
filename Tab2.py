from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import ImageQt
import sys
import os

class CheckableComboBox(QtWidgets.QComboBox):
    def __init__(self):
        super(CheckableComboBox, self).__init__()
        self.view().pressed.connect(self.handle_item_pressed)
        self.setModel(QtGui.QStandardItemModel(self))

        types = ['動作','喜劇','愛情','恐怖','科幻','其他']
        for i, type in enumerate(types):
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
        self.photo_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.photo_btn.setFont(font)
        self.photo_btn.setObjectName("photo_btn")
        self.horizontalLayout_6.addWidget(self.photo_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.label_photo = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_photo.setMaximumSize(QtCore.QSize(150, 200))
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
        self.delete_btn.clicked.connect(self.deleteLater)
    
    def selectPhoto(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(None,  
                                    "開啟圖片",  
                                    self.cwd, # 起始路径 
                                    "Image Files(*.png *.jpg *.bmp)")
        if filePath and os.path.exists(filePath):
            self.label_photo.setPixmap(QtGui.QPixmap(filePath))

    def save(self):
        profile = {}

        profile['name'] = self.input_Role.text()
        profile['actor'] = self.input_Actor.text()
        profile['description'] = self.input_Desc.toPlainText()

        # if self.label_photo.pixmap != None:
        #     image = ImageQt.fromqpixmap(self.label_photo.grab())
        #     print(image)
        if profile['name'] == '' and profile['actor'] == '' and profile['description'] == '':
            return

        return profile

    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("", "角色名稱："))
        self.label_2.setText(_translate("", "演員："))
        self.photo_btn.setText(_translate("", "選擇相片"))
        self.label_3.setText(_translate("", "描述："))
        self.delete_btn.setText(_translate("", "刪除角色"))

class Tab2(QtWidgets.QWidget):
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
        
        self.retranslateUi()

        #signals
        self.addRole_btn.clicked.connect(self._addCharacter)

    def _addCharacter(self):
        self.save()
        self.rolesLayout.addWidget(Character())
       
    def save(self):
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

        #接API
    
    def import(self):
        pass

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("", "劇名："))
        self.label_2.setText(_translate("", "編劇："))
        self.label_3.setText(_translate("", "類型："))
        self.label_4.setText(_translate("", "概要："))
        self.label_5.setText(_translate("", "角色："))
        self.addRole_btn.setText(_translate("", "新增角色"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen = Tab2()
    screen.show()
    sys.exit(app.exec_())

