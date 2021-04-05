import pdb
from models.country import Country
from models.city import City
from models.sight import Sight

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.sight_repository as sight_repository

city_repository.delete_all()
country_repository.delete_all()
sight_repository.delete_all()

country1 = Country("France", False)
country_repository.save(country1)
country2 = Country("Greece", False)
country_repository.save(country2)
country3 = Country("United Kingdom", True)
country_repository.save(country3)
country4 = Country("Switzerland", False)
country_repository.save(country4)
country5 = Country("America", True)
country_repository.save(country5)
country6 = Country("Australlia", False)
country_repository.save(country6)
country7 = Country("United Arab Emirates", True)
country_repository.save(country7)


city1 = City("Paris", country1, False)
city_repository.save(city1)
city2 = City("Santorini", country2, False)
city_repository.save(city2)
city3 = City("London", country3, True)
city_repository.save(city3)
city4 = City("Zurich", country4, False)
city_repository.save(city4)
city5 = City("Las Vegas", country5, True)
city_repository.save(city5)
city6 = City("Sydney", country6, False)
city_repository.save(city6)
city7 = City("Dubai", country7, True)
city_repository.save(city7)

sight1 = Sight("Eiffel Tower",city1, country1, False)
sight_repository.save(sight1)
sight2 = Sight("Amoudi Bay", city2, country2, False)
sight_repository.save(sight2)
sight3 = Sight("Town Bridge", city3, country3, False)
sight_repository.save(sight3)
sight4 = Sight("Lake Zurich", city4, country4, False)
sight_repository.save(sight4)
sight5 = Sight("Bellagio Fountains", city5, country5, False)
sight_repository.save(sight5)
sight6 = Sight("Sydney Opera House", city6, country6, False)
sight_repository.save(sight6)
sight7 = Sight("Burj Khalifa", city7, country7, True)
sight_repository.save(sight7)





pdb.set_trace()