import save_data_interface as i
import re


class SaveToHTML(i.SaveDataInterface):
    def __init__(self):
        super().__init__()
        self.path = ''
        self.exprList = list()

    def save_data(self):
        file = open(self.path, 'w+')
        result = "<!DOCTYPE html>\n" \
                 "<html>\n" \
                 "<head>\n\t" \
                    "<title>BottleNeck</title>\n\t" \
                 "<style>\n\t" \
                 "body {background-color: lavender}\n\t" \
                 "table, th, td {border: 2px solid black; border-collapse: collapse}\n\t" \
                 "th {background-color: #FDDF95}\n\t" \
                 "th, td {padding: 10px; width: 150px}\n\t" \
                 "td {background-color: #ccff99}\n\t" \
                 "h1 {text-shadow: 0 0 3px #9F00EAFF}\n\t" \
                 "</style>\n" \
                 "</head>\n" \
                 "<body>\n\t" \
                 "<table align=center>\n\t" \
                    "<caption><h1>Bottle neck data</h1></caption>\n\t" \
                    "<tr>\n\t\t" \
                        "<th>Student ID</th>\n\t\t" \
                        "<th>Surname</th>\n\t\t" \
                        "<th>Faculty</th>\n\t\t" \
                        "<th>Major</th>\n\t\t" \
                        "<th>Department</th>\n\t\t" \
                        "<th>Evaluations</th>\n\t\t" \
                        "<th>Ranking</th>\n\t" \
                    f"</tr>\n\t"

        # extracting student's information
        pattern = re.compile(
            r"--\s\w{2}\:\s(\d+)\s--\n\w{7}\:\s(\w+)\n\w{7}\:\s(\w+)\n\w{5}\:\s(\d+)\n\w{10}\:\s(\w+)\n\w{11}\:\s([\d\,?\s]+)\n\w{7}\:\s(\d+)")

        for expr in self.exprList:
            it = re.finditer(pattern, expr)
            pure_value = next(it).group(0, 1, 2, 3, 4, 5, 6, 7)

            result += f"<tr>\n\t\t" \
                        f"<td>{pure_value[1]}</td>\n\t\t" \
                        f"<td>{pure_value[2]}</td>\n\t\t" \
                        f"<td>{pure_value[3]}</td>\n\t\t" \
                        f"<td>{pure_value[4]}</td>\n\t\t" \
                        f"<td>{pure_value[5]}</td>\n\t\t" \
                        f"<td>{pure_value[6]}</td>\n\t\t" \
                        f"<td>{pure_value[7]}</td>\n\t" \
                      f"</tr>\n\t"

        result += "</table>\n" \
                  "</body>\n" \
                  "</html>"

        file.write(result)
        file.close()

    def set_path(self, path):
        self.path = path

    def set_expression(self, value):
        self.exprList = value
