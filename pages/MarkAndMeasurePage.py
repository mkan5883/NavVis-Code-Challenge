from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class MarkAndMeasurePage(BasePage):
    vertical_distance_button = (By.XPATH, "//mat-icon[@title='Vertical Distance']/*[name()='svg']")
    canvas = (By.XPATH, "(//canvas[@data-engine='three.js r139'])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_vertical_distance_measurement_type(self):
        self.click(self.vertical_distance_button)

    def pick_vertical_points(self, x_coordinates, y_coordinates):
        canvas_dimensions = self.get_element(self.canvas)
        self.click_x_y_coordinates_relative_to_an_element(canvas_dimensions, x_coordinates, y_coordinates)

