from PyQt5 import QtCore, QtGui, QtWidgets

import os


class DialogFunctions:
    def __init__(self):
        self.msg = QtWidgets.QMessageBox()

    def about_project(self):
        s = 'Цей додаток створений з любов\'ю для того, щоб було зручно шукати інформацію у XML файлі!\n' \
            'Задля комфортного та естетичного перегляду інформації, ви можете конвертувати її ' \
            'у HTML формат, та відкрити його у браузері, наприклад Google Chrome, для цього натисніть Convert.\n' \
            'Підтримуються 3 формати обробки XML даних : SAX API, DOM API та Etree API.\n' \
            'Для того щоб відсортувати інформацію, поставте галочку поряд з потрібним полем, та натисніть Search.\n' \
            'Ви завжди можете очистити дані у додатку за допомогою кнопки Clear.\n' \
            'Приємного користування!'

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

    def save_before_close(self, event, widget, saving_func):
        reply = self.msg.question(widget, 'Window Close', 'Do you want to close the window without saving?',
                                  self.msg.Yes | self.msg.Save | self.msg.Cancel)
        if reply == self.msg.Yes:
            event.accept()
        elif reply == self.msg.Save:
            saving_func()
            event.ignore()
        elif reply == self.msg.Cancel:
            event.ignore()

    def save_when_reopen(self, widget, saving_func):
        reply = self.msg.question(widget, 'Window Close', 'Do you want to open new file without saving previous?', self.msg.Yes | self.msg.Save | self.msg.Cancel)
        if reply == self.msg.Save:
            saving_func()
        elif reply == self.msg.Yes:
            return True
        elif reply == self.msg.Cancel:
            pass

    def save_when_clear(self, widget, saving_func):
        reply = self.msg.question(widget, 'Window Close', 'Do you want to clear area without saving?', self.msg.Yes | self.msg.Save | self.msg.Cancel)
        if reply == self.msg.Save:
            saving_func()
        elif reply == self.msg.Yes:
            return True
        elif reply == self.msg.Cancel:
            pass
