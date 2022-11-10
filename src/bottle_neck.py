import bottle_neck_buttons as btn
from PyQt5 import QtCore, QtGui, QtWidgets

import sax_handler as han
import xml.sax

class BottleNeck(btn.BottleNeckButtons):
    def __init__(self):
        super().__init__()
        self.result_area()

    def parse_to_combo_boxes(self):
        pass

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
