class Crew:
    def __init__(self, description, year, duration, completed = False, id = None),:
        self.description = description
        self.year = year
        self.duration = duration
        self.completed = completed
        self.id = id

    def mark_complete(self):
        self.completed = True


# why does init ( ends with , after id = None) ?