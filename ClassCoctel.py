class coctel():
    def __init__(self,id,name,tag,alcohol,instructions,imagen,ingredients):
        self.id=id
        self.name=name
        self.tag=tag
        self.alcohol=alcohol
        self.instructions=instructions
        self.imagen=imagen
        self.ingredients=ingredients
        
    def __str__(self):
        if self.tag !=None:
            #el dato depende del coctel
            return str(f"Coctels:"+"\n"+f"Name -> {self.name}"+"\n"+f"Tag -> {self.tag}"+"\n"+f"Alcohol -> {self.alcohol}"+"\n"+f"Instructions -> {self.instructions}"+"\n"+f"Imagen -> {self.imagen}"+"\n"+f"Ingredients -> {self.ingredients}")
        else:
            return str(f"Coctels:"+"\n"+f"Name -> {self.name}"+"\n"+f"Alcohol -> {self.alcohol}"+"\n"+f"Instructions -> {self.instructions}"+"\n"+f"Imagen -> {self.imagen}"+"\n"+f"Ingredients -> {self.ingredients}")
    
    def __eq__(self,coctel2):
        if coctel2.id != self.id:
            return False
        if coctel2.name != self.name:
            return False
        if coctel2.tag != self.tag:
            return False
        if coctel2.alcohol != self.alcohol:
            return False
        if coctel2.instructions != self.instructions:
            return False
        if coctel2.imagen != self.imagen:
            return False
        if coctel2.ingredients != self.ingredients:
            return False
        return True
    
    