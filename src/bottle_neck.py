import bottle_neck_buttons as btn
from PyQt5 import QtCore, QtGui, QtWidgets

import re

import sax_handler
import dom_handler
import etree_handler
import json_handler

import expander
import reducer

# input control
# delete from combo boxes


class BottleNeck(btn.BottleNeckButtons):
    def __init__(self):
        super().__init__()
        self.pure_value_list = list()

        self.expander = expander.Expander(self.on_add)
        self.reducer = reducer.Reducer(self.on_remove)

    def closeEvent(self, event):
        if self.isSaved is not True:
            self.message.save_before_close(event, self.centralwidget, self.save_data)

        self.expander.close()
        self.reducer.close()

    def parse_to_scroll_area(self, expr):
        self.pure_value_list.clear()

        # searching and extracting a student
        pattern = re.compile(
            r"--\s\w{2}\:\s\d+\s--\n\w{7}\:\s\w+\n\w{7}\:\s\w+\n\w{5}\:\s\d+\n\w{10}\:\s\w+\n\w{11}\:\s[\d\,?\s]+\n\w{7}\:\s\d+")
        for pure_value in re.findall(pattern, expr):
            self.pure_value_list.append(pure_value)

        self.area.clear()
        self.area.append_area(self.pure_value_list)
        self.saveXML.exprList = self.pure_value_list
        self.saveJSON.exprList = self.pure_value_list
        self.saveHTML.exprList = self.pure_value_list

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

        self.area.clear()
        self.area.append_area(filtered_pure_value_list)
        self.saveXML.exprList = filtered_pure_value_list
        self.saveJSON.exprList = filtered_pure_value_list
        self.saveHTML.exprList = filtered_pure_value_list

    def sax_handler(self, path):
        self.unpacking_data(sax=True, path=path)

    def dom_handler(self, path):
        self.unpacking_data(dom=True, path=path)

    def etree_handler(self, path):
        self.unpacking_data(etree=True, path=path)

    def json_handler(self, path):
        self.unpacking_data(json=True, path=path)

    def unpacking_data(self, sax=False, dom=False, etree=False, json=False, path=''):
        handler = None
        if sax:
            handler = sax_handler.setup(path)
        elif dom:
            handler = dom_handler.DomHandler(path)
        elif etree:
            handler = etree_handler.EtreeHandler(path)
        elif json:
            handler = json_handler.JsonHandler(path)

        box_data = handler.handle()
        pure_result = handler.result

        self.append_combo_boxes(box_data)
        self.parse_to_scroll_area(pure_result)

    def add_student_button(self):
        self.change_data(expand=True)

    def del_student_button(self):
        self.change_data(reduce=True)

    def change_data(self, expand=False, reduce=False):
        if expand:
            self.expander.open_changer()
        elif reduce:
            self.reducer.open_changer()

    # function for updating students list after adding new student
    def on_add(self, box_data, student):
        self.append_combo_boxes(box_data)

        self.area.append_area([student])
        self.pure_value_list.append(student)

        self.saveXML.exprList.append(student)
        self.saveJSON.exprList.append(student)
        self.saveHTML.exprList.append(student)
        self.isSaved = False

    # function for updating students list after removing student
    def on_remove(self, box_data, student):
        try:
            self.pure_value_list.remove(student)
            self.area.clear()
            self.area.append_area(self.pure_value_list)

            self.saveXML.exprList = self.pure_value_list
            self.saveJSON.exprList = self.pure_value_list
            self.saveHTML.exprList = self.pure_value_list
            self.isSaved = False
        except:
            self.message.remove_error()
