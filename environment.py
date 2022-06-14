import platform
from selenium import webdriver

from pages.MarkAndMeasurePage import MarkAndMeasurePage
from pages.SearchPage import SearchPage
from pages.HomePage import HomePage


def before_all(context):
    if platform.system() == 'Windows':
        context.executable_path = 'chromedriver.exe'
    else:
        context.executable_path = './chromedriver'

    context.driver = webdriver.Chrome(executable_path=context.executable_path)
    context.driver.maximize_window()
    context.home_page = HomePage(context.driver)
    context.search_page = SearchPage(context.driver)
    context.mark_and_measure_page = MarkAndMeasurePage(context.driver)


def after_all(context):
    print('-----------------END-----------------')
    context.driver.close()
