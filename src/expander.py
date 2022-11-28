from PyQt5 import QtCore, QtGui, QtWidgets
import changer_interface as i
import dialog_functions


class Expander(QtWidgets.QWidget, i.ChangerInterface):
    def __init__(self, add_func):
        super().__init__()
        self.add_func = add_func

        # window settings
        self.setWindowTitle("Expander")
        self.resize(540, 340)
        self.setMinimumSize(QtCore.QSize(540, 340))
        self.setMaximumSize(QtCore.QSize(540, 340))
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: #ccff99")

        self.comboBoxStatusDict = {"Surname": [], "Faculty": [], "Department": [], "Major": [], "ID": [],
                                   "Evaluations": [], "Ranking": []}

    def open_changer(self):
        # font setting
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)

        form_layout = QtWidgets.QFormLayout()
        self.setLayout(form_layout)

        # fields setting
        # ID
        id_line = QtWidgets.QLineEdit(self)
        id_line.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("\d*")))
        id_line.setFont(font)
        id_label = QtWidgets.QLabel("ID:")
        id_label.setFont(font)

        # Surname
        surname_line = QtWidgets.QLineEdit(self)
        surname_line.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z]*")))
        surname_line.setFont(font)
        surname_label = QtWidgets.QLabel("Surname:")
        surname_label.setFont(font)

        # Faculty
        faculty_line = QtWidgets.QLineEdit(self)
        faculty_line.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z]*")))
        faculty_line.setFont(font)
        faculty_label = QtWidgets.QLabel("Faculty:")
        faculty_label.setFont(font)

        # Major
        major_line = QtWidgets.QLineEdit(self)
        major_line.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("\d*")))
        major_line.setFont(font)
        major_label = QtWidgets.QLabel("Major:")
        major_label.setFont(font)

        # Department
        department_line = QtWidgets.QLineEdit(self)
        department_line.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z]*")))
        department_line.setFont(font)
        department_label = QtWidgets.QLabel("Department:")
        department_label.setFont(font)

        # Evaluations
        evaluations_line = QtWidgets.QLineEdit(self)
        evaluations_line.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[\d\,\s]*")))
        evaluations_line.setFont(font)
        evaluations_label = QtWidgets.QLabel("Evaluations:")
        evaluations_label.setFont(font)

        # Ranking
        ranking_line = QtWidgets.QLineEdit(self)
        ranking_line.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("\d*")))
        ranking_line.setFont(font)
        ranking_label = QtWidgets.QLabel("Ranking:")
        ranking_label.setFont(font)

        # show fields on form
        form_layout.addRow(id_label, id_line)
        form_layout.addRow(surname_label, surname_line)
        form_layout.addRow(faculty_label, faculty_line)
        form_layout.addRow(major_label, major_line)
        form_layout.addRow(department_label, department_line)
        form_layout.addRow(evaluations_label, evaluations_line)
        form_layout.addRow(ranking_label, ranking_line)

        # commit button
        self.CommitButton = QtWidgets.QPushButton(self)
        self.CommitButton.setText("Commit")
        self.CommitButton.setGeometry(QtCore.QRect(20, 280, 500, 40))
        self.CommitButton.setFont(font)
        self.CommitButton.setStyleSheet("background-color:rgb(255, 250, 80)")

        self.CommitButton.clicked.connect(lambda: commit_button())
        self.show()
        form_layout.deleteLater()

        def commit_button():
            if id_line.text() != '' and surname_line.text() != '' and faculty_line.text() != '' \
            and major_line.text() != '' and department_line.text() != '' and evaluations_line.text() != '' \
            and ranking_line.text() != '':
                result = ''
                result += f"-- ID: {id_line.text()} --\n"
                result += f"Surname: {surname_line.text()}\n"
                result += f"Faculty: {faculty_line.text()}\n"
                result += f"Major: {major_line.text()}\n"
                result += f"Department: {department_line.text()}\n"
                result += f"Evaluations: {evaluations_line.text()}\n"
                result += f"Ranking: {ranking_line.text()}"

                self.comboBoxStatusDict["ID"].append(id_line.text())
                self.comboBoxStatusDict["Surname"].append(surname_line.text())
                self.comboBoxStatusDict["Faculty"].append(faculty_line.text())
                self.comboBoxStatusDict["Major"].append(major_line.text())
                self.comboBoxStatusDict["Department"].append(department_line.text())
                self.comboBoxStatusDict["Evaluations"].append(evaluations_line.text())
                self.comboBoxStatusDict["Ranking"].append(ranking_line.text())

                self.add_func(self.comboBoxStatusDict, result)
            else:
                msg = dialog_functions.DialogFunctions()
                msg.fill_all_fields()
