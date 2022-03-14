# repositories/crew_repository.py

from db.run_sql import run_sql
from models.crew import *
  
def select_all():  
    Crew = [] # ADDED - in case we get `None` back from run_sql

    sql = "SELECT * FROM crew"
    results = run_sql(sql)

    for row in results:
        Crew = Crew(row['description'], row['year'], row['duration'], row['completed'], row['id'] )
        Crew.append(Crew)
    return Crew 

# The function called `select_all` in our `crew_repository` to get all the rows in the `crew` table in the database and return a list of crew objects. 
# The SQL will be a `SELECT` clause. Since we are simply getting all the rows in the table, we do not need to pass any values into the `run_sql` function, 
# but we do want to get the rows the function returns.

# The `run_sql` function returns a list of dictionary-like objects, but we really want a list of crew objects back. 
# To get this we need to loop through the list of results, getting the information for each crew from the dictionary 
# like object, and then creating a list of crew objects.