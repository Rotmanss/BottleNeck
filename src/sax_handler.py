import handler_interface as i
import xml.sax


class SaxHandler(i.HandlerInterface, xml.sax.handler.ContentHandler):
    def __init__(self):
        super().__init__()
        self.comboBoxStatusDict = {"Surname": [], "Faculty": [], "Department": [], "Major": [], "ID": [],
                                   "Evaluations": [], "Ranking": []}
        self.result = ""

    def handle(self) -> dict:
        return self.comboBoxStatusDict

    def get_result(self):
        return self.result

    def startElement(self, name, attrs):
        self.current = name
        if name == "Student":
            self.result += f"-- ID: {attrs['id']} --\n"
            self.comboBoxStatusDict["ID"].append(attrs['id'])

    def characters(self, content):
        if self.current == "Surname":
            self.name = content
        elif self.current == "Faculty":
            self.faculty = content
        elif self.current == "Major":
            self.major = content
        elif self.current == "Department":
            self.department = content
        elif self.current == "Evaluations":
            self.evaluations = content
        elif self.current == "Ranking":
            self.ranking = content

    def endElement(self, name):
        if self.current == "Surname":
            self.result += f"Surname: {self.name}\n"
            self.comboBoxStatusDict["Surname"].append(self.name)
        elif self.current == "Faculty":
            self.result += f"Faculty: {self.faculty}\n"
            self.comboBoxStatusDict["Faculty"].append(self.faculty)
        elif self.current == "Major":
            self.result += f"Major: {self.major}\n"
            self.comboBoxStatusDict["Major"].append(self.major)
        elif self.current == "Department":
            self.result += f"Department: {self.department}\n"
            self.comboBoxStatusDict["Department"].append(self.department)
        elif self.current == "Evaluations":
            self.result += f"Evaluations: {self.evaluations}\n"
            self.comboBoxStatusDict["Evaluations"].append(self.evaluations)
        elif self.current == "Ranking":
            self.result += f"Ranking: {self.ranking}\n"
            self.comboBoxStatusDict["Ranking"].append(self.ranking)
        self.current = ""


def setup():
    handler = SaxHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(r'D:\Programs\Pycharm\PyProjects\BottleNeck\StudentSuccess.xml')

    return handler
