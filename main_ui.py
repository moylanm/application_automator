#!/usr/bin/env python
# -*- coding: latin-1 -*-
from PySide6.QtCore import Qt, QRect
from helpers import create_form_elements
from PySide6.QtWidgets import QMainWindow, QPushButton

class MainUI(QMainWindow):

    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.setup_window()
        self.init_ui()

    def setup_window(self):
        self.setWindowTitle("Application Automator")
        self.resize(600, 300)
        self.move(1000, 200)

    def init_ui(self):
        create_form_elements(self)
        self.create_button("Fill", QRect(15, 140, 75, 30), self.fill_application)
        self.create_button("Submit", QRect(95, 140, 75, 30), self.submit_application)

    def create_button(self, text, geometry, callback):
        button = QPushButton(text, self)
        button.setGeometry(geometry)
        button.clicked.connect(callback)

    def fill_application(self):
        pass

    def submit_application(self):
        pass
