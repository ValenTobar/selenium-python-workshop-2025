from behave import given, when, then
from selenium import webdriver
from pages.wikipedia_search_page import Wikipedia

@given('el usuario se encuentra en la pagina de principal de wikipedia')
def step_given_wikipedia_search(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://es.wikipedia.org/wiki/Wikipedia:Portada')
    context.wikipedia_search_page = Wikipedia(context.driver)

@when('el usuario escribe Python (lenguaje de programación) en la barra de busqueda')
def step_when_wikipedia_search(context):
    context.wikipedia_search_page.search("Python (lenguaje de programación)")


@then('aparece una pagina con el resultado de busqueda')
def step_then_wikipedia_search(context):
    assert "Python" in context.wikipedia_search_page.isElementPresent()
