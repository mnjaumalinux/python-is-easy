"""
These functions returns the various attributes of a song when called 
"""

Song_title = "Childs Play" # Describes the title of the song
Artist	= "Drake"
Genre	= "pop"
Speechiness = 0.156 # 
Loudness = -11.204 # The higher the value, the louder the song (in dB).
Acousticness = 0.0145 # The higher the value the more acoustic the song is.
Tempo = 80.03
Danceability = 1 #The higher the value, the easier it is to dance to this song.
Valence = 0.308 #The higher the value, the more positive mood for the song.
LengthInSeconds = 241400 #The duration of the song.
Popularity = "medium"


def SongTitle():
	return Song_title

def genre():
	return Genre	

def artist():
	return Artist
	
def tempo():
	return Tempo > 50

def loudness():
	return Loudness < -20

	
SongTitle()
genre()
artist()
tempo()
loudness()