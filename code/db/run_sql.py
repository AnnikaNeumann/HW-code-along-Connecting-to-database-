from os import curdir
import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    
    try:
        conn=psycopg2.connect("dbname = 'star_trek'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        cur.execute(sql, values)

        

        
