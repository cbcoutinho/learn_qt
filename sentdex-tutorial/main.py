import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(50, 50, 500, 300)
window.setWindowTitle('PyQt4 Simple App')

window.show()
app.exec_()
