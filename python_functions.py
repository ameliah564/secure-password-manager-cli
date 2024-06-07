import psycopg2
from config import load_config

#python functions for INSERT
def insert_record(given_url, given_username, given_password):

    table_query = '''
    INSERT INTO vault (URL, username, password)
    VALUES (%s, %s, %s);
    '''
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(table_query, (given_url, given_username, given_password))
                conn.commit()
                print("Inserted record.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

#python function for UPDATE
def update_record(given_url, given_username, given_password):

    table_query = '''
    UPDATE vault
    SET username = %s, password = %s
    WHERE url = %s;
    '''
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(table_query, (given_username, given_password, given_url))
                conn.commit()
                print("Updated record.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
#python function for DELETE
def delete_record(given_url):

    table_query = '''
    DELETE FROM vault
    WHERE url = %s;
    '''
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(table_query, (given_url))
                conn.commit()
                print("Deleted record.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    
def list_records():
    table_query = '''
    SELECT * FROM vault;
    '''
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:                
                cur.execute(table_query)
                # fetch all rows from the result
                rows = cur.fetchall()
                # print each row
                for row in rows:
                    print(row)
                if not rows:
                    print("There are no records stored.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
        
def get_record(given_url):
    table_query = '''
    SELECT * FROM vault
    WHERE url = %s;
    '''
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(table_query, (given_url,))
                record = cur.fetchone()
                print(record)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


    
    