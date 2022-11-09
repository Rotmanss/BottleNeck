import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import src.application_view as bottle_neck

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = bottle_neck.BottleNeck()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
