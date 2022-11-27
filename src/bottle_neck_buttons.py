import application_view as view
from PyQt5 import QtCore, QtGui, QtWidgets

import scroll_area as sa

import save_to_xml
import save_to_html
import save_to_json


class BottleNeckButtons(view.ApplicationView):
    def __init__(self):
        super().__init__()
        self.isSaved = True
        self.on_event()

        self.checkBoxStatusDict = {"Surname": False, "Faculty": False, "Department": False, "Major": False, "ID": False,
                                   "Evaluations": False, "Ranking": False}
        self.boxesDict = {"Surname": self.surnameBox, "Faculty": self.facultyBox,
                                    "Department": self.departmentBox, "Major": self.majorBox,
                                    "ID": self.idBox, "Evaluations": self.evaluationsBox,
                                    "Ranking": self.rankingBox}
        self.parsingType = {"Sax": True, "Dom": False, "Etree": False, "Json": False}

        self.area = sa.ScrollArea(self.scrollArea)

        self.saveXML = save_to_xml.SaveToXML()
        self.saveHTML = save_to_html.SaveToHTML()
        self.saveJSON = save_to_json.SaveToJSON()

    def on_event(self):
        self.convertButton.clicked.connect(self.convert_button)
        self.searchButton.clicked.connect(self.search_button)
        self.addStudentButton.clicked.connect(self.add_student_button)
        self.delStudentButton.clicked.connect(self.del_student_button)

        self.SaxApiButton.clicked.connect(self.sax_api_button)
        self.DomApiButton.clicked.connect(self.dom_api_button)
        self.EtreeApiButton.clicked.connect(self.etree_api_button)
        self.JsonApiButton.clicked.connect(self.json_api_button)

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
            self.saveHTML.path = path
            self.saveHTML.save_data()
        except:
            self.message.wrong_file_format()

    def search_button(self):
        self.filtering()
        self.isSaved = False

    def add_student_button(self):
        pass

    def del_student_button(self):
        pass

    # radio buttons
    def sax_api_button(self):
        self.parsingType["Sax"] = self.SaxApiButton.isChecked()
        self.parsingType["Dom"] = self.DomApiButton.isDown()
        self.parsingType["Etree"] = self.EtreeApiButton.isDown()
        self.parsingType["Json"] = self.EtreeApiButton.isDown()

    def dom_api_button(self):
        self.parsingType["Dom"] = self.DomApiButton.isChecked()
        self.parsingType["Sax"] = self.SaxApiButton.isDown()
        self.parsingType["Etree"] = self.EtreeApiButton.isDown()
        self.parsingType["Json"] = self.EtreeApiButton.isDown()

    def etree_api_button(self):
        self.parsingType["Etree"] = self.EtreeApiButton.isChecked()
        self.parsingType["Sax"] = self.SaxApiButton.isDown()
        self.parsingType["Dom"] = self.DomApiButton.isDown()
        self.parsingType["Json"] = self.EtreeApiButton.isDown()

    def json_api_button(self):
        self.parsingType["Json"] = self.JsonApiButton.isChecked()
        self.parsingType["Sax"] = self.SaxApiButton.isDown()
        self.parsingType["Dom"] = self.DomApiButton.isDown()
        self.parsingType["Etree"] = self.EtreeApiButton.isDown()

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
            if self.isSaved:
                path = self.message.get_open_path(self.centralwidget)[0]
                if self.parsingType["Sax"]:
                    self.sax_handler(path)
                elif self.parsingType["Dom"]:
                    self.dom_handler(path)
                elif self.parsingType["Etree"]:
                    self.etree_handler(path)
                elif self.parsingType["Json"]:
                    self.json_handler(path)
            else:
                if self.message.save_when_reopen(self.centralwidget, self.save_data):
                    path = self.message.get_open_path(self.centralwidget)[0]
                    if self.parsingType["Sax"]:
                        self.sax_handler(path)
                    elif self.parsingType["Dom"]:
                        self.dom_handler(path)
                    elif self.parsingType["Etree"]:
                        self.etree_handler(path)
                    elif self.parsingType["Json"]:
                        self.json_handler(path)
        except:
            self.message.wrong_file_format()

    def save_data(self):
        try:
            path, extension = self.message.get_save_path(self.centralwidget)
            if extension == 'XML File (*.xml)':
                self.saveXML.path = path
                self.saveXML.save_data()
            elif extension == 'JSON File (*.json)':
                self.saveJSON.path = path
                self.saveJSON.save_data()

            self.isSaved = True
        except:
            self.message.wrong_file_format()

    def clear_data(self):
        if self.isSaved:
            self.area.clear()
            for box in self.boxesDict.values():
                box.clear()
        else:
            if self.message.save_when_clear(self.centralwidget, self.save_data):
                self.area.clear()
                for box in self.boxesDict.values():
                    box.clear()
                self.isSaved = True

    def about_project(self):
        self.message.about_project()

    def append_combo_boxes(self, data):
        for key, value in data.items():
            for element in value:
                if self.boxesDict[key].findText(str(element)) == -1:  # if not found, 0 if found
                    self.boxesDict[key].addItem(str(element))

    # overriding functions
    def filtering(self):
        pass

    def sax_handler(self, path):
        pass

    def dom_handler(self, path):
        pass

    def etree_handler(self, path):
        pass

    def json_handler(self, path):
        pass
