import handler_interface as i
import xml.dom.minidom


class DomHandler(i.HandlerInterface):
    def __init__(self):
        super().__init__()
        self.comboBoxStatusDict = {"Surname": [], "Faculty": [], "Department": [], "Major": [], "ID": [],
                                   "Evaluations": [], "Ranking": []}
        self.result = ""

    def handle(self):
        domtree = xml.dom.minidom.parse(r'D:\Programs\Pycharm\PyProjects\BottleNeck\StudentSuccess.xml')

        group = domtree.documentElement
        students = group.getElementsByTagName('Student')

        for student in students:
            surname = student.getElementsByTagName('Surname')[0].childNodes[0].nodeValue
            faculty = student.getElementsByTagName('Faculty')[0].childNodes[0].nodeValue
            major = student.getElementsByTagName('Major')[0].childNodes[0].nodeValue
            department = student.getElementsByTagName('Department')[0].childNodes[0].nodeValue
            evaluations = student.getElementsByTagName('Evaluations')[0].childNodes[0].nodeValue
            ranking = student.getElementsByTagName('Ranking')[0].childNodes[0].nodeValue

            self.result += f"-- ID: {student.getAttribute('id')} --\n"
            self.result += f"Surname: {surname}\n"
            self.result += f"Faculty: {faculty}\n"
            self.result += f"Major: {major}\n"
            self.result += f"Department: {department}\n"
            self.result += f"Evaluations: {evaluations}\n"
            self.result += f"Ranking: {ranking}\n"

            self.comboBoxStatusDict["ID"].append(student.getAttribute('id'))
            self.comboBoxStatusDict["Surname"].append(surname)
            self.comboBoxStatusDict["Faculty"].append(faculty)
            self.comboBoxStatusDict["Major"].append(major)
            self.comboBoxStatusDict["Department"].append(department)
            self.comboBoxStatusDict["Evaluations"].append(evaluations)
            self.comboBoxStatusDict["Ranking"].append(ranking)

        return self.comboBoxStatusDict

    def get_result(self):
        return self.result
