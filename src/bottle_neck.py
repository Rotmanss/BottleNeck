import bottle_neck_buttons as btn
from PyQt5 import QtCore, QtGui, QtWidgets

import re


class BottleNeck(btn.BottleNeckButtons):
    def __init__(self):
        super().__init__()

    def parse_to_scroll_box(self, expr):
        # pattern = re.compile(r"--\s\w{2}\s(\d+)\s--\n\w{7}\:\s(\w+)\n\w{7}\:\s(\w+)\n\w{5}\:\s(\d+)\n\w{10}\:\s(\w+)\n\w{11}\:\s(\d+)\n\w{7}\:\s(\d+)")
        # for it in re.finditer(pattern, expr):
        #     pure_value = it.group(0, 1, 2, 3, 4, 5, 6, 7)
        #     print(pure_value[0])

        pure_value_list = list()
        pattern = re.compile(r"(--\s\w{2}\s\d+\s--\n\w{7}\:\s\w+\n\w{7}\:\s\w+\n\w{5}\:\s\d+\n\w{10}\:\s\w+\n\w{11}\:\s\d+\n\w{7}\:\s\d+)")
        for pure_value in re.findall(pattern, expr):
            pure_value_list.append(pure_value)

        self.area.fill_area(pure_value_list)

    def filtering(self):
        pass
