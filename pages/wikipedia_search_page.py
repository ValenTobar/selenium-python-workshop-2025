from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class Wikipedia(BasePage):
    SEARCH_FIELD = (By.NAME, 'search')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/form/div/button')
    CONFIRM_MSG = (By.XPATH, '/html/body/div[2]/div/div[3]/main/header/h1/span')

    def search(self, searching):
        self.enter_text(self.SEARCH_FIELD, searching)
        self.click(self.SEARCH_BUTTON)

    def isElementPresent(self):
        elemento = self.find_element(self.CONFIRM_MSG)
        texto = elemento.text
        return texto
    