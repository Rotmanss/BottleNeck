from PyQt5 import QtCore, QtGui, QtWidgets

import os


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

    def get_open_path(self, parent):
        return QtWidgets.QFileDialog.getOpenFileName(parent, 'Select a file', os.getcwd()[:-4],
                                                     'XML File (*.xml)', 'XML File (*.xml)')

    def get_save_path(self, parent):
        return QtWidgets.QFileDialog.getSaveFileName(parent, 'Select a file', os.getcwd()[:-4], 'XML File (*.xml)',
                                                     'XML File (*.xml)')

    def get_convert_path(self, parent):
        return QtWidgets.QFileDialog.getSaveFileName(parent, 'Select a file', os.getcwd()[:-4], 'HTML File (*.html)',
                                                     'HTML File (*.html)')
# reopen
# close
# clear
# dublication in box
