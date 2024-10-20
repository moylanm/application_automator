#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QLabel, QLineEdit, QMainWindow, QPushButton
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class MainUI(QMainWindow):

    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.setup_window()
        self.init_ui()

        with open('form_data.json') as f:
            self.form_data = json.load(f)

    def setup_window(self):
        self.setWindowTitle('Application Automator')
        self.resize(600, 300)
        self.move(1000, 200)

    def init_ui(self):
        self.url_label = QLabel('URL:', self)
        self.url_label.setGeometry(QRect(15, 10, 60, 30))
        self.url_field = QLineEdit(self)
        self.url_field.setGeometry(QRect(15, 40, 400, 30))

        self.captcha_label = QLabel('CAPTCHA:', self)
        self.captcha_label.setGeometry(QRect(15, 75, 70, 30))
        self.captcha_field = QLineEdit(self)
        self.captcha_field.setGeometry(QRect(15, 105, 100, 30))

        self.create_button('fill', QRect(15, 140, 75, 30), self.fill_application)
        self.create_button('submit', QRect(95, 140, 75, 30), self.submit_application)

    def create_button(self, text, geometry, callback):
        button = QPushButton(text.title(), self)
        button.setObjectName(text)
        button.setGeometry(geometry)
        button.clicked.connect(callback)

    def fill_application(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        wait = WebDriverWait(driver, 5)

        driver.maximize_window()
        driver.get(self.url_field.text())

        driver.find_element(By.XPATH, self.form_data['interested-button-xpath']).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.form_data['submit-button-xpath'])))

        #for item in self.form_data['basic-information']:
        #    driver.find_element(By.XPATH, item['xpath']).send_keys(item['value'])

        #for item in self.form_data['address-information']:
        #    driver.find_element(By.XPATH, item['xpath']).send_keys(item['value'])
        #    driver.switch_to.active_element.send_keys(Keys.ESCAPE)

        #skill_set_form = self.form_data['professional-details']['skill-set-form']
        #skill_set_input = driver.find_element(By.XPATH, skill_set_form['input-xpath'])

        #for item in self.form_data['professional-details']['skills']:
        #    skill_set_input.send_keys(item['skill'])
        #    button_string = f"{item['level']}-button-xpath"
        #    wait.until(EC.element_to_be_clickable((By.XPATH, skill_set_form[button_string])))
        #    driver.find_element(By.XPATH, skill_set_form[button_string]).click()
        #    driver.find_element(By.XPATH, skill_set_form['skill-button-xpath']).click()
        #    skill_set_input.clear()
        #    sleep(0.4)

        #driver.find_element(By.XPATH, self.form_data['education-add-button-xpath']).click()

        #for item in self.form_data['education-details']['input-fields']:
        #    driver.find_element(By.XPATH, item['xpath']).send_keys(item['value'])

        #for item in self.form_data['education-details']['date-fields']:
        #    driver.find_element(By.XPATH, item['dropdown-xpath']).click()
        #    driver.switch_to.active_element.send_keys(item['value'])
        #    sleep(0.1)
        #    driver.switch_to.active_element.send_keys(Keys.ENTER)
        #    driver.switch_to.active_element.send_keys(Keys.ENTER)



        sleep(5)

    def submit_application(self):
        pass
