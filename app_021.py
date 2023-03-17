import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        # Отправляет текущий индекс (позицию) выбранного элемента.
        widget.currentIndexChanged.connect(self.index_changed)

        # Есть альтернативный сигнал отправки текста.
        widget.editTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i): # i — это int
        print(i)

    def text_changed(self, s): # s — это str
        print(s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
