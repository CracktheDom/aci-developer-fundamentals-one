import uuid


class Artist:
    """
    Represents an Artist entity.

    Attributes:
        name (str): The name of the artist.
        albums (list): A list of albums associated with the artist.
        artist_id (uuid.UUID): Unique identifier for the artist.
    """

    def __init__(self, name: str):
        """
        Initializes an Artist object.

        Args:
            name (str): The name of the artist.
        """
        self.artist_name: str = name
        self.albums: list = list()
        self.artist_id: uuid.UUID = uuid.uuid4()  # Generate a unique ID for the artist

    def add_album(self, Album):
        """
        Adds an album to the artist's collection.

        Args:
            album: The album object to be added.
        """
        self.albums.append(Album)

    def __str__(self) -> str:
        """
        String representation of the Artist object.

        Returns:
            str: String representation of the Artist object.
        """
        return f"This is an Artist object: {self.artist_name}"


class Album:
    """
    Represents an Album entity.

    Attributes:
        name (str): The name of the album.
        artist_id (uuid.UUID): Unique identifier for the artist associated with the album.
        album_id (uuid.UUID): Unique identifier for the album.
        tracks (list): A list of tracks associated with the album.
    """

    def __init__(
        self,
        name: str,
        # artist_id: uuid.UUID
        artist: Artist,
        tracks: list = [],
    ):
        """
        Initializes an Album object.

        Args:
            name (str): The name of the album.
            artist_id (uuid.UUID): Unique identifier for the artist associated with the album.
        """
        self.album_name: str = name
        self.artist = artist
        # self.artist_id: uuid.UUID = artist_id
        self.album_id: uuid.UUID = uuid.uuid4()  # Generate a unique ID for the album
        self.tracks: list = tracks

    def __str__(self) -> str:
        """
        String representation of the Album object.

        Returns:
            str: String representation of the Album object.
        """
        return f"This is an Album object: {self.album_name}"

    def add_track(self, Track):
        """
        Adds a track to the album's collection.

        Args:
            track: The track object to be added.
        """
        self.tracks.append(Track)


class Track:
    """
    Represents a Track entity.

    Attributes:
        number (int): The track number.
        album_id (uuid.UUID): Unique identifier for the album associated with the track.
        name (str): The name of the track.
        length (int): The length of the track in seconds.
    """

    def __init__(self, number: int, name: str, length: int, album_id: uuid.UUID):
        """
        Initializes a Track object.

        Args:
            number (int): The track number.
            name (str): The name of the track.
            length (int): The length of the track in seconds.
            album_id (uuid.UUID): Unique identifier for the album associated with the track.
        """
        self.number: int = number
        self.album_id: uuid.UUID = album_id
        self.track_name: str = name
        self.length: int = length

    def __str__(self):
        """
        String representation of the Track object.

        Returns:
            str: String representation of the Track object.
        """
        return f"This is a Track object: {self.track_name}"


def main():
    """
    Main function to create Artist, Album, and Track objects and print album tracks.

    This function demonstrates the creation of Artist, Album, and Track objects
    and their association. It then prints the tracks of each album associated
    with the Artist.
    """

    # Create new Artist object
    men_i_trust = Artist(name="Men I Trust")

    # Create new Album objects
    untourable_album = Album(
        name="Untourable Album",
        # artist_id=men_i_trust.artist_id
        artist=men_i_trust,
    )

    # Use Artist method to album to list of albums in Artist object
    men_i_trust.add_album(
        Album(
            # artist_id=men_i_trust.artist_id,
            artist=men_i_trust,
            name="Oncle Jazz",
        )
    )

    # Create new Track objects and append them to Album object
    untourable_album.tracks.append(
        Track(
            4,
            "Sorbitol",
            2 * SECONDS_PER_MINUTE + 58,
            album_id=untourable_album.album_id,
        )
    )
    untourable_album.tracks.append(
        Track(
            1,
            "Organon",
            2 * SECONDS_PER_MINUTE + 30,
            album_id=untourable_album.album_id,
        )
    )
    untourable_album.tracks.append(
        Track(
            5,
            "Tree Among Shrubs",
            3 * SECONDS_PER_MINUTE + 8,
            album_id=untourable_album.album_id,
        )
    )
    untourable_album.tracks.append(
        Track(
            3, "Sugar", 2 * SECONDS_PER_MINUTE + 56, album_id=untourable_album.album_id
        )
    )
    untourable_album.tracks.append(
        Track(
            2,
            "Oh Dove",
            3 * SECONDS_PER_MINUTE + 16,
            album_id=untourable_album.album_id,
        )
    )

    # Add Album object to Artist object's list of albums
    men_i_trust.albums.append(untourable_album)

    # Create new Track objects and append them to Album object
    men_i_trust.albums[0].add_track(
        Track(
            name="Oncle Jazz",
            length=57,
            number=1,
            album_id=men_i_trust.albums[0].album_id,
        )
    )
    men_i_trust.albums[0].add_track(
        Track(
            3,
            "Days Go By",
            3 * SECONDS_PER_MINUTE + 26,
            album_id=men_i_trust.albums[0].album_id,
        )
    )
    men_i_trust.albums[0].add_track(
        Track(
            15,
            "Show Me How",
            3 * SECONDS_PER_MINUTE + 35,
            album_id=men_i_trust.albums[0].album_id,
        )
    )
    men_i_trust.albums[0].add_track(
        Track(
            17,
            "You Deserve This",
            3 * SECONDS_PER_MINUTE + 5,
            album_id=men_i_trust.albums[0].album_id,
        )
    )

    # Add Album object to Artist object's list of albums
    # men_i_trust.albums.append(oncle_jazz)

    # Print the tracks of each album associated with the Artist
    print_album_tracks(men_i_trust)


def print_album_tracks(artist: Artist):
    """
    Print the tracks of each album associated with the given artist.

    Args:
        artist (Artist): The artist whose albums' tracks are to be printed.
    """
    if len(artist.albums) > 0:
        print(f"Artist name: {artist.artist_name}")
        for album in artist.albums:
            print(f"  Album: {album.album_name}")
            print("    Tracks:")
            # Sort tracks by track number
            for album_track in sorted(album.tracks, key=lambda track: track.number):
                print(f"      {album_track.number:2d}: {album_track.track_name}")

            # Calculate and print total runtime of the album
            print(
                f"  Total runtime is {sum([track.length for track in album.tracks])} seconds\n"
            )
    else:
        # If no albums are associated with the artist
        print(f"No albums associated with the artist, {artist.name}")


# Constant variable
SECONDS_PER_MINUTE = 60

if __name__ == "__main__":
    main()
