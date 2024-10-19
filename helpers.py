#!/usr/bin/env python
# -*- coding: latin-1 -*-
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QLabel, QLineEdit

FORM_METADATA = [
    {"label": "URL :", "label_geometry": QRect(15, 10, 60, 30), "field_type": QLineEdit, "field_geometry": QRect(70, 10, 690, 30), "field_name": "url_field", "attr": "url"},
    {"label": "CAPTCHA :", "label_geometry": QRect(25, 50, 60, 30), "field_type": QLineEdit, "field_geometry": QRect(70, 50, 690, 30), "field_name": "captcha_field", "attr": "captcha"}
]

def create_form_fields(parent):
    for el in FORM_METADATA:
        label = QLabel(el["label"], parent)
        label.setGeometry(el["label_geometry"])

        field = el["field_type"](parent)
        field.setGeometry(el["label_geometry"])

        setattr(parent, el["field_name"], field)
