
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("codev.ne")
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(QIcon("logo.ico"))
        
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("https://codev.me"))
        self.setCentralWidget(self.web_view)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
