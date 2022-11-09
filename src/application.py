import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import bottle_neck as bonk

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = bonk.BottleNeck()
    ui.show()
    sys.exit(app.exec_())
