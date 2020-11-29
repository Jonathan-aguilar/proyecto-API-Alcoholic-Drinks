import sqlite3

def main():
    conexion = sqlite3.connect("Database.db")
    cursor = conexion.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS COCTELES_PREFERIDOS
    (id Number,
    name Text,
    tag Text,
    alcohol Text,
    instructions Text,
    imagen Text,
    ingredients Text)''')
    conexion.commit()
    
    cursor.execute('''CREATE TABLE IF NOT EXITS COCTELES 
    (id Number,
    name Text,
    tag Text,
    alcohol Text,
    instructions Text,
    ingredients Text)''')
    
    conexion.commit()
    conexion.close()

if __name__ == '__main__':
    main()