from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QBrush, QPainter, QColor
import sys
from random import randint


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.d = False
        uic.loadUi(r'E:\Введение в репозитории. Подключение в PyCharm. Работа с удаленным репозиторием\Second\UI.ui', self)
        self.pushButton.clicked.connect(self.draw)
    
    def draw(self):
        self.d = True
        self.update()

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.qp.setPen(QColor(255, 255, 0))
        self.drawCircle()
        self.qp.end()

    def drawCircle(self):
        if self.d:
            a = randint(0, 100)
            self.qp.drawEllipse(self.pushButton.x(), self.pushButton.y() + self.pushButton.height(), a, a)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ap = App()
    ap.show()
    sys.exit(app.exec_())
