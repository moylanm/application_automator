#!/usr/bin/env python
# -*- coding: latin-1 -*-
from PySide6.QtCore import Qt, QRect
from helpers import create_form_fields
from PySide6.QtWidgets import QMainWindow

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
        create_form_fields(self)
