class Movie:
    def __init__(self, movie_name, hero, heroine, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating

    def display(self):
        print("Movie:", self.movie_name)
        print("Hero:", self.hero)
        print("Heroine:", self.heroine)
        print("Rating:", self.rating)

movie = Movie("Example Movie", "Hero", "Heroine", 8.5)
movie.display()
