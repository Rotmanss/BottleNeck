from PyQt5 import QtCore, QtGui, QtWidgets


class ScrollArea(QtWidgets.QListWidget):
    def __init__(self, scrollArea):
        super().__init__()
        self.area = scrollArea

    def fill_area(self, item_list):
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.setFont(font)

        self.addItems(item_list)

        self.currentItemChanged.connect(self.get_item)
        self.currentTextChanged.connect(self.get_text)

        self.area.setWidget(self)

    def get_item(self, item):
        # QtWidgets.QListWidgetItem = "Hello"
        #item.setText("Hello")
        print(item)

    def get_text(self, text):
        print(text)

    def clear_area(self):
        self.clear()
