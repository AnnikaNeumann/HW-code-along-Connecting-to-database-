import pdb 
from models.crew import *
import repositories.crew_repository as crew_repository  

result = crew_repository.select_all()

for crew in result:
    print(crew.__dict__)

pdb.set_trace()