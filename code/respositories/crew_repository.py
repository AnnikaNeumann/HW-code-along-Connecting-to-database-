from db.run_sql import run_sql

from models.crew import Crew
  
def select_all():  
    Crew = [] 

    sql = "SELECT * FROM crew"
    results = run_sql(sql)

    for row in results:
        Crew = Crew(row['description'], row['year'], row['duration'], row['completed'], row['id'] )
        Crew.append(Crew)
    return Crew 

