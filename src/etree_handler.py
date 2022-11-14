import handler_interface as i
import xml.etree.ElementTree as ET


class EtreeHandler(i.HandlerInterface):
    def __init__(self, path):
        self.path = path

        self.comboBoxStatusDict = {"Surname": [], "Faculty": [], "Department": [], "Major": [], "ID": [],
                                   "Evaluations": [], "Ranking": []}
        self.result = ""

    def handle(self) -> dict:
        tree = ET.parse(self.path)
        root = tree.getroot()

        for x in root.findall('Student'):
            try:
                student_id = x.attrib.popitem()[1]
                surname = x.find('Surname').text
                faculty = x.find('Faculty').text
                department = x.find('Department').text
                major = x.find('Major').text
                evaluations = x.find('Evaluations').text
                ranking = x.find('Ranking').text

                self.result += f"-- ID: {student_id} --\n"
                self.result += f"Surname: {surname}\n"
                self.result += f"Faculty: {faculty}\n"
                self.result += f"Major: {major}\n"
                self.result += f"Department: {department}\n"
                self.result += f"Evaluations: {evaluations}\n"
                self.result += f"Ranking: {ranking}\n"

                self.comboBoxStatusDict["ID"].append(student_id)
                self.comboBoxStatusDict["Surname"].append(surname)
                self.comboBoxStatusDict["Faculty"].append(faculty)
                self.comboBoxStatusDict["Major"].append(major)
                self.comboBoxStatusDict["Department"].append(department)
                self.comboBoxStatusDict["Evaluations"].append(evaluations)
                self.comboBoxStatusDict["Ranking"].append(ranking)
            except:
                pass

        return self.comboBoxStatusDict

    def get_result(self):
        return self.result
