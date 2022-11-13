from PyQt5 import QtCore, QtGui, QtWidgets


class DialogFunctions:
    def __init__(self):
        self.msg = QtWidgets.QMessageBox()

    def about_project(self):
        s = 'Цей додаток оброблює, фільтрує та конвертує XML'
        self.msg.setIcon(self.msg.Information)
        self.msg.setWindowTitle("About project")
        self.msg.setText(s)
        self.msg.setStandardButtons(self.msg.Ok)
        self.msg.exec_()
