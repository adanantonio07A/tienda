import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(
        host='127.0.0.1',       # o 'localhost'
        user='tiendauser',           # Tu usuario real
        password='tiendapass',       # Tu contraseña real
        database='tienda_db',   # La base de datos que creaste
        port=3306               # Puerto por defecto de MySQL
    )
    print("✅ Conexión exitosa a MySQL")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("❌ Usuario o contraseña incorrectos")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("❌ La base de datos no existe")
    else:
        print(f"❌ Otro error: {err}")
else:
    cnx.close()

"""
import mysql.connector

try:
    print("🔌 Probando conexión directa...")
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="e3m7d$e!p",
        password="drg#a!aa@sa1a4rr",
        database="emdep_government3",
        port="3306"
    )

    print("✅ Conexión directa exitosa")
    conn.close()
except Exception as e:
    print("❌ Error en conexión directa:")
    print(e)
"""