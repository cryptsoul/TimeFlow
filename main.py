import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controls()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 1000, 700)
        self.setWindowTitle("TimeFlow")
        self.setStyleSheet("background-color: #202D34;")
        
    def controls(self):
       lTitle=QLabel("TimeFlow", self)
       lTitle.setFont(QFont("Arial", 30))
       lTitle.setGeometry(0,0,500,100)
       lTitle.setAlignment(Qt.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
