import psycopg2
from config import load_config

def create_tables():

    create_table_query = '''CREATE TABLE Vault
    (URL TEXT PRIMARY KEY NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL);'''
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(create_table_query)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()