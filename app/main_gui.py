from PyQt6.QtWidgets import QApplication
from app.gui.main_window import MainWindow
import sys

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Moodle Desktop")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
