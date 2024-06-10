from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
QLineEdit, QPushButton, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")