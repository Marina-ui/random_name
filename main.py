from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from random import randint
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('circles.ui', self)

        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.circles(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def circles(self, qp):
        qp.setBrush(QColor(Qt.yellow))
        n = randint(1, 5)
        for i in range(n):
            r1 = randint(20, 200)
            r2 = r1
            r3 = randint(200, 400)
            r4 = r3
            qp.drawEllipse(r1, r2, r3, r4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())