"""
This loop returns the key and values of a given dictionary
"""


SongAttributes = {"Song_title":"Childs Play", "Artist":"Drake", "Genre":"pop", "Speechiness":0.156, "Loudness":-11.204, "Acousticness":0.0145, "Tempo":80.03, "Danceability":1, "Valence":0.308, 
"LengthInSeconds":241400,  "Popularity":"medium"}

for key,value in SongAttributes.items():
	print(key,value)


def DictCheck(key,value):
	if key in SongAttributes:
		if SongAttributes[key] == value:
			return True
		else:
			return False
	else:
		return False


		

DictCheck("Artist","Drake")