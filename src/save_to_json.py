import json

import save_data_interface as i
import re


class SaveToJSON(i.SaveDataInterface):
    def __init__(self):
        super().__init__()
        self.path = ''
        self.exprList = list()

    def save_data(self):
        result = {"Students": []}
        # extracting student's information
        pattern = re.compile(
            r"--\s\w{2}\:\s(\d+)\s--\n\w{7}\:\s(\w+)\n\w{7}\:\s(\w+)\n\w{5}\:\s(\d+)\n\w{10}\:\s(\w+)\n\w{11}\:\s([\d\,?\s]+)\n\w{7}\:\s(\d+)")

        for expr in self.exprList:
            it = re.finditer(pattern, expr)
            pure_value = next(it).group(0, 1, 2, 3, 4, 5, 6, 7)
            result["Students"].append(
                {
                    "ID": pure_value[1],
                    "Surname": pure_value[2],
                    "Faculty": pure_value[3],
                    "Major": pure_value[4],
                    "Department": pure_value[5],
                    "Evaluations": pure_value[6],
                    "Ranking": pure_value[7]
                })

        json_string = json.dumps(result, indent=2)
        with open(self.path, 'w') as file:
            file.write(json_string)
