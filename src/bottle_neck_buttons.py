import application_view as view
from PyQt5 import QtCore, QtGui, QtWidgets

import sax_handler as han
import xml.sax
import scroll_area as sa


class BottleNeckButtons(view.ApplicationView):
    def __init__(self):
        super().__init__()
        self.on_event()

        self.checkBoxStatusDict = {"Surname": False, "Faculty": False, "Department": False, "Major": False, "ID": False,
                                   "Evaluations": False, "Ranking": False}
        self.boxesDict = {"Surname": self.surnameBox, "Faculty": self.facultyBox,
                                    "Department": self.departmentBox, "Major": self.majorBox,
                                    "ID": self.idBox, "Evaluations": self.evaluationsBox,
                                    "Ranking": self.rankingBox}
        self.area = sa.ScrollArea(self.scrollArea)

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
        self.filtering()

    # radio buttons
    def sax_api_button(self):
        print('sax api button')

    def dom_api_button(self):
        print('dom api button')

    # check(tick) boxes
    def surname_check_button(self):
        print('surname check button')
        self.checkBoxStatusDict["Surname"] = self.surnameCheckButton.isChecked()

    def faculty_check_button(self):
        print('faculty check button')
        self.checkBoxStatusDict["Faculty"] = self.facultyCheckButton.isChecked()

    def department_check_button(self):
        print('department check button')
        self.checkBoxStatusDict["Department"] = self.departmentCheckButton.isChecked()

    def major_check_button(self):
        print('major check button')
        self.checkBoxStatusDict["Major"] = self.majorCheckButton.isChecked()

    def id_check_button(self):
        print('id check button')
        self.checkBoxStatusDict["ID"] = self.idCheckButton.isChecked()

    def evaluations_check_button(self):
        print('evaluations check button')
        self.checkBoxStatusDict["Evaluations"] = self.evaluationsCheckButton.isChecked()

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
        clear_result = handler.get_result()

        for key in data:
            for i, value in enumerate(data[key]):
                if key == 'Surname':
                    self.surnameBox.addItem(value)
                elif key == "Faculty":
                    self.facultyBox.addItem(value)
                elif key == "Department":
                    self.departmentBox.addItem(value)
                elif key == "Major":
                    self.majorBox.addItem(value)
                elif key == "ID":
                    self.idBox.addItem(value)
                elif key == "Evaluations":
                    self.evaluationsBox.addItem(value)
                elif key == "Ranking":
                    self.rankingBox.addItem(value)
        self.parse_to_scroll_box(clear_result)

    def save_data(self):
        print('save data')

    def clear_data(self):
        print('clear data')

    def parse_to_scroll_box(self, expr):
        pass

    def filtering(self):
        pass
