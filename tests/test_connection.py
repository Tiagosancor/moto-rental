import pymysql

# Configurações de conexão
config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Ti040506",
    "database": "moto_rental_db",
    "port": 3306
}

# Teste de conexão
try:
    # Cria a conexão
    connection = pymysql.connect(**config)
    
    # Abre um cursor para executar comandos SQL
    with connection.cursor() as cursor:
        # Executa uma consulta simples
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        
        # Verifica se o resultado é válido e exibe
        if result:
            print("Conexão bem-sucedida, resultado da consulta:", result[0])
        else:
            print("A consulta não retornou nenhum resultado.")
    
    # Fecha a conexão
    connection.close()

except pymysql.MySQLError as e:
    print("Erro ao conectar ao banco de dados:", e)
