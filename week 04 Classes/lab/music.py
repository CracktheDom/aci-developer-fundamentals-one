import uuid


class Artist:
    """
    Represents an Artist entity.

    Attributes:
        name (str): The name of the artist.
        albums (dict): A dict of albums associated with the artist.
        artist_id (uuid.UUID): Unique identifier for the artist.
    """

    def __init__(self, name: str):
        """
        Initializes an Artist object.

        Args:
            name (str): The name of the artist.
        """
        self.artist_name: str = name
        self.albums: dict = dict()

        # Generate a unique ID for the artist
        self.artist_id: uuid.UUID = uuid.uuid4()

    def add_album(self, Album) -> None:
        """
        Adds an album to the artist's collection.

        Args:
            Album: The album object to be added.
        """
        self.albums[Album.album_name] = Album

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
        artist_id: uuid.UUID,
        # artist: Artist,
        track_list: list = [],
    ):
        """
        Initializes an Album object.

        Args:
            name (str): The name of the album.
            artist_id (uuid.UUID): Unique identifier for the artist associated with the album.
            track_list (list): The list that contains Track objects associated with album
        """
        self.album_name: str = name
        self.artist_id: uuid.UUID = artist_id
        self.album_id: uuid.UUID = uuid.uuid4()  # Generate a unique ID for the album
        self.track_list: list = list()

    def __str__(self) -> str:
        """
        String representation of the Album object.

        Returns:
            str: String representation of the Album object.
        """
        return f"This is an Album object: {self.album_name}"

    def add_track(self, Track) -> None:
        """
        Adds a track to the album's collection.

        Args:
            track: The Track object to be added.
        """
        Track.album_id = self.album_id
        self.track_list.append(Track)


class Track:
    """
    Represents a Track entity.

    Attributes:
        number (int): The track number.
        album_id (uuid.UUID): Unique identifier for the album associated with the track.
        name (str): The name of the track.
        duration (int): The duration of the track in seconds.
    """

    def __init__(
        self,
        number: int,
        name: str,
        duration: int,
        # album_id: uuid.UUID
    ):
        """
        Initializes a Track object.

        Args:
            number (int): The track number.
            name (str): The name of the track.
            duration (int): The duration of the track in seconds.
            album_id (uuid.UUID): Unique identifier for the album associated with the track.
        """
        self.number: int = number
        self.album_id: uuid.UUID = ""
        self.track_name: str = name
        self.duration: int = duration

    def __str__(self) -> str:
        """
        String representation of the Track object.

        Returns:
            str: String representation of the Track object.
        """
        return f"This is a Track object: {self.track_name}"


def main() -> None:
    """
    Main function to create Artist, Album, and Track objects and print album tracks.

    This function demonstrates the creation of Artist, Album, and Track objects
    and their association. It then prints the tracks of each album associated
    with the Artist.
    """

    # Create new Artist object
    men_i_trust: Artist = Artist(name="Men I Trust")

    # Create new Album objects
    untourable_album: Album = Album(
        name="Untourable Album",
        artist_id=men_i_trust.artist_id
        # artist=men_i_trust,
    )

    oncle_jazz = Album(artist_id=men_i_trust.artist_id, name="Oncle Jazz")

    untourable_album.add_track(
        Track(
            1,
            "Organon",
            2 * SECONDS_PER_MINUTE + 30,
            # album_id=untourable_album.album_id,
        )
    )

    # Use Artist method to album to list of albums in Artist object
    men_i_trust.add_album(oncle_jazz)

    # Create new Track objects and append them to Album object
    untourable_album.add_track(
        Track(
            4,
            "Sorbitol",
            2 * SECONDS_PER_MINUTE + 58,
            # album_id=untourable_album.album_id,
        )
    )
    untourable_album.add_track(
        Track(
            5,
            "Tree Among Shrubs",
            3 * SECONDS_PER_MINUTE + 8,
            # album_id=untourable_album.album_id,
        )
    )
    untourable_album.add_track(
        Track(
            3,
            "Sugar",
            2 * SECONDS_PER_MINUTE + 56,
            # album_id=untourable_album.album_id
        )
    )
    untourable_album.add_track(
        Track(
            2,
            "Oh Dove",
            3 * SECONDS_PER_MINUTE + 16,
            # album_id=untourable_album.album_id,
        )
    )

    # Add Album object to Artist object's list of albums
    men_i_trust.add_album(untourable_album)

    # Create new Track objects and append them to Album object
    men_i_trust.albums.get("Oncle Jazz").add_track(
        Track(
            name="Oncle Jazz",
            duration=57,
            number=1,
            # album_id=men_i_trust.albums.get("Oncle Jazz").album_id,
        )
    )
    men_i_trust.albums.get("Oncle Jazz").add_track(
        Track(
            3,
            "Days Go By",
            3 * SECONDS_PER_MINUTE + 26,
            # album_id=men_i_trust.albums.get("Oncle Jazz").album_id,
        )
    )
    men_i_trust.albums.get("Oncle Jazz").add_track(
        Track(
            15,
            "Show Me How",
            3 * SECONDS_PER_MINUTE + 35,
            # album_id=men_i_trust.albums.get("Oncle Jazz").album_id,
        )
    )
    men_i_trust.albums.get("Oncle Jazz").add_track(
        Track(
            17,
            "You Deserve This",
            3 * SECONDS_PER_MINUTE + 5,
            # album_id=men_i_trust.albums.get("Oncle Jazz").album_id,
        )
    )

    # Print the tracks of each album associated with the Artist
    print_album_tracks(men_i_trust)


def print_album_tracks(artist: Artist) -> str:
    """
    Print the tracks of each album associated with the given artist.

    Args:
        artist (Artist): The artist whose albums' tracks are to be printed.
    """
    if len(artist.albums) > 0:
        print(f"Artist name: {artist.artist_name}")
        for v in artist.albums.values():
            print(f"  Album: {v.album_name}")
            print("    Tracks:")

            album_duration = 0  # Track duration of album

            # Sort tracks by track number
            for album_track in sorted(v.track_list, key=lambda track: track.number):
                album_duration += album_track.duration
                print(f"      {album_track.number:2d}: {album_track.track_name}")

            # Calculate and print total runtime of the album
            print(f"  Total runtime is {album_duration} seconds\n")
    else:
        # If no albums are associated with the artist
        print(f"No albums associated with the artist, {artist.name}")


# {"Oncle Jazz": Album(name, artist_id), "untourable album": Album(name, artist_id)}


# Constant variable
SECONDS_PER_MINUTE: int = 60

if __name__ == "__main__":
    main()
