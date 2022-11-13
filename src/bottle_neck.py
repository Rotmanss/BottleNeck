import bottle_neck_buttons as btn
from PyQt5 import QtCore, QtGui, QtWidgets

import re

import sax_handler
import dom_handler


class BottleNeck(btn.BottleNeckButtons):
    def __init__(self):
        super().__init__()
        self.pure_value_list = list()

    def parse_to_scroll_area(self, expr):
        pattern = re.compile(r"--\s\w{2}\:\s\d+\s--\n\w{7}\:\s\w+\n\w{7}\:\s\w+\n\w{5}\:\s\d+\n\w{10}\:\s\w+\n\w{11}\:\s[\d\,?\s]+\n\w{7}\:\s\d+")
        for pure_value in re.findall(pattern, expr):
            self.pure_value_list.append(pure_value)

        self.area.clear_area()
        self.area.fill_area(self.pure_value_list)

    def filtering(self):
        filtered_pure_value_list = [i for i in self.pure_value_list]
        key_words = list()

        for key, status in self.checkBoxStatusDict.items():
            if status:
                key_words.append(f"{key}: {self.boxesDict[key].currentText()}")

        for pattern in key_words:
            re_pattern = re.compile(pattern)
            for data in self.pure_value_list:
                if not re.findall(re_pattern, data):
                    try:
                        filtered_pure_value_list.remove(data)
                    except:
                        pass

        self.area.clear_area()
        self.area.fill_area(filtered_pure_value_list)
        self.save.set_expression(filtered_pure_value_list)

    def sax_handler(self):
        self.unpacking_data(sax=True)

    def dom_handler(self):
        self.unpacking_data(dom=True)

    def unpacking_data(self, sax=False, dom=False):
        self.clear_data()
        self.pure_value_list.clear()

        handler = None
        if sax:
            handler = sax_handler.setup()
        elif dom:
            handler = dom_handler.DomHandler()

        data = handler.handle()
        pure_result = handler.get_result()

        for key in data:
            for value in data[key]:
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

        self.parse_to_scroll_area(pure_result)
