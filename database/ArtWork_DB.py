import sqlite3
from exceptions.artwork_error import ArtworkError
from model.Art_Model import Artwork
from model.Art_Model import Artist
from exceptions.artwork_error import ArtworkError
db_artist = 'artStore.db'


class SQLArtworkDB():
    def __init__(self):
        with sqlite3.connect(db_artist) as con:
            con.execute(
                'CREATE TABLE IF NOT EXISTS ARTWORK (artistName TEXT NOT NULL, name TEXT UNIQUE NOT NULL, price FLOAT, available INTEGER)')
        with sqlite3.connect(db_artist) as con:
            con.execute('CREATE TABLE IF NOT EXISTS ARTIST (name TEXT PRIMARY KEY UNIQUE NOT NULL , email TEXT NOT NULL)')

    def insert_artist(self, artist):


        try:
            with sqlite3.connect(db_artist) as con:
                rows_mod = con.execute('INSERT INTO ARTIST VALUES (?, ?)', (artist.name, artist.email))
            con.close()
            return rows_mod
        except sqlite3.IntegrityError as ie:
            raise ArtworkError(f'Cannot add a duplicate artist, {artist.name} already exists ')

    def insert_artwork(self, artwork):
        try:
            with sqlite3.connect(db_artist) as con:
                rows_mod = con.execute('INSERT INTO ARTWORK VALUES (?, ?, ?, ?)',
                                       (artwork.artist, artwork.name, artwork.price, artwork.available))
            con.close()
            return rows_mod
        except sqlite3.IntegrityError as ie:
            raise ArtworkError(f'Cannot add a duplicate piece of artwork, {artwork.name} already exists ')


    def search_all_artwork(self, artist):
        con = sqlite3.connect(db_artist)
        artwork_cursor = con.execute('SELECT * FROM ARTWORK where artistName = ?', (artist,))
        artworks = [ Artwork(*row) for row in artwork_cursor.fetchall() ]
        con.close()
        return artworks

    def search_available_artwork(self, artist):
        con = sqlite3.connect(db_artist)
        artwork_cursor = con.execute('SELECT * FROM ARTWORK WHERE artistName like ? and available = 1', (artist,))
        artworks = [ Artwork(*row) for row in artwork_cursor.fetchall() ]
        con.close()
        return artworks

    def delete_artwork(self, artwork):
        print(artwork)
        con = sqlite3.connect(db_artist)
        rows_mod = con.execute('DELETE FROM ARTWORK WHERE name = ?', (artwork,))
        con.close()
        return rows_mod

    def change_status(self, artwork, available):

        con = sqlite3.connect(db_artist)
        rows_mod = con.execute('UPDATE ARTWORK set available = ? where name = ?', (available, artwork))
        con.close()
        return rows_mod
