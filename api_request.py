import sqlite3
import requests
import GETAPI
import GetDB
from Coctel import Coctel

class APICOCTEL(GETAPI.GETAPI):
    def searchName(self, bebida_name):
        url= 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + bebida_name
        response = requests.get(url)
        
        if response.status_code == 200:
            response_json = response.json()
            id_coctel = response_json['coctels']
            
        i=0
        namecoctels = []
        characteristics = []
        
        for identification in id_coctel:
            identification = id_cocteli].get ("strDrink")
            namecoctels.append((f"Coctel {identification} number {i}"))
            
            identification = id_coctel[i]
            characteristics.append(identification)
            i+=1
        return namecoctels
    
    def getCoctel(self,selection,bebida_name):
        url = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + bebida_name
        response = requests.get(url)
        
        if response.status_code == 200:
            response_json = response.json()
            id_coctel = response_json['coctels']
            
        id = id_coctel[selection].get("idDrink")
        name = id_coctel[selection].get("strDrink")
        tag = id_coctel[selection].get("strTags")
        alcohol = id_coctel[selection].get("strAlcoholic")
        instructions = id_coctel[selection].get("strInstructions")
        imagen = id_coctel[selection].get("strDrinkThumb")
        ingredients=""
        ingredient=1
        while ingredient <= 15:
            if id_coctel[selection].get(f"strIngredient{ingredient}") != "" or id_coctel[selection].get(f"strIngredient{ingredient}") != " " or id_coctel[selection].get(f"strIngredient{ingredient}") is None:
                ingredients += id_coctel[selection].get(f"strIngredient{ingredient}")
                ingredients += ","
                ingredient +=1
                
                
        #create object coctel
        b = Coctel(id,name,tag,alcohol,instructions,imagen,ingredients)
        
        return b
    
class DataBase(GetDB.GETDB):
    def __init__(self,file):
        self.conexion = sqlite3.connect(file)
        self.cursor = self.conexion.cursor()
        
    def SaveCoctel(self,debida):
        self.cursor.execute("INSERT INTO COCTELES_PREFERIDOS VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(bebida.id,bebida.name,bebida.tag,bebida.alcohol.bebida.instructions,bebida.imagen,bebida.ingredients))
        self.conexion.commit()
        return (f"EL registro se guardo con exito")
    
    def ShowCoctel(self):
        showcoc = self.cursor.execute("SELECT * from COCTELES_PREFERIDOS").fetchall()
        
        cocteles = []
        i=0
        for b in showcoc:
            cocteles.append(bebida(b[0],b[1],b[2],b[3],b[4],b[5],b[6]))
            i+=1
        
        return cocteles
    
    def DeleteCoctel(self,name):
        self.cursor.execute("DELETE DROM COCTELES_PREFERIDOS WHERE name = ?",(name,))
        self.conexion.commit()
        
    def UpdateCoctel(self,name):
        self.cursor.execute("UPDATE COCTELES_PREFERIDOS WHERE nombre = ?",(nombre))
        self.conexion.commit()
        
        return (f"El coctel: {name} fue actualizado")

if name __name__ == '__main__':
    db = DB()
        
    
            
        