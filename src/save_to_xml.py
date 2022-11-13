import save_data_interface as i
import xml.etree.ElementTree as et


class SavingToXML(i.SavingDataInterface):
    def __init__(self):
        super().__init__()

    def save_data(self):
        my_tree = et.parse(r'D:\Programs\Pycharm\PyProjects\BottleNeck\StudentSuccess.xml')
        my_root = my_tree.getroot()
        my_root[0].clear()
        my_tree.write('new.xml')
