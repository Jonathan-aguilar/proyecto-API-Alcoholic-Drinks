import unittest
import sqlite3
import os
from Coctel import Coctel
from unittest.mock import patch
from unittest.mock import MagicMock
from api_request import DataBase
from api_request import APICOCTEL

class testintegration_api_request(unittest.TestCase):
    def setUp(self):
        self.conexion =  sqlite3.connect("Test_DataBase.db")
        cursor = self.conexion.cursor()
        self.db = DataBase('Test_Database.db')
        cursor.execute('''CREATE TABLE IF NOT EXISTS COCTELES_PREFERIDOS
                       (id Number,
                       name Text,
                       tag Text,
                       alcohol Text,
                       instructions Text,
                       imagen Text,
                       ingredients Text)'''
                       )
        
        
        #falta agregar nuestras bebidas 
        self.db.guardarBebida(bebida(12370, "Tequila Sour", "None", "Alcoholic", "Whiskey sour glass", "Shake tequila, juice of lemon, and powdered sugar with ice and strain into a whiskey sour glass. Add the half-slice of lemon, top with the cherry, and serve.", "https://www.thecocktaildb.com/images/media/drink/ek0mlq1504820601.jpg", "Tequila, Lemon, Powdered sugar, Lemon, Cherry, , , , , , , , , , , "))
        self.db.guardarBebida(bebida(13621, "Tequila Sunrise", "IBA,ContemporaryClassic", "Cocktail", "Alcoholic", "Highball glass", "Pour the tequila and orange juice into glass over ice. Add the grenadine, which will sink to the bottom. Stir gently to create the sunrise effect. Garnish and serve.", "https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg", "Tequila, Orange juice, Grenadine, , , , , , , , , , , , , "))
        self.db.guardarBebida(bebida(11000, "Mojito", "IBA,ContemporaryClassic,Alcoholic,USA", "Cocktail", "Alcoholic", "Highball glass", "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.", "https://www.thecocktaildb.com/images/media/drink/rxtqps1478251029.jpg", "Light rum, Lime, Sugar, Mint, Soda water, , , , , , , , , , , "))
        self.db.guardarBebida(bebida(12770, "Iced Coffee", "None", "Coffee / Tea", "Non alcoholic", "Coffee mug", "Mix together until coffee and sugar is dissolved. Add milk. Shake well. Using a blender or milk shake maker produces a very foamy drink. Serve in coffee mug.", "https://www.thecocktaildb.com/images/media/drink/ytprxy1454513855.jpg", "Coffee, Sugar, Water, Milk, , , , , , , , , , , , "))
        self.db.guardarBebida(bebida(11007, "Margarita", "IBA,ContemporaryClassic", "Ordinary Drink", "Alcoholic", "Cocktail glass", "Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.", "https://www.thecocktaildb.com/images/media/drink/wpxpvu1439905379.jpg", "Tequila, Triple sec, Lime juice, Salt, , , , , , , , , , , , "))

    #Elimino la base de datos
    def DBDown(self):
        self.con.close()
        self.db.con.close()
        os.remove("DataBase.db")

    #falta medio codigo
if __name__ == '__main__':
    unittest.main()
