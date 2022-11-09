from PyQt5 import QtCore, QtGui, QtWidgets


class BottleNeck(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 720))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:lavender")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(510, 0, 551, 671))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("background-color:rgba(255, 255, 127, 125)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 549, 669))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 630, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(255, 250, 80)")
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(260, 480, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 530, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 30, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 80, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 180, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 130, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 330, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 230, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 280, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 630, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 170, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(190, 40, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(5)
        self.comboBox.setMaxCount(5)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 90, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setMaxVisibleItems(5)
        self.comboBox_2.setMaxCount(5)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(190, 140, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setMaxVisibleItems(5)
        self.comboBox_3.setMaxCount(5)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(190, 190, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setMaxVisibleItems(5)
        self.comboBox_4.setMaxCount(5)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(190, 340, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setMaxVisibleItems(5)
        self.comboBox_5.setMaxCount(5)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(190, 290, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setEditable(False)
        self.comboBox_6.setMaxVisibleItems(5)
        self.comboBox_6.setMaxCount(5)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_8 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_8.setGeometry(QtCore.QRect(190, 240, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setEditable(False)
        self.comboBox_8.setMaxVisibleItems(5)
        self.comboBox_8.setMaxCount(5)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_8.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "src"))
        self.pushButton.setText(_translate("MainWindow", "Convert"))
        self.radioButton.setText(_translate("MainWindow", "SAX API"))
        self.radioButton_2.setText(_translate("MainWindow", "DOM API"))
        self.checkBox.setText(_translate("MainWindow", "Surname"))
        self.checkBox_2.setText(_translate("MainWindow", "Faculty"))
        self.checkBox_3.setText(_translate("MainWindow", "Department"))
        self.checkBox_4.setText(_translate("MainWindow", "Major"))
        self.checkBox_5.setText(_translate("MainWindow", "ID"))
        self.checkBox_7.setText(_translate("MainWindow", "Evaluetes"))
        self.checkBox_8.setText(_translate("MainWindow", "Ranking"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Pevny"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Olefir"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Fesiuk"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Vishnyak"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Algin"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "CSC"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "IT"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "MAM"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Chemistry"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "History"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "122"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "121"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "112"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "027"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "102"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "OR"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "OOP"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Mathan"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "UH"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "H2O"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "100"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "200"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "300"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "400"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "500"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "10"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "9"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "8"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "7"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "6"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
