import bottle_neck_buttons as btn
from PyQt5 import QtCore, QtGui, QtWidgets

import re


class BottleNeck(btn.BottleNeckButtons):
    def __init__(self):
        super().__init__()
        self.pure_value_list = list()

    def parse_to_scroll_box(self, expr):
        # pattern = re.compile(r"--\s\w{2}\s(\d+)\s--\n\w{7}\:\s(\w+)\n\w{7}\:\s(\w+)\n\w{5}\:\s(\d+)\n\w{10}\:\s(\w+)\n\w{11}\:\s(\d+)\n\w{7}\:\s(\d+)")
        # for it in re.finditer(pattern, expr):
        #     pure_value = it.group(0, 1, 2, 3, 4, 5, 6, 7)
        #     print(pure_value[0])

        pattern = re.compile(r"(--\s\w{2}\s\d+\s--\n\w{7}\:\s\w+\n\w{7}\:\s\w+\n\w{5}\:\s\d+\n\w{10}\:\s\w+\n\w{11}\:\s\d+\n\w{7}\:\s\d+)")
        for pure_value in re.findall(pattern, expr):
            self.pure_value_list.append(pure_value)

        self.area.fill_area(self.pure_value_list)

    def filtering(self):
        filtered_pure_value_list = [i for i in self.pure_value_list.copy()]
        key_words = list()

        for key, status in self.checkBoxStatusDict.items():
            if status:
                print(self.boxesDict[key].currentText())
                key_words.append(self.boxesDict[key].currentText())

        for pattern in key_words:
            re_pattern = re.compile(pattern)
            for data in self.pure_value_list:
                if not re.findall(re_pattern, data):
                    filtered_pure_value_list.remove(data)

        self.area.clear_area()
        self.area.fill_area(filtered_pure_value_list)

