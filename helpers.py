#!/usr/bin/env python
# -*- coding: latin-1 -*-
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QLabel, QLineEdit

FORM_METADATA = [
    {"label": "URL:", "label_geometry": QRect(15, 10, 60, 30), "field_geometry": QRect(15, 40, 400, 30), "field_name": "url_field"},
    {"label": "CAPTCHA:", "label_geometry": QRect(15, 75, 70, 30), "field_geometry": QRect(15, 105, 100, 30), "field_name": "captcha_field"}
]

def create_form_elements(parent):
    for el in FORM_METADATA:
        label = QLabel(el["label"], parent)
        label.setGeometry(el["label_geometry"])

        field = QLineEdit(parent)
        field.setGeometry(el["field_geometry"])

        setattr(parent, el["field_name"], field)
