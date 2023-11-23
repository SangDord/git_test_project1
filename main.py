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
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(int(250 - rad / 2),
                            int(300 - rad / 2), rad, rad)
        
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