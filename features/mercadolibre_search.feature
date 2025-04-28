Feature: Buscar iphone13 en mercadolibre
    Scenario: Busqueda exitosa de producto
        Given el usuario se encuentra en la pagina principal de mercadolibre
        When el usuario escribe iPhone 13 en la barra de busqueda
        Then aparecen resultados con la palabra iPhone