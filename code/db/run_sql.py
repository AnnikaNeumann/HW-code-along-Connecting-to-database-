from unittest import result
import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    
    try:
        conn=psycopg2.connect("dbname = 'star_trek'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
# Finally, we need to close our cursor(`cur`) otherwise it will continue to keep hold of resources on the database until the connection is finally closed.
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
    return results

#### Getting the results
# When we run our SQL to get the items from the database we want to access the results to see what we can back. 
# To do this we call the `fetchall` method on our `cursor`:      

# This gets all the rows returned from running the query. This is normally returned as a list of tuples, but as we are using `DictCursor` 
# we get a list of dictionary-like items back.

# We will return this list at the end of the function, but just in case an exception is raised we will set `results` t
# o be an empty list at the start of the function.

        

        
