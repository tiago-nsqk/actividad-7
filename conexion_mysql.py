"""Actividad 7 - Parte 3: MySQL desde Python.

Crea la base `actividad7` con las tablas `automovil`, `paciente` y `producto`,
inserta registros, hace consultas y carga el resultado en un DataFrame de pandas.
"""
import os

import mysql.connector
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# 1. Conexión (las credenciales vienen del archivo .env)
db = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
)
# 2. Cursor
cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS actividad7")
cursor.execute("USE actividad7")

# Tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS automovil (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(10) NOT NULL,
    marca VARCHAR(50),
    modelo INT
)""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS paciente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT,
    fecha_cita DATE
)""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2),
    stock INT,
    activo BOOLEAN DEFAULT TRUE
)""")

# 3. Inserción
cursor.executemany(
    "INSERT INTO producto (nombre, precio, stock) VALUES (%s, %s, %s)",
    [("Teclado", 49.90, 30), ("Mouse", 19.90, 80), ("Monitor", 189.00, 12)],
)
db.commit()

# Consulta con filtro
cursor.execute("SELECT * FROM producto WHERE precio > %s", (20,))
print(cursor.fetchall())

# Modificación
cursor.execute("UPDATE producto SET stock = stock - 1 WHERE nombre = %s", ("Mouse",))

# Eliminación
cursor.execute("DELETE FROM producto WHERE nombre = %s", ("Monitor",))
db.commit()

# Resultado en DataFrame de pandas
cursor.execute("SELECT * FROM producto")
columnas = [c[0] for c in cursor.description]
df = pd.DataFrame(cursor.fetchall(), columns=columnas)
print(df)

# 4. Cierre
cursor.close()
db.close()
