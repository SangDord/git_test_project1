import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.qp = QPainter()
        self.flag = False
        self.pushBtn.clicked.connect(self.is_draw)

    def is_draw(self):
        self.flag = True
        self.update()
        
    def draw_circle(self):
        rad = randint(20, 100)
        pen = self.qp.pen()
        pen.setColor(QColor(255, 255, 0))
        self.qp.setPen(pen)
        self.qp.drawEllipse(randint(0, 500 - 2 * rad), randint(0, 600 - 2 * rad), rad, rad)
        
    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_circle()
            self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
