import pdb 
from modules.movie import Movie
import repositories.movie_repository as movie_repository  

result = movie_repository.select_all()

for crew in result:
    print(crew.__dict__)

pdb.set_trace()