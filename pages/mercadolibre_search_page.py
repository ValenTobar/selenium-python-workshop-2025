from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class MercadoLibre(BasePage):
    SEARCH_FIELD = (By.ID, 'cb1-edit')
    SEARCH_BUTTON = (By.XPATH, '/html/body/header/div/div[2]/form/button')
    ELEMENTS_MSG = (By.XPATH, '/html/body/main/div/div[2]/section/div[7]/ol/li[1]/div/div/div/div[2]/h3/a')

    def search(self, nameproduct):
        self.enter_text(self.SEARCH_FIELD, nameproduct)
        self.click(self.SEARCH_BUTTON)

    def isElementPresent(self):
        elemento = self.find_element(self.ELEMENTS_MSG)
        texto = elemento.text
        return texto 
    
    
