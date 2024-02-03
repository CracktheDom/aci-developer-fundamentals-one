#!/usr/bin/env python3

from music import *


def test_artist_init():
    assert isinstance(artist, Artist)


def test_artist_name_exists():
    assert artist.artist_name is not None


def test_artist_name_type():
    assert isinstance(artist.artist_name, str)


def test_artist_albums_exists():
    assert artist.albums is not None


def test_artist_albums_type():
    assert isinstance(artist.albums, dict)


def test_artist_artist_id_exists():
    assert artist.artist_id is not None


def test_artist_artist_id_type():
    assert isinstance(artist.artist_id, uuid.UUID)


def test_artist_albums_duration():
    assert len(artist.albums) > 0


def test_artist_albums_elem_type():
    for _, album in artist.albums.items():
        assert isinstance(album, Album)


def test_album_init():
    assert isinstance(album, Album)


def test_album_name_exists():
    assert album.album_name is not None


def test_album_name_type():
    assert isinstance(album.album_name, str)


def test_album_artist_id_exists():
    assert album.artist_id is not None


def test_album_artist_type():
    assert isinstance(album.artist_id, uuid.UUID)


def test_album_tracks_exists():
    assert album.track_list is not None


def test_album_tracks_type():
    assert isinstance(album.track_list, list)


def test_albums_tracks_duration():
    assert len(album.track_list) > 0


def test_track_exists():
    assert track is not None


def test_track_type():
    assert isinstance(track, Track)


def test_track_number_exists():
    assert track.number is not None


def test_track_number_type():
    assert isinstance(track.number, int)


def test_track_name_exists():
    assert track.track_name is not None


def test_track_name_type():
    assert isinstance(track.track_name, str)


def test_track_duration_exists():
    assert track.duration is not None


def test_track_duration_type():
    assert isinstance(track.duration, int)


def test_album_tracks_elem_type():
    for track in album.track_list:
        assert isinstance(track, Track)


def test_artist__str__function__output():
    assert artist.__str__() == f"This is an Artist object: {artist.artist_name}"


def test_album__str__function_output():
    assert album.__str__() == f"This is an Album object: {album.album_name}"


def test_track__str__function_output():
    assert track.__str__() == f"This is a Track object: {track.track_name}"


def test_seconds_per_minute_exists():
    assert SECONDS_PER_MINUTE is not None


def test_seconds_per_minute_type():
    assert isinstance(SECONDS_PER_MINUTE, int)


def test_seconds_per_minute_equals():
    assert SECONDS_PER_MINUTE == 60


def test_artist_add_album():
    second_album = Album(name="Chronicles of a Diamond", artist_id=artist.artist_id)
    artist.add_album(second_album)
    assert second_album in artist.albums.values()


def test_album_add_track():
    another_track = Track(
        name="Oct 33",
        # album_id=album.album_id,
        number=5,
        duration=4 * SECONDS_PER_MINUTE + 49,
    )
    album.add_track(another_track)
    assert album.track_list[-1] is another_track


# set up data for tests
artist = Artist("Black Pumas")
album = Album(
    "Black Pumas",
    artist_id=artist.artist_id,
    # artist,
)
track = Track(
    # album_id=album.album_id,
    name="Black Moon Rising",
    duration=222,
    number=1,
)
album.add_track(track)
album.add_track(
    Track(
        # album_id=album.album_id,
        # minutes * 60 seconds/minute + remaining seconds
        duration=4 * SECONDS_PER_MINUTE + 6,
        number=4,
        name="Fire",
    )
)
album.add_track(
    Track(
        # album_id=album.album_id,
        number=2,
        name="Colors",
        duration=4 * SECONDS_PER_MINUTE + 6,
    )
)
album.add_track(
    Track(
        # album_id=album.album_id,
        number=3,
        name="Know Better",
        duration=4 * SECONDS_PER_MINUTE + 9,
    )
)
artist.add_album(album)


if __name__ == "__main__":
    ...
