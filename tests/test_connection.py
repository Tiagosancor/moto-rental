import pymysql


config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Ti040506",
    "database": "moto_rental_db",
    "port": 3306
}


try:
    
    connection = pymysql.connect(**config)
    

    with connection.cursor() as cursor:
        
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        
        
        if result:
            print("Conexão bem-sucedida, resultado da consulta:", result[0])
        else:
            print("A consulta não retornou nenhum resultado.")
    
    
    connection.close()

except pymysql.MySQLError as e:
    print("Erro ao conectar ao banco de dados:", e)
