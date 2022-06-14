from behave import *


@when(u'The visitor search the "{search}" via the search box')
def step_impl(context, search):
    context.search_page.search_and_select_destination(search)


@then(u'The visitor clicks on the route')
def step_impl(context):
    context.search_page.click_route_button()


@then(u'The visitor search the "{search}" as start point')
def step_impl(context, search):
    context.search_page.search_and_select_route_start_input(search)


@then(u'The visitor click Start here')
def step_impl(context):
    context.search_page.click_start_here_button()
