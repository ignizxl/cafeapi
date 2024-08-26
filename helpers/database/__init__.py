import psycopg2
import psycopg2.extras
from Globals import *
def get_db_connection():
    """Cria uma conexão com o banco de dados PostgreSQL."""
    conn = None
    try:
        conn = psycopg2.connect(database=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD, 
                                host=DATABASE_HOST, port=DATABASE_PORT)
        conn.cursor_factory = psycopg2.extras.DictCursor
    except psycopg2.Error as e:
        print(f'Não foi possível conectar ao banco de dados: {e}')
    return conn