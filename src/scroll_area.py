from PyQt5 import QtCore, QtGui, QtWidgets


class ScrollArea(QtWidgets.QTextEdit):
    def __init__(self, scrollArea):
        super().__init__()
        self.setGeometry(QtCore.QRect(510, 0, 551, 671))
        self.area = scrollArea

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.setFont(font)

        self.setReadOnly(True)

    def append_area(self, item_list):
        for item in item_list:
            self.append(item)

        self.area.setWidget(self)
