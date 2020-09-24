
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.common import myconst
from src.common.selenium import Selenium
from PIL import ImageGrab
import os
import time
import unittest
import yaml

class Scenario(Selenium, unittest.TestCase):
    # constructor of unittest class
    @classmethod
    def setUpClass(self,classname):
        filepath = myconst.cst.MOCK_FOLDER_PATH + classname + '.yml'
        with open(filepath) as file:
            self.yaml = yaml.safe_load(file)

    # destructor of unittest class
    @classmethod
    def tearDownClass(self):
        pass

    # the action before each of tests is executed in unittest 
    def setUp(self):
        raise NotImplementedError()

    # the action after each of tests is executed in unittest
    def tearDown(self):
        raise NotImplementedError()
