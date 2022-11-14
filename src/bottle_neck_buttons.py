import application_view as view
from PyQt5 import QtCore, QtGui, QtWidgets

import scroll_area as sa

import save_to_xml
import save_to_html


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
        self.parsingType = {"Sax": True, "Dom": False}

        self.area = sa.ScrollArea(self.scrollArea)

        self.saveXML = save_to_xml.SaveToXML()
        self.saveHTML = save_to_html.SaveToHTML()

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
        self.actionAbout.triggered.connect(self.about_project)

    # buttons
    def convert_button(self):
        try:
            path = self.message.get_convert_path(self.centralwidget)[0]
            self.saveHTML.set_path(path)
            self.saveHTML.save_data()
        except:
            pass

    def search_button(self):
        self.filtering()

    # radio buttons
    def sax_api_button(self):
        self.parsingType["Sax"] = self.SaxApiButton.isChecked()
        self.parsingType["Dom"] = self.DomApiButton.isDown()

    def dom_api_button(self):
        self.parsingType["Dom"] = self.DomApiButton.isChecked()
        self.parsingType["Sax"] = self.SaxApiButton.isDown()

    # check(tick) boxes
    def surname_check_button(self):
        self.checkBoxStatusDict["Surname"] = self.surnameCheckButton.isChecked()

    def faculty_check_button(self):
        self.checkBoxStatusDict["Faculty"] = self.facultyCheckButton.isChecked()

    def department_check_button(self):
        self.checkBoxStatusDict["Department"] = self.departmentCheckButton.isChecked()

    def major_check_button(self):
        self.checkBoxStatusDict["Major"] = self.majorCheckButton.isChecked()

    def id_check_button(self):
        self.checkBoxStatusDict["ID"] = self.idCheckButton.isChecked()

    def evaluations_check_button(self):
        self.checkBoxStatusDict["Evaluations"] = self.evaluationsCheckButton.isChecked()

    def ranking_check_button(self):
        self.checkBoxStatusDict["Ranking"] = self.rankingCheckButton.isChecked()

    # menu bar
    def open_data(self):
        try:
            path = self.message.get_open_path(self.centralwidget)[0]
            if self.parsingType["Sax"]:
                self.sax_handler(path)
            else:
                self.dom_handler(path)
        except:
            pass

    def save_data(self):
        try:
            path = self.message.get_save_path(self.centralwidget)[0]
            self.saveXML.set_path(path)
            self.saveXML.save_data()
        except:
            pass

    def clear_data(self):
        self.area.clear_area()
        for box in self.boxesDict.values():
            box.clear()

    def about_project(self):
        self.message.about_project()

    # overriding functions
    def filtering(self):
        pass

    def sax_handler(self, path):
        pass

    def dom_handler(self, path):
        pass
