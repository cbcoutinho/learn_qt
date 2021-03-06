import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('PyQt4 Tutorial')
        self.setWindowIcon(QtGui.QIcon('resources/myicon.png'))
        self.centerOnScreen()

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

        # *** Simple toolbar
        extractAction = QtGui.QAction(QtGui.QIcon('resources/myicon.png'), 'Get out', self)
        extractAction.triggered.connect(self.close_application)
        extractAction.setStatusTip('Leave The App')

        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)

        # *** Simple checkbox for enlarging window
        checkBox = QtGui.QCheckBox('Enlarge Window', self)
        checkBox.move(100,25)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.show()

    def centerOnScreen (self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
              (resolution.height() / 2) - (self.frameSize().height() / 2))

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

        self.centerOnScreen()


    def close_application(self):

        choice = QtGui.QMessageBox.question(self,
                                            'Extract!',
                                            'Really want to quit?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            print('Leaving now')
            sys.exit()
        else:
            pass


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
