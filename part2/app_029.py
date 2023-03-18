import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from part2.util import Color


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = Color('red')
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
