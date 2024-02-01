#!/usr/bin/env python3

from music import *


def test_artist_init():
    assert isinstance(artist, Artist)


def test_artist_name_exists():
    assert artist.name is not None


def test_artist_name_type():
    assert isinstance(artist.name, str)


def test_artist_albums_exists():
    assert artist.albums is not None


def test_artist_albums_type():
    assert isinstance(artist.albums, list)


def test_artist_artist_id_exists():
    assert artist.artist_id is not None


def test_artist_artist_id_type():
    assert isinstance(artist.artist_id, uuid.UUID)


def test_artist_albums_length():
    assert len(artist.albums) > 0


def test_artist_albums_elem_type():
    for album in artist.albums:
        assert isinstance(album, Album)


def test_album_init():
    assert isinstance(album, Album)


def test_album_name_exists():
    assert album.name is not None


def test_album_name_type():
    assert isinstance(album.name, str)


def test_album_artist_id_exists():
    assert album.artist_id is not None


def test_album_artist_type():
    assert isinstance(album.artist_id, uuid.UUID)


def test_album_tracks_exists():
    assert album.tracks is not None


def test_album_tracks_type():
    assert isinstance(album.tracks, list)


def test_albums_tracks_length():
    assert len(album.tracks) > 0


def test_track_exists():
    assert track is not None


def test_track_type():
    assert isinstance(track, Track)


def test_track_number_exists():
    assert track.number is not None


def test_track_number_type():
    assert isinstance(track.number, int)


def test_track_name_exists():
    assert track.name is not None


def test_track_name_type():
    assert isinstance(track.name, str)


def test_track_length_exists():
    assert track.length is not None


def test_track_length_type():
    assert isinstance(track.length, int)


def test_album_tracks_elem_type():
    for track in album.tracks:
        assert isinstance(track, Track)


def test_artist_function__str__output():
    assert artist.__str__() == f"This is an Artist object: {artist.name}"


def test_album_function__str__output():
    assert album.__str__() == f"This is an Album object: {album.name}"


def test_track_function__str__output():
    assert track.__str__() == f"This is a Track object: {track.name}"


def test_seconds_per_minute_exists():
    assert SECONDS_PER_MINUTE is not None


def test_seconds_per_minute_type():
    assert isinstance(SECONDS_PER_MINUTE, int)


def test_seconds_per_minute_equals():
    assert SECONDS_PER_MINUTE == 60


artist = Artist("Black Pumas")

album = Album("Black Pumas", artist_id=artist.artist_id)
track = Track(name="Black Moon Rising", length=222, number=1)
album.tracks.append(track)

album.tracks.append(
    Track(
        # minutes * seconds/minute + remaining seconds
        length=4 * SECONDS_PER_MINUTE + 6,
        number=4,
        name="Fire",
    )
)

album.tracks.append(Track(2, "Colors", 4 * SECONDS_PER_MINUTE + 6))
album.tracks.append(Track(3, "Know Better", 4 * SECONDS_PER_MINUTE + 9))
artist.add_album(album)


if __name__ == "__main__":
    ...
