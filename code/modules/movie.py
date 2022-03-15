class Movie:
    def __init__(self, description, year, duration, id = None):
        self.description = description
        self.year = year
        self.duration = duration
        self.id = id



# why does init ( ends with , after id = None) ?