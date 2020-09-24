from src.common import const as cst
import platform

class Myconst:
    #----------------------------------------------#
    # CHROME DRIVER
    #----------------------------------------------#
    # DRIVER PATH
    if 'macOS' in platform.platform():
        cst.CHROME_DRIVER_PATH = '/usr/local/bin/chromedriver'
    elif 'Windows' in platform.platform():
        cst.CHROME_DRIVER_PATH = 'C:\\programs\\chromedriver'
    # WHETHER TO USE BROWSER OR NOT (True / False)
    cst.CHROME_DRIVER_BROWSER = True
    # WINDOW SIZE (Width / Height)
    cst.CHROME_DRIVER_WINDOW_SIZE = '1920,1080'

    #----------------------------------------------#
    # LOG
    #----------------------------------------------#
    cst.LOG_FOLDER_PATH = "log/"
    cst.LOG_FOLDER_NAME = "seleniumci"

    #----------------------------------------------#
    # MOCKDATA
    #----------------------------------------------#
    cst.MOCK_FOLDER_PATH = "mockdata/"

    #----------------------------------------------#
    # USER
    #----------------------------------------------#
    cst.USER_EMAIL_ADULT = "adult@test.com"
    cst.USER_EMAIL_UNDERAGE = "underage@test.com"
    cst.USER_PASSWORD = "Password1234"
