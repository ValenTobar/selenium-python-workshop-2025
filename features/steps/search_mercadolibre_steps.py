from behave import given, when, then
from selenium import webdriver
from pages.mercadolibre_search_page import MercadoLibre

@given('el usuario se encuentra en la pagina principal de mercadolibre')
def step_given_mercadolibre_search(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co/')
    context.mercadolibre_search_page = MercadoLibre(context.driver)

@when('el usuario escribe iPhone 13 en la barra de busqueda')
def step_when_mercadolibre_search(context):
    context.mercadolibre_search_page.search("iPhone 13")


@then('aparecen resultados con la palabra iPhone')
def step_then_mercadolibre_search(context):
    assert "iPhone" in context.mercadolibre_search_page.isElementPresent()
