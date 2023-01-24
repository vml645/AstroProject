import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap

class PixInsightApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set the main window properties
        self.setWindowTitle("PixInsight App")
        self.setGeometry(100, 100, 600, 400)
        
        # Create a menu bar and add actions
        self.create_menu_bar()
        
        # Create a label to display the image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 30, 580, 340)
        
        self.show()
        
    def create_menu_bar(self):
        # Create a menu bar and add actions
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        
        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_image)
        self.file_menu.addAction(open_action)
        
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        self.file_menu.addAction(exit_action)

    def open_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.xpm *.jpg *.bmp);;All Files (*)", options=options)
        if file_name:
            # Set the image to the label
            self.image_label.setPixmap(QPixmap(file_name))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PixInsightApp()
    sys.exit(app.exec_())
