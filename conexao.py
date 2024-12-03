
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="87654321",
        database="meu_projeto"
    )
