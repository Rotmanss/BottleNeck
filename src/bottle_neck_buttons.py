import application_view as view
from PyQt5 import QtCore, QtGui, QtWidgets

import sax_handler as han
import xml.sax


class BottleNeckButtons(view.ApplicationView):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.on_event()

        self.checkBoxStatusDict = {"Surname": False, "Faculty": False, "Department": False, "Major": False, "ID": False,
                                   "Evaluations": False, "Ranking": False}

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

        self.actionOpen.triggered.connect(self.open_data)
        self.actionSave.triggered.connect(self.save_data)
        self.actionClear.triggered.connect(self.clear_data)

    # buttons
    def convert_button(self):
        print(self.evaluationsBox.currentText())
        print(self.evaluationsBox.currentIndex())
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
        self.checkBoxStatusDict["Surname"] = self.surnameCheckButton.isChecked()
        print(self.checkBoxStatusDict)

    def faculty_check_button(self):
        print('faculty check button')
        self.checkBoxStatusDict["Faculty"] = self.surnameCheckButton.isChecked()

    def department_check_button(self):
        print('department check button')
        self.checkBoxStatusDict["Department"] = self.surnameCheckButton.isChecked()

    def major_check_button(self):
        print('major check button')
        self.checkBoxStatusDict["Major"] = self.surnameCheckButton.isChecked()

    def id_check_button(self):
        print('id check button')
        self.checkBoxStatusDict["ID"] = self.surnameCheckButton.isChecked()

    def evaluations_check_button(self):
        print('evaluations check button')
        self.checkBoxStatusDict["Evaluations"] = self.surnameCheckButton.isChecked()

    def ranking_check_button(self):
        print('ranking check button')
        self.checkBoxStatusDict["Ranking"] = self.surnameCheckButton.isChecked()

    # menu bar
    def open_data(self):
        handler = han.SaxHandler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(r'D:\Programs\Pycharm\PyProjects\BottleNeck\StudentSuccess.xml')

        data = handler.handle()

        for key in data:
            if key == 'Surname':
                for value in data[key]:
                    self.surnameBox.addItem(value)
            elif key == "Faculty":
                for value in data[key]:
                    self.facultyBox.addItem(value)
            elif key == "Department":
                for value in data[key]:
                    self.departmentBox.addItem(value)
            elif key == "Major":
                for value in data[key]:
                    self.majorBox.addItem(value)
            elif key == "ID":
                for value in data[key]:
                    self.idBox.addItem(value)
            elif key == "Evaluations":
                for value in data[key]:
                    self.evaluationsBox.addItem(value)
            elif key == "Ranking":
                for value in data[key]:
                    self.rankingBox.addItem(value)

        print(data)

    def save_data(self):
        print('save data')

    def clear_data(self):
        print('clear data')
