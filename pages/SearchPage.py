from selenium.webdriver import Keys
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    search_input_box = (By.XPATH, "//input[@name='searchInput']")
    route_start_input_box = (By.NAME, "routeStartInput")
    route_start_search_button = (By.XPATH, "//li[@class='show-results-area long-title']")
    search_button = (By.XPATH, "//mat-icon[text()='search']")
    list = (By.XPATH, "//ul[@class='list-group ng-scope']/li")
    ivion_splash_screen = (By.XPATH, "//div[@id='ivion-splash-screen']")
    results_list = (By.XPATH, "//ul[@class='list-group ng-scope']")
    route_button = (By.XPATH, "//span[text()='Route']/parent::button")
    start_here_button = (By.XPATH, "//div[text()=' Start here ']")

    def __init__(self, driver):
        super().__init__(driver)

    def search(self, search_value):
        self.send_keys(self.search_input_box, search_value)

    def click_search_button(self):
        self.click(self.search_button)

    def search_and_select_destination(self, search_value):
        self.wait_till_element_invisibility(self.ivion_splash_screen)
        self.search(search_value)
        self.click_search_button()
        self.select_from_searched_result(search_value)

    def search_and_select_route_start_input(self, search_value):
        self.send_keys(self.route_start_input_box, search_value)
        self.click(self.route_start_search_button)
        self.select_from_searched_result(search_value)

    def select_from_searched_result(self, search_value):
        self.wait_visible(self.results_list)
        elements = self.get_elements(self.list)
        for e in elements:
            if search_value in e.text.replace("\n", " ").replace(" •", ""):
                e.click()
                break

    def click_route_button(self):
        self.click(self.route_button)

    def click_start_here_button(self):
        self.click(self.start_here_button)
