from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    menu_icon = (By.ID, "tooltip-0")
    mark_and_measure_in_menu = (By.ID, "tooltip-11")
    mark_and_measure_in_left_panel = (By.XPATH, "//span[@id='tooltip-7']")
    ivion_splash_screen = (By.XPATH, "//div[@id='ivion-splash-screen']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_menu(self):
        self.click(self.menu_icon)

    def click_mark_and_measure_from_menu(self):
        self.wait_till_element_invisibility(self.ivion_splash_screen)
        self.open_menu()
        self.click(self.mark_and_measure_in_menu)

    def click_mark_and_measure_from_left_panel(self):
        self.wait_till_element_invisibility(self.ivion_splash_screen)
        self.click(self.mark_and_measure_in_left_panel)


