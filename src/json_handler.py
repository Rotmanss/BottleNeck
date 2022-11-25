import handler_interface as i
import json


class JsonHandler(i.HandlerInterface):
    def __init__(self, path):
        self.path = path

        self.comboBoxStatusDict = {"Surname": [], "Faculty": [], "Department": [], "Major": [], "ID": [],
                                   "Evaluations": [], "Ranking": []}
        self.result = ""

    def handle(self) -> dict:
        with open(self.path, 'r') as file:
            students_json = json.loads(file.read())['Students']

        for student in students_json:
            for key, value in student.items():
                try:
                    self.comboBoxStatusDict[key].append(value)

                    if key == "ID":
                        self.result += f"-- ID: {value} --\n"
                    elif key == "Surname":
                        self.result += f"Surname: {value}\n"
                    elif key == "Faculty":
                        self.result += f"Faculty: {value}\n"
                    elif key == "Major":
                        self.result += f"Major: {value}\n"
                    elif key == "Department":
                        self.result += f"Department: {value}\n"
                    elif key == "Evaluations":
                        self.result += f"Evaluations: {value}\n"
                    elif key == "Ranking":
                        self.result += f"Ranking: {value}\n"
                except:
                    print('Wrong object name in json file!')

        return self.comboBoxStatusDict
