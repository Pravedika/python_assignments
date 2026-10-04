class Movie:
    def __init__(self, movie_name, hero, heroine, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating

movie_one = Movie("Movie One", "Hero One", "Heroine One", 8.5)
movie_two = Movie("Movie Two", "Hero Two", "Heroine Two", 9.0)

for movie in [movie_one, movie_two]:
    print(movie.movie_name, movie.hero, movie.heroine, movie.rating)
