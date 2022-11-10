from PyQt5 import QtCore, QtGui, QtWidgets


class ApplicationView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def init_ui(self):
        # self == window
        self.setObjectName("self")
        self.resize(1080, 720)
        self.setMinimumSize(QtCore.QSize(1080, 720))
        self.setMaximumSize(QtCore.QSize(1080, 720))
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color:lavender")

        # central widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # scroll area
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

        # buttons
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(20, 630, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.convertButton.setFont(font)
        self.convertButton.setStyleSheet("background-color:rgb(255, 250, 80)")
        self.convertButton.setObjectName("convertButton")

        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(260, 630, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("background-color:rgb(255, 170, 255)")
        self.searchButton.setObjectName("searchButton")

        # radio buttons
        self.SaxApiButton = QtWidgets.QRadioButton(self.centralwidget)
        self.SaxApiButton.setGeometry(QtCore.QRect(260, 480, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.SaxApiButton.setFont(font)
        self.SaxApiButton.setStyleSheet("")
        self.SaxApiButton.setObjectName("SaxApiButton")
        self.SaxApiButton.setChecked(True)

        self.DomApiButton = QtWidgets.QRadioButton(self.centralwidget)
        self.DomApiButton.setGeometry(QtCore.QRect(260, 530, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.DomApiButton.setFont(font)
        self.DomApiButton.setStyleSheet("")
        self.DomApiButton.setObjectName("DomApiButton")

        # check(tick) boxes
        # surname
        self.surnameCheckButton = QtWidgets.QCheckBox(self.centralwidget)
        self.surnameCheckButton.setGeometry(QtCore.QRect(20, 30, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.surnameCheckButton.setFont(font)
        self.surnameCheckButton.setObjectName("surnameCheckButton")

        # faculty
        self.facultyCheckButton = QtWidgets.QCheckBox(self.centralwidget)
        self.facultyCheckButton.setGeometry(QtCore.QRect(20, 80, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.facultyCheckButton.setFont(font)
        self.facultyCheckButton.setObjectName("facultyCheckButton")

        # department
        self.departmentCheckButton = QtWidgets.QCheckBox(self.centralwidget)
        self.departmentCheckButton.setGeometry(QtCore.QRect(20, 180, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.departmentCheckButton.setFont(font)
        self.departmentCheckButton.setObjectName("departmentCheckButton")

        # major
        self.majorCheckButton = QtWidgets.QCheckBox(self.centralwidget)
        self.majorCheckButton.setGeometry(QtCore.QRect(20, 130, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.majorCheckButton.setFont(font)
        self.majorCheckButton.setObjectName("majorCheckButton")

        # id
        self.idCheckButton = QtWidgets.QCheckBox(self.centralwidget)
        self.idCheckButton.setGeometry(QtCore.QRect(20, 330, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.idCheckButton.setFont(font)
        self.idCheckButton.setObjectName("idCheckButton")

        # evaluations
        self.evaluationsCheckButton = QtWidgets.QCheckBox(self.centralwidget)
        self.evaluationsCheckButton.setGeometry(QtCore.QRect(20, 230, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.evaluationsCheckButton.setFont(font)
        self.evaluationsCheckButton.setObjectName("evaluationsCheckButton")

        # ranking
        self.rankingCheckButton = QtWidgets.QCheckBox(self.centralwidget)
        self.rankingCheckButton.setGeometry(QtCore.QRect(20, 280, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.rankingCheckButton.setFont(font)
        self.rankingCheckButton.setObjectName("rankingCheckButton")

        # combo(drop menu) boxes
        # surname
        self.surnameBox = QtWidgets.QComboBox(self.centralwidget)
        self.surnameBox.setGeometry(QtCore.QRect(190, 40, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.surnameBox.setFont(font)
        self.surnameBox.setEditable(False)
        self.surnameBox.setObjectName("surnameBox")

        # faculty
        self.facultyBox = QtWidgets.QComboBox(self.centralwidget)
        self.facultyBox.setGeometry(QtCore.QRect(190, 90, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.facultyBox.setFont(font)
        self.facultyBox.setEditable(False)
        self.facultyBox.setObjectName("facultyBox")

        # major
        self.majorBox = QtWidgets.QComboBox(self.centralwidget)
        self.majorBox.setGeometry(QtCore.QRect(190, 140, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.majorBox.setFont(font)
        self.majorBox.setEditable(False)
        self.majorBox.setObjectName("majorBox")

        # department
        self.departmentBox = QtWidgets.QComboBox(self.centralwidget)
        self.departmentBox.setGeometry(QtCore.QRect(190, 190, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.departmentBox.setFont(font)
        self.departmentBox.setEditable(False)
        self.departmentBox.setObjectName("departmentBox")

        # id
        self.idBox = QtWidgets.QComboBox(self.centralwidget)
        self.idBox.setGeometry(QtCore.QRect(190, 340, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.idBox.setFont(font)
        self.idBox.setEditable(False)
        self.idBox.setObjectName("idBox")

        # ranking
        self.rankingBox = QtWidgets.QComboBox(self.centralwidget)
        self.rankingBox.setGeometry(QtCore.QRect(190, 290, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.rankingBox.setFont(font)
        self.rankingBox.setEditable(False)
        self.rankingBox.setObjectName("rankingBox")

        # evaluations
        self.evaluationsBox = QtWidgets.QComboBox(self.centralwidget)
        self.evaluationsBox.setGeometry(QtCore.QRect(190, 240, 281, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.evaluationsBox.setFont(font)
        self.evaluationsBox.setEditable(False)
        self.evaluationsBox.setObjectName("evaluationsBox")

        self.surnameBox.setCurrentIndex(0)
        self.facultyBox.setCurrentIndex(0)
        self.majorBox.setCurrentIndex(0)
        self.departmentBox.setCurrentIndex(0)
        self.idBox.setCurrentIndex(0)
        self.rankingBox.setCurrentIndex(0)
        self.evaluationsBox.setCurrentIndex(0)

        # menu bar
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClear = QtWidgets.QAction(self)
        self.actionClear.setObjectName("actionClear")
        self.actionAbout = QtWidgets.QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setObjectName("actionSave")

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("window", "BottleNeck"))

        # buttons
        self.convertButton.setText(_translate("window", "Convert"))
        self.searchButton.setText(_translate("window", "Search"))

        # radio buttons
        self.SaxApiButton.setText(_translate("window", "SAX API"))
        self.DomApiButton.setText(_translate("window", "DOM API"))

        # check(tick) boxes
        self.surnameCheckButton.setText(_translate("window", "Surname"))
        self.facultyCheckButton.setText(_translate("window", "Faculty"))
        self.departmentCheckButton.setText(_translate("window", "Department"))
        self.majorCheckButton.setText(_translate("window", "Major"))
        self.idCheckButton.setText(_translate("window", "ID"))
        self.evaluationsCheckButton.setText(_translate("window", "Evaluations"))
        self.rankingCheckButton.setText(_translate("window", "Ranking"))

        # menu bar
        self.menuFile.setTitle(_translate("window", "File"))
        self.actionOpen.setText(_translate("window", "Open"))
        self.actionClear.setText(_translate("window", "Clear"))
        self.actionAbout.setText(_translate("window", "About"))
        self.actionSave.setText(_translate("window", "Save"))
        self.actionSave.setShortcut(_translate("window", "Ctrl+S"))
