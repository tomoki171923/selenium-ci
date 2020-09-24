# How to execute this file
# Executing the follow command.
# python3 ./SchoolQuotation_case3_reservation.py -v

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.common import myconst
from src.scenario import scenario
import unittest
import datetime
import pathlib
import os
import sys
import platform
import termcolor
import time

class case1_sample(scenario.Scenario):

    # unittest上での事実上のコンストラクタ
    @classmethod
    def setUpClass(self):
        super().setUpClass(classname)

    # unittest上test実施前処理
    def setUp(self):
        self.setWebdriver()
        self.toReservationPage()

    # unittest上各test実施後処理
    def tearDown(self):
        # close chrome driver
        self.driver.close()

    # go to the reservation page.
    def toReservationPage(self):
        self.toPage(self.yaml['data']['url']['option'])
        option_form = self.yaml['data']['form']['quotation']['option']
        self.setSelectboxById(option_form['stay']['id'], option_form['stay']['text'])
        self.clickById('btn-result')
        self.scrollByClass('next-step')
        self.clickByText('留学カウンセリング予約')

    # 初期描画時のフォーム項目テスト
    def execInitTest(self, case_name):
        case_form = self.yaml['data']['form'][case_name]['set']
        self.scrollByClass('form_sections')
        self.getScreenshot(case_name ,'init')
        self.scrollByName('comment')
        self.getScreenshot(case_name ,'init')
        # checkbox
        case_form_check = case_form['check']['counselings']
        checkbox_texts = list()
        # 15は余裕値（今後checkboxが増えた時用）
        for i in range(15):
            id = case_form_check['id'] + str(i)
            try:
                element = self.driver.find_element_by_id(id)
                # 補足：Nuxt 上ではvalue = labeltextでコーディングしている
                checkbox_texts.append(element.get_attribute("value"))
            except:
                # element が見つからなかったらbreak
                break
        with self.subTest(msg=f"init checkbox test"):
            self.assertEqual(checkbox_texts, case_form_check['values'])
        # text box
        case_form_text = case_form['text']
        for form in case_form_text:
            element = self.driver.find_element_by_name(case_form_text[form]['name'])
            with self.subTest(msg=f"init text test"):
                self.assertEqual(element.text, case_form_text[form]['text'])
        # select option
        case_form_option = case_form['option']
        for form in case_form_option:
            select, options = self.getSelectboxOptionsByName(case_form_option[form]['name'])
            init_option = self.trimStr(select.all_selected_options[0].text)
            with self.subTest(msg=f"init select test"):
                self.assertEqual(options, case_form_option[form]['values'])
                self.assertEqual(init_option, case_form_option[form]['text'])



    # 各フォーム項目バリデーションテスト
    def execValidationTest(self, case_name: str, case_type="error"):
        case_form = self.yaml['data']['form'][case_name]
        self.scrollByClass('form_sections')
        self.setTextboxByName(case_form['set']['name'], case_form['set']['text'])
        self.getScreenshot(case_name ,case_form['set']['name'])
        if case_type == "error":
            element = self.driver.find_element_by_class_name('err-text')
        elif case_type == "success":
            element = self.driver.find_element_by_class_name('alert_currect')
        with self.subTest(msg=f"{case_form['set']['name']} validation test"):
            self.assertEqual(
                element.text, case_form['msg'])

    # 各フォーム項目Null値テスト
    def execNullTest(self, case_name: str):
        case_form = self.yaml['data']['form'][case_name]
        name = case_form['set']['name']
        self.scrollByClass('form_sections')
        element = self.driver.find_element_by_name(name)
        self.getScreenshot(case_name ,name)
        element.send_keys(Keys.TAB)
        self.getScreenshot(case_name ,name)
        element = self.driver.find_element_by_class_name('err-text')
        with self.subTest(msg=f"{name} null test"):
            self.assertEqual(
                element.text, case_form['msg'])

    # Submitボタン挙動テスト
    def execSubmitTest(self, case_name, case_type="error"):
        case_form = self.yaml['data']['form'][case_name]['set']
        case_form_text = case_form['text']
        self.scrollByClass('form_sections')
        for form in case_form_text:
            self.setTextboxByName(case_form_text[form]['name'], case_form_text[form]['text'])
        case_form_option = case_form['option']
        for form in case_form_option:
            self.setSelectboxByName(case_form_option[form]['name'], case_form_option[form]['text'])
        if 'radio' in case_form:
            self.clickByClass(case_form['radio']['agree']['class'])
        self.getScreenshot(case_name ,'submit')
        self.scrollByName('comment')
        submit = self.driver.find_element_by_id('submitBtn')
        self.getScreenshot(case_name ,'submit')
        with self.subTest(msg=f"submit test"):
            if case_type=="error":
                self.assertEqual(submit.is_enabled(), False)
            elif case_type == "success":
                self.assertEqual(submit.is_enabled(), True)


    # ---------------------init item test begin
    def test_case01(self):
        self.execInitTest(sys._getframe().f_code.co_name)
    # ---------------------init item test end
    
    # ---------------------validation item test begin
    def test_case02(self):
        self.execValidationTest(sys._getframe().f_code.co_name)

    
    def test_case03(self):
        self.execValidationTest(sys._getframe().f_code.co_name)
        
    
    def test_case04(self):
        self.execValidationTest(sys._getframe().f_code.co_name)

    
    def test_case05(self):
        self.execValidationTest(sys._getframe().f_code.co_name)

    
    def test_case06(self):
        self.execNullTest(sys._getframe().f_code.co_name)

    
    def test_case07(self):
        self.execNullTest(sys._getframe().f_code.co_name)

    
    def test_case08(self):
        self.execNullTest(sys._getframe().f_code.co_name)

    
    def test_case09(self):
        self.execNullTest(sys._getframe().f_code.co_name)

    
    def test_case10(self):
        self.execValidationTest(sys._getframe().f_code.co_name)

    
    def test_case11(self):
        self.execValidationTest(sys._getframe().f_code.co_name)

    
    def test_case12(self):
        self.execValidationTest(sys._getframe().f_code.co_name , "success")

    
    def test_case13(self):
        self.execValidationTest(sys._getframe().f_code.co_name , "success")

    
    def test_case14(self):
        self.execValidationTest(sys._getframe().f_code.co_name , "success")

    
    def test_case15(self):
        self.execValidationTest(sys._getframe().f_code.co_name , "success")

    
    def test_case16(self):
        self.execValidationTest(sys._getframe().f_code.co_name)

    
    def test_case17(self):
        self.execValidationTest(sys._getframe().f_code.co_name)

    
    def test_case18(self):
        self.execValidationTest(sys._getframe().f_code.co_name)

    
    def test_case19(self):
        self.execValidationTest(sys._getframe().f_code.co_name)

    
    def test_case20(self):
        self.execValidationTest(sys._getframe().f_code.co_name , "success")

    
    def test_case21(self):
        self.execValidationTest(sys._getframe().f_code.co_name , "success")

    
    def test_case22(self):
        self.execValidationTest(sys._getframe().f_code.co_name , "success")

    
    def test_case23(self):
        self.execValidationTest(sys._getframe().f_code.co_name , "success")

    
    def test_case24(self):
        self.execValidationTest(sys._getframe().f_code.co_name)

    
    def test_case25(self):
        self.execValidationTest(sys._getframe().f_code.co_name)

    
    def test_case26(self):
        self.execValidationTest(sys._getframe().f_code.co_name)

    
    def test_case27(self):
        self.execValidationTest(sys._getframe().f_code.co_name)
    # ---------------------validation item test end

    # ---------------------submit test begin
    
    def test_case28(self):
        self.execSubmitTest(sys._getframe().f_code.co_name)

    
    def test_case29(self):
        self.execSubmitTest(sys._getframe().f_code.co_name)

    
    def test_case30(self):
        self.execSubmitTest(sys._getframe().f_code.co_name)

    
    def test_case31(self):
        self.execSubmitTest(sys._getframe().f_code.co_name , "success")
    # ---------------------submit test end

if __name__ == '__main__':
    date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    classname = os.path.splitext(os.path.basename(__file__))[0]
    myconst.cst.LOG_FOLDER = myconst.cst.LOG_FOLDER_PATH + myconst.cst.LOG_FOLDER_NAME + '_' + date + '_' + classname + '/'
    os.makedirs(myconst.cst.LOG_FOLDER)
    logpath = myconst.cst.LOG_FOLDER + classname + '.log'

    #unittest.main()
    with pathlib.Path(logpath).open('w') as fw:
        date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        fw.write(
        f'******************* SELENIUM TEST START : {date} *******************\n'
        '\n')
        unittest.main(
            testRunner=unittest.TextTestRunner(
            stream=fw,
            descriptions=False,
            verbosity=2))
