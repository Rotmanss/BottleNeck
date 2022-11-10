import bottle_neck_buttons as btn
from PyQt5 import QtCore, QtGui, QtWidgets


class BottleNeck(btn.BottleNeckButtons):
    def __init__(self):
        super().__init__()
        self.result_area()

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
