from behave import *


@given(u'A visitor is on the web page of Munich headquarter in NavVis IVION')
def step_impl(context):
    context.driver.get("https://hq.iv.navvis.com/")


@when(u'The visitor navigate to the Mark & Measure tool via the measurement icon')
def step_impl(context):
    context.home_page.click_mark_and_measure_from_left_panel()


@when(u'The visitor navigate to the Mark & Measure tool via the menu')
def step_impl(context):
    context.home_page.click_mark_and_measure_from_menu()


@then(u'The visitor clicks on the vertical distance measure')
def step_impl(context):
    context.mark_and_measure_page.click_vertical_distance_measurement_type()


@then(u'The visitor pick "{x_coordinate}" and "{y_coordinate}" coordinates')
def step_impl(context, x_coordinate, y_coordinate):
    context.mark_and_measure_page.pick_vertical_points(x_coordinate, y_coordinate)

