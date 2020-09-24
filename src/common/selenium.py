
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.common import myconst
from PIL import ImageGrab
import os
import time
import yaml

class Selenium:
    # set webdriver
    def setWebdriver(self):
        # setting chrome driver
        chrome_options = Options()
        chrome_options.add_argument(f"--window-size={myconst.cst.CHROME_DRIVER_WINDOW_SIZE}")
        if not myconst.cst.CHROME_DRIVER_BROWSER:
            chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(
                options=chrome_options,
                executable_path= myconst.cst.CHROME_DRIVER_PATH)
        # for wait loading
        self.driver.implicitly_wait(10)
        # for wait javascript function
        self.driver.set_script_timeout(10)
        # go to the root url if root url is existed
        if 'url' in self.yaml['data']:
            if self.yaml['data']['url'] is not None and 'root' in self.yaml['data']['url']:
                self.driver.get(self.yaml['data']['url']['root'])

    # go to the specified url page
    def toPage(self, url):
        self.driver.get(url)
        WebDriverWait(
            self.driver, 10).until(
            ExpectedConditions.presence_of_all_elements_located)

    # trimming blank character in first and last
    def trimStr(self, str):
        return str.lstrip().rstrip()

    # waiting until display specific element
    def waitDisplayElementByClass(self, class_name):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ExpectedConditions.presence_of_element_located((By.CLASS_NAME, class_name)))
        time.sleep(1)

    # waiting until complete ajax action
    def waitCompleteAjax(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: self.driver.execute_script(
            "return jQuery.active == 0"))
        time.sleep(1)

    # waiting until display alert
    def waitDisplayAlert(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ExpectedConditions.alert_is_present())
        time.sleep(1)

    # save a screenshot
    def getScreenshot(self, case_name, image_name=None, zoom_ratio=100):
        script = "document.body.style.zoom='{}%'"
        self.driver.execute_script(script.format(zoom_ratio))
        if image_name is not None:
            base_filepath = myconst.cst.LOG_FOLDER + case_name + '-' + image_name
        else:
            base_filepath = myconst.cst.LOG_FOLDER + case_name
        index = 1
        filepath = base_filepath + f"-{str(index).zfill(3)}" + '.png'
        while(os.path.isfile(filepath)):
            index += 1
            filepath = base_filepath + f"-{str(index).zfill(3)}" + '.png'
        self.driver.save_screenshot(filepath)

    # save a screenshot (alert only, and target is main screen only)
    # main screen -> If you use a laptop, laptop's screen is main screen.
    def getAlertScreenshot(self, case_name):
        img = ImageGrab.grab()
        img.save(myconst.cst.LOG_FOLDER + case_name + '-alert.png')

    # find & click the element by id.
    def clickById(self, id):
        self.driver.find_element_by_id(id).click()

    # find & click the element by name. (It is the first element found.)
    def clickByName(self, name):
        self.driver.find_element_by_name(name).click()

    # find & click the element by link text. (It is the first element found.)
    def clickByText(self, text):
        self.driver.find_element_by_partial_link_text(text).click()

    # find & click the element by class. (It is the first element found.)
    def clickByClass(self, classname):
        self.driver.find_element_by_class_name(classname).click()

    # scroll to the element.
    def scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # scroll to the element by id.
    def scrollById(self, id):
        element = self.driver.find_element_by_id(id)
        self.scroll(element)

    # scroll to the element by name. (It is the first element found.)
    def scrollByName(self, name):
        element = self.driver.find_element_by_name(name)
        self.scroll(element)

    # scroll to the element by link text. (It is the first element found.)
    def scrollByText(self, text):
        element = self.driver.find_element_by_partial_link_text(text)
        self.scroll(element)

    # scroll to the element by class. (It is the first element found.)
    def scrollByClass(self, classname):
        element = self.driver.find_element_by_class_name(classname)
        self.scroll(element)

    # set the value on the textbox by id.
    def setTextboxById(self, id, value):
        element = self.driver.find_element_by_id(id)
        element.send_keys(value)

    # set the value on the textbox by name. (It is the first element found.)
    def setTextboxByName(self, name, value):
        element = self.driver.find_element_by_name(name)
        element.send_keys(value)

    # set the value on the textbox by class. (It is the first element found.)
    def setTextboxByClass(self, classname):
        element = self.driver.find_element_by_class_name(classname)
        element.send_keys(value)

    # set the value on the selectbox by id.
    def setSelectboxById(self, id, value):
        select = Select(self.driver.find_element_by_id(id))
        select.select_by_visible_text(value)

    # set the value on the selectbox by name. (It is the first element found.)
    def setSelectboxByName(self, name, value):
        select = Select(self.driver.find_element_by_name(name))
        select.select_by_visible_text(value)

    # set the value on the selectbox by class. (It is the first element found.)
    def setSelectboxByClass(self, classname):
        select = Select(self.driver.find_element_by_class_name(classname))
        select.select_by_visible_text(value)

    # get options on the selectbox by id.
    def getSelectboxOptionsById(self, id):
        select = Select(self.driver.find_element_by_id(id))
        option_texts = list()
        for option in select.options:
            text = self.trimStr(option.text)
            option_texts.append(text)
        return select, option_texts

    # get options on the selectbox by name. (It is the first element found.)
    def getSelectboxOptionsByName(self, name):
        select = Select(self.driver.find_element_by_name(name))
        option_texts = list()
        for option in select.options:
            text = self.trimStr(option.text)
            option_texts.append(text)
        return select, option_texts