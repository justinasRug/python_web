import io

class Song():
    def __init__(self, songName, genre, like, pic ):
        self.songName = songName
        self.genre = genre
        self.like = like
        self.pic = pic
        
    def printSongs(self):
        print("Song Title - " + str(self.songName) + "\nGenre - " + str(self.genre) + "\n" +str(self.like) +"\n" +str(self.pic) + "\n\n")
        
    def writeSongsToFile(self):
        with io.open("all_Songs.txt", "a", encoding="utf-8") as f:
             f.write("Song Title - " + str(self.songName) + "\nGenre - " + str(self.genre) + "\n" +str(self.like) +"\n\n")
             f.close()

 
class Artis():
    def __init__(self, fullName, bandName, position, age):
        self.fullName = fullName
        self.bandName = bandName
        self.position = position
        self.age = age 
       