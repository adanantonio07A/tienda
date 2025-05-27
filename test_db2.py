import mysql.connector
try:
    cnxDB = mysql.connector.connect(user= 'tiendauser',
                                        password= 'tiendapass',
                                            host= '127.0.0.1',
                                        database= 'tienda_db',
                                        autocommit = True)
    cursor = cnxDB.cursor()    
    print("saliendo try")                                      
except Exception as e:
    print("FATAL ERROR IN DATABASE: ", e)