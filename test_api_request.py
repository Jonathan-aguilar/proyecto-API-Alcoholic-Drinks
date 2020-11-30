import unittest
import sqlite3
import os
from Coctel import Coctel
from unittest.mock import patch
from unittest.mock import MagicMock
from api_request import DataBase
from api_request import APICOCTEL

class test_api_request(unittest.TestCase):
    @patch('requests.get')
    
    def searchname_test(self,mock):
        test_cases=(
            ("Ace",['Ace'],lambda:{"coctel:"[{"strDrink:" "Ace"}]}),
            ("Rose",['Rose','Amaretto Rose'],lambda:{"coctel:"[{"strDrink:" "Rose"},{"strDrink:" "Amaretto Rose"}]}),
            ("Zorro",['Zorro'],lambda:{"coctel:"[{"strDrink:" "Zorro"}]})
        )
        
        search = APICOCTEL()
        
        for entrada,salida_esperada,function in test_cases:
            mock.return_value.status_code=200
            mock.return_value.json=function
            
            salida_real = search.search_name(entrada)
            self.assertEqual(salida_real,salida_esperada)
            
    @patch('requests.get')
    def test_getcoctel(self,mock):
        test_cases=(
            ()
        )
        
        search = APICOCTEL()
        
        for entradanum,entradanom,function,esperada in test_cases:
            mock.return_value.status.code = 200
            mock.return_value.json=function
            salida_real = buscar.getcoctel(entradanum,entradanom)
            print(type(salida_real.id))
            print(esperada.id)
            self.assertEqual(salida_real.id,esperada.id)
                   
    