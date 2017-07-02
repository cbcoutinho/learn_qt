import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('PyQt4 Tutorial')
        self.setWindowIcon(QtGui.QIcon('resources/myicon.png'))

        # *** Main menu ***
        extractAction = QtGui.QAction('&GET TO THE CHOPPA', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.statusBar()
        self.home()

    def home(self):
        btn = QtGui.QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.setStatusTip('Leave The App')

        # btn.resize(100,100)
        # btn.resize(btn.sizeHint())
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)

        extractAction = QtGui.QAction(QtGui.QIcon('resources/myicon.png'), 'Get out', self)
        extractAction.triggered.connect(self.close_application)
        extractAction.setStatusTip('Leave The App')

        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)




        self.show()

    def close_application(self):
        # print('Woooah!')
        sys.exit()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
