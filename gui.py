import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

class Window(QManiWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Lumiere")
        self.setMinimumHeight(500)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
