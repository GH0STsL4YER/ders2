#music album

class Artist():
    "bu sinif artistin sarkilarini yukler"
    def __init__(self, name, date, genre):
        self.name = name
        self.date = date
        self.genre = genre

    def show_info(self):
        print(self.name, self.date, self.genre) 

class Song(Artist):
    def __init__(self, name, date, genre):
        super().__init__(name, date, genre)

s1=Song("Trapp queen", 2017, "pop")  
s2=Song("bir sonraki haytima gel", 2020, "pop")
s3=Song("Tacata", 2023, "brazilien phonk")      
s1.show_info()

class Likes():
    "bu sinif en cok like alan sarkilari onerir"
    def __init__(self, likes, name, artist):
        self.likes = likes
        self.name = name
        self.artist = artist

class List(Likes):
    def __init__(self, likes, name, artist):
        super().__init__(likes, name, artist)
