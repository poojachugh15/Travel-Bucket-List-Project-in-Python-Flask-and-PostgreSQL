class Sight:
    
    def __init__(self, name, city, country, visited = False, id = None):
        self.name = name
        self.city = city
        self.country = country
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True