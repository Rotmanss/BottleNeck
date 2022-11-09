import application_view as view
from PyQt5 import QtCore, QtGui, QtWidgets


class BottleNeck(view.ApplicationView):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.result_area()
        self.on_event()

    def result_area(self):
        result = QtWidgets.QListWidget()

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        result.setFont(font)

        result.addItems(["Onsadfasdfasdfasdfasddfasdfasdfasd\nasdfdasfasdf\nasdfasdfasf\nasdfasdfas\nasdfasdfe", "Two", "Three"])

        result.currentItemChanged.connect(self.get_item)
        result.currentTextChanged.connect(self.get_text)

        self.scrollArea.setWidget(result)

    def get_item(self, item):
        print(item.text())
        QtWidgets.QListWidgetItem = "Hello"
        item.setText("Hello")

    def get_text(self, text):
        print(text)

    def on_event(self):
        self.convertButton.clicked.connect(self.convert_button)
        self.searchButton.clicked.connect(self.search_button)

        self.SaxApiButton.clicked.connect(self.sax_api_button)
        self.DomApiButton.clicked.connect(self.dom_api_button)

        self.surnameCheckButton.clicked.connect(self.surname_check_button)
        self.facultyCheckButton.clicked.connect(self.faculty_check_button)
        self.departmentCheckButton.clicked.connect(self.department_check_button)
        self.majorCheckButton.clicked.connect(self.major_check_button)
        self.idCheckButton.clicked.connect(self.id_check_button)
        self.evaluationsCheckButton.clicked.connect(self.evaluations_check_button)
        self.rankingCheckButton.clicked.connect(self.ranking_check_button)

    # buttons
    def convert_button(self):
        print('convert button')

    def search_button(self):
        print('search button')

    # radio buttons
    def sax_api_button(self):
        print('sax api button')

    def dom_api_button(self):
        print('dom api button')

    # check(tick) boxes
    def surname_check_button(self):
        print('surname check button')

    def faculty_check_button(self):
        print('faculty check button')

    def department_check_button(self):
        print('department check button')

    def major_check_button(self):
        print('major check button')

    def id_check_button(self):
        print('id check button')

    def evaluations_check_button(self):
        print('evaluations check button')

    def ranking_check_button(self):
        print('ranking check button')
