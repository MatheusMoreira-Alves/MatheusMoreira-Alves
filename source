import psycopg2

# Define as informações de conexão com o banco de dados;
database_info = {
    'host': 'containers-us-west-141.railway.app',
    'port': '6610',
    'database': 'railway',
    'user': 'postgres',
    'password': '*'
}

# Cria a conexão com o banco de dados;
def connect():
    database = psycopg2.connect(**database_info)
    return database

try:
    database = connect()
    print("Connection successful!")

except Exception as e:
    print(f"Error connecting to database: {e}")
