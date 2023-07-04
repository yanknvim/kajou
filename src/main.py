import fire

from mutagen.easyid3 import EasyID3

import os
import random


def add_song(path, playlist):
    """Add music file at the path to the playlist."""
    with open(playlist, "a") as f:
        try:
            f.write(path + "\n")
        except Exception as e:
            print(e)


def insert_song(path, index, playlist):
    """Insert music file at path to the playlist which is specifed by the index."""
    with open(playlist, "r+") as f:
        try:
            songs = f.readlines()
            songs.insert(index - 1, path)

            f.seek(0)
            f.truncate()

            f.writelines(songs)
        except Exception as e:
            print(e)


def list_song(playlist):
    """List tracks in the playlist."""
    with open(playlist, "r") as f:
        try:
            for i, path in enumerate(f.readlines()):
                song_index = "{} | ".format(str(i + 1).rjust(3))
                try:
                    tags = EasyID3(path.strip())
                    description = "{0} - {1}".format(
                        tags["artist"][0], tags["title"][0]
                    )
                    print(song_index, description)
                except:
                    filename = os.path.splitext(os.path.basename(path))[0]
                    print(song_index, filename)

        except Exception as e:
            print(e)


def remove_song(index, playlist):
    """Remove specified track from playlist by the index."""
    with open(playlist, "r+") as f:
        try:
            songs = f.readlines()
            songs.pop(index - 1)

            f.seek(0)
            f.truncate()

            f.writelines(songs)
        except Exception as f:
            print(f)


def sort_song(playlist):
    """Sort and delete duplicated tracks in the playlist."""
    with open(playlist, "r+") as f:
        try:
            songs = f.readlines()
            songs = sorted(list(set(songs)))

            f.seek(0)
            f.truncate()

            f.writelines(songs)
        except Exception as e:
            print(e)


def shuffle_song(playlist):
    """Shuffle tracks in the playlist."""
    with open(playlist, "r+") as f:
        try:
            songs = f.readlines()
            random.shuffle(songs)

            f.seek(0)
            f.truncate()

            f.writelines(songs)
        except Exception as e:
            print(e)


def main():
    fire.Fire(
        {
            "add": add_song,
            "insert": insert_song,
            "list": list_song,
            "remove": remove_song,
            "sort": sort_song,
            "shuffle": shuffle_song,
        }
    )

