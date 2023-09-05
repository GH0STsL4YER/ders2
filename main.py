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
s2.show_info()
s3.show_info()
print("-------------------------------")
class Views():
    "bu sinif en cok like alan sarkilari onerir"
    def __init__(self, views, name, artist):
        self.views = views
        self.name = name
        self.artist = artist

    def show_info(self):
        print(self.views, self.name, self.artist)

class List(Views):
    def __init__(self, views, name, artist):
        super().__init__(views, name, artist)

Top1 = List( "8.1billion", "Despacito", "Luis Fonsi ft. Daddy Yankee" )
Top2 = List(  "5.9billion", "Shape of You", "Ed Sheeran")
Top3 = List(  "4.8billion", "Uptown Funk", "Mark Ronson ft. Bruno Mars")
Top1.show_info()
Top2.show_info()
Top3.show_info()
