"""
Create a group of classes that represents information about music artists, 
their albums, and the tracks on those albums.  

Each class should contain the following information:
    Artist:  name, released albums
    Album: name, artist, tracks
    Track: number, name, length (seconds), artists

Demonstrate ways to navigate the relationships between the classes.
List every track from every album published for an artist.
List the album, number of tracks, and the total run time of the album for each artist.


"""
#Artist class - init method only takes as input the name parameter, creates an empty albums list
class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

#Album class - init method takes as input the name and artist parameters, creates an empty tracks list
class Album:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.tracks = []
#Track  class -  - init method takes as input the number, name and length parameters, creates an empty artists list
class Track:
    def __init__(self, number, name, length):
        self.number = number
        self.name = name
        self.length = length
        self.artists = []

#instantiating two Artist objects
artist_one = Artist("Artist One")
artist_two = Artist("Artist Two")

#instantiating an Album object, album_one
album_one = Album("First Opus", artist_one)

#adding album_one to the list of albums by artist_one
artist_one.albums.append(album_one)

#adding a track to the list of tracks in album_one
album_one.tracks.append(
    Track(1, "Cool Birds", 245)
    )
#adding a track to the list of tracks in album_one
album_one.tracks.append(
    Track(2, "Warm Giraffes", 270)
    )

#instantiating an Album object, album_two
album_two = Album("Second Concerto", artist_two)

#adding album_two to the list of albums by artist_two
artist_two.albums.append(album_two)

#adding a track to the list of tracks in album_two
album_two.tracks.append(
    Track(1, "Flying Flute", 180)
    )

#Repeat process of creating an album, adding it to eh artist, and then adding tracks to the album
album_three = Album("Second Opus", artist_one)

artist_one.albums.append(album_three)

album_three.tracks.append(
    Track(1, "Towering Oaks", 150)
    )

album_three.tracks.append(
    Track(2, "Lofty Cedars", 138)
    )

# List every track from every album published for an artist.
print("Track List")
for artist in [artist_one, artist_two]:
    print(f"{artist.name}")
    for album in artist.albums:
        for track in album.tracks:
            print(f"\t{track.name}")


print("\n\n")    

# List the album, number of tracks, and the total run time of the album for each artist
print("Album Details")
album_list = []
for artist in [artist_one, artist_two]:
    print(f"{artist.name}")
    for album in artist.albums:
        print(f"\tAlbum: {album.name} Tracks: {len(album.tracks)} Total Run Time: {sum([x.length for x in album.tracks])}")
