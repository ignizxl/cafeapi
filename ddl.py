import psycopg2
from Globals import *

def initialize_database():
    """Cria e inicializa o banco de dados usando o script SQL fornecido."""
    try:
        # Conectando ao banco de dados PostgreSQL
        connection = psycopg2.connect(database=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD, 
                                host=DATABASE_HOST, port=DATABASE_PORT)
        connection.autocommit = True  # Permite a execução do comando de criação do banco de dados
        
        # Abrir e executar o script SQL
        with open('schema.sql', 'r') as file:
            script = file.read()
        
        with connection.cursor() as cursor:
            cursor.execute(script)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    initialize_database()