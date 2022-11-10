import handler_interface as i
import xml.sax


class SaxHandler(i.HandlerInterface, xml.sax.handler.ContentHandler):
    def __init__(self):
        super().__init__()
        self.comboBoxStatusDict = {"Surname": [], "Faculty": [], "Department": [], "Major": [], "ID": [],
                                   "Evaluations": [], "Ranking": []}

    def handle(self) -> dict:
        return self.comboBoxStatusDict

    def startElement(self, name, attrs):
        self.current = name
        if name == "Student":
            print(f"-- Person {attrs['id']} --")
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
            print(f"Surname: {self.name}")
            self.comboBoxStatusDict["Surname"].append(self.name)
        elif self.current == "Faculty":
            print(f"Faculty: {self.faculty}")
            self.comboBoxStatusDict["Faculty"].append(self.faculty)
        elif self.current == "Major":
            print(f"Major: {self.major}")
            self.comboBoxStatusDict["Major"].append(self.major)
        elif self.current == "Department":
            print(f"Department: {self.department}")
            self.comboBoxStatusDict["Department"].append(self.department)
        elif self.current == "Evaluations":
            print(f"Evaluations: {self.evaluations}")
            self.comboBoxStatusDict["Evaluations"].append(self.evaluations)
        elif self.current == "Ranking":
            print(f"Ranking: {self.ranking}")
            self.comboBoxStatusDict["Ranking"].append(self.ranking)
        self.current = ""
