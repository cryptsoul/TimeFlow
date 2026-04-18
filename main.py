import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPainter, QBrush, QColor, QPen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #window
        self.setWindowTitle("TimeFlow")
        self.setGeometry(400, 200, 1000, 700)
        self.setStyleSheet("background-color: #202D34;")

        #Title
        lTitle = QLabel("TimeFlow", self)
        lTitle.setFont(QFont("Arial", 30))
        lTitle.setStyleSheet("color: white; background: transparent;")
        lTitle.setGeometry(0, 0, 200, 50)
        lTitle.setAlignment(Qt.AlignCenter)
    
    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor(1, 161, 180)))
        painter.drawRect(0, 0, self.width(), 50)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
