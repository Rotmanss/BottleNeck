import save_data_interface as i
import xml.etree.ElementTree as et
import re


class SaveToXML(i.SavingDataInterface):
    def __init__(self):
        super().__init__()
        self.exprList = list()

    def save_data(self):
        file = open(r'D:\Programs\Pycharm\PyProjects\BottleNeck\new.xml', 'w+')
        result = "<?xml version=\"1.0\" ?>\n" \
                 "<Students>\n\t"

        pattern = re.compile(
            r"--\s\w{2}\:\s(\d+)\s--\n\w{7}\:\s(\w+)\n\w{7}\:\s(\w+)\n\w{5}\:\s(\d+)\n\w{10}\:\s(\w+)\n\w{11}\:\s([\d\,?\s]+)\n\w{7}\:\s(\d+)")

        for expr in self.exprList:
            it = re.finditer(pattern, expr)
            pure_value = next(it).group(0, 1, 2, 3, 4, 5, 6, 7)

            result += f"<Student id = \"{pure_value[1]}\">\n\t\t" \
                      f"<Surname>{pure_value[2]}</Surname>\n\t\t" \
                      f"<Faculty>{pure_value[3]}</Faculty>\n\t\t" \
                      f"<Major>{pure_value[4]}</Major>\n\t\t" \
                      f"<Department>{pure_value[5]}</Department>\n\t\t" \
                      f"<Evaluations>{pure_value[6]}</Evaluations>\n\t\t" \
                      f"<Ranking>{pure_value[7]}</Ranking>\n\t" \
                      f"</Student>\n\t"
        result += "</Students>"

        file.write(result)

    def set_expression(self, value):
        self.exprList = value
