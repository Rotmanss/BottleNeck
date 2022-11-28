from PyQt5 import QtCore, QtGui, QtWidgets

import os


class DialogFunctions:
    def __init__(self):
        self.msg = QtWidgets.QMessageBox()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.msg.setFont(font)

    def about_project(self):
        s = 'Цей додаток створений з любов\'ю для того, щоб було зручно шукати інформацію у XML або JSON файлі ' \
            'у яких зберігається інформація про студента!\n\n' \
            'Задля комфортного та естетичного перегляду інформації, ви можете конвертувати її ' \
            'у HTML формат, та відкрити його у браузері, наприклад Google Chrome, для цього натисніть Convert.\n\n' \
            'Підтримуються 3 формати обробки XML даних : SAX API, DOM API та Etree API. ' \
            'Для обробки JSON файлу, натисніть кнопочку \'JSON\' над кнопкою Search, та відкрийте файл.\n\n' \
            'ПОПЕРЕДЖЕННЯ: студента буде ПРОІГНОРОВАНО, якщо його атрибут або вміст атрибуту ' \
            'не буде відповідати нижче наведеним шаблонам:\n\n\t' \
            'Для XML файлів:\n\t' \
            '<Student id = "100">\n\t\t' \
                '<Surname>Pevny</Surname>\n\t\t' \
                '<Faculty>CSC</Faculty>\n\t\t' \
                '<Major>122</Major>\n\t\t' \
                '<Department>OR</Department>\n\t\t' \
                '<Evaluations>10, 11,232 9</Evaluations>\n\t\t' \
                '<Ranking>1</Ranking>\n\t' \
            '</Student>\n\n\t' \
            'Для JSON файлів:\n\t\t' \
            '{\n\t\t' \
              '"ID": 100,\n\t\t' \
              '"Surname": "Pevny",\n\t\t' \
              '"Faculty": "CSC",\n\t\t' \
              '"Major": 122,\n\t\t' \
              '"Department": "OR",\n\t\t' \
              '"Evaluations": "10, 11,232 9",\n\t\t' \
              '(якщо оцінка одна, її можна записати без\n\t\tкавичок, наприклад: "Evaluations": 5)\n\t\t' \
              '"Ranking": 1\n\t\t' \
            '}\n\n' \
            'Для того щоб відсортувати інформацію, поставте галочку поряд з потрібним полем, та натисніть Search.\n' \
            'Ви завжди можете очистити дані у додатку за допомогою кнопки Clear.\n' \
            'Щоб додати або видалити студента, натисніть конпку Add student/Remove student відповідно.\n' \
            'Для збереження у файл JSON або XML ОБЕРІТЬ ПРАВИЛЬНЕ РОЗШИРЕННЯ ФАЙЛУ та натисніть Save.\n' \
            'Приємного користування!'

        self.msg.setIcon(self.msg.Information)
        self.msg.setWindowTitle("About project")
        self.msg.setText(s)
        self.msg.setStandardButtons(self.msg.Ok)
        self.msg.exec_()

    def get_open_path(self, parent):
        return QtWidgets.QFileDialog.getOpenFileName(parent, 'Select a file', os.getcwd()[:-4],
                                                     'XML File (*.xml);; JSON File (*.json)', 'JSON File (*.json)')

    def get_save_path(self, parent):
        return QtWidgets.QFileDialog.getSaveFileName(parent, 'Select a file', os.getcwd()[:-4],
                                                     'XML File (*.xml);; JSON File (*.json)', 'JSON File (*.json)')

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

    def wrong_file_format(self):
        self.msg.setIcon(self.msg.Critical)
        self.msg.setWindowTitle("Error")
        self.msg.setText("Incorrect file format!")
        self.msg.setStandardButtons(self.msg.Ok)
        self.msg.exec_()

    def wrong_data_input(self):
        self.msg.setIcon(self.msg.Critical)
        self.msg.setWindowTitle("Error")
        self.msg.setText("You have wrong fields in file, student was skipped")
        self.msg.setStandardButtons(self.msg.Ok)
        self.msg.exec_()

    def remove_error(self):
        self.msg.setIcon(self.msg.Critical)
        self.msg.setWindowTitle("Error")
        self.msg.setText("List does not have this student!")
        self.msg.setStandardButtons(self.msg.Ok)
        self.msg.exec_()

    def confirm_deletion(self, widget):
        reply = self.msg.question(widget, 'Delete student', 'Do you want to delete student?',
                                  self.msg.Yes | self.msg.Cancel)
        if reply == self.msg.Yes:
            return True
        elif reply == self.msg.Cancel:
            return False

    def fill_all_fields(self):
        self.msg.setIcon(self.msg.Warning)
        self.msg.setWindowTitle("Warning")
        self.msg.setText("You have to fill all fields in this form!")
        self.msg.setStandardButtons(self.msg.Ok)
        self.msg.exec_()
