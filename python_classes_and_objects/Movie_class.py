class Movie:
    def display(self,hero,heroine,rating):
        self.hero = hero
        self.heroine =  heroine
        self.rating = rating
    def show(self):
        print("Hero Name: ",self.hero)
        print("Heroine Name: ",self.heroine)
        print("Rating: ",self.rating)
m1 = Movie()
m2 = Movie()
m1.display("Dulquer","PujaHegde",4.8)
m2.display("Tonvio","kayadu",4.5)
m1.show()
m2.show()