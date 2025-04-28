Feature: Busqueda en wikipedia
    Scenario: Busqueda exitosa en wikipedia
        Given el usuario se encuentra en la pagina de principal de wikipedia
        When el usuario escribe Python (lenguaje de programación) en la barra de busqueda
        Then aparece una pagina con el resultado de busqueda