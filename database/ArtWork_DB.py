import sqlite3
from exceptions.artwork_error import ArtworkError
from model.Art_Model import Artwork
from model.Art_Model import Artist
from exceptions.artwork_error import ArtworkError

db_artist = 'artStore.db'


class SQLArtworkDB():
    def __init__(self):

        with sqlite3.connect(db_artist) as con:
            con.execute('CREATE TABLE IF NOT EXISTS ARTIST (artistsName TEXT NOT NULL, email TEXT NOT NULL)')
        with sqlite3.connect(db_artist) as con:
            con.execute(
                'CREATE TABLE IF NOT EXISTS ARTWORK (artistName TEXT NOT NULL, name TEXT UNIQUE NOT NULL, price FLOAT, available INTEGER, FOREIGN KEY(artistName) REFERENCES ARTIST(artistsName))')

    #initializes db, creates both tables if not existing already
    def insert_artist(self, artist):


        try:
            with sqlite3.connect(db_artist) as con:
                rows_mod = con.execute('INSERT INTO ARTIST VALUES (?, ?)', (artist.name, artist.email))
            con.close()
            return rows_mod
        except sqlite3.IntegrityError as ie:
            raise ArtworkError(f'Cannot add a duplicate artist, {artist.name} already exists ')
    #inserting artist in to db, recieves artist object from view_model which is passed from view, returns rows modified
    #to verify if artist has been added, if a duplicate artist is added it is not added and error message is passed
    def insert_artwork(self, artwork):
        try:
            with sqlite3.connect(db_artist) as con:
                rows_mod = con.execute('INSERT INTO ARTWORK VALUES (?, ?, ?, ?)',
                                       (artwork.artist, artwork.name, artwork.price, artwork.available))
            con.close()
            return rows_mod
        except sqlite3.IntegrityError as ie:
            raise ArtworkError(f'Cannot add a duplicate piece of artwork, {artwork.name} already exists ')

    #method to insert artwork, recieves artwork object from view model which is passed from view
    #returns rows mod to verify artwork is added, if duplicate art piece is added it is not added and error message is passed

    def search_all_artwork(self, artist):
        con = sqlite3.connect(db_artist)
        artwork_cursor = con.execute('SELECT * FROM ARTWORK where artistName = ?', (artist,))
        artworks = [ Artwork(*row) for row in artwork_cursor.fetchall() ]
        con.close()
        return artworks
    #searching for all artwork from a particular artist
    def search_available_artwork(self, artist):
        con = sqlite3.connect(db_artist)
        artwork_cursor = con.execute('SELECT * FROM ARTWORK WHERE artistName like ? and available = 1', (artist,))
        artworks = [ Artwork(*row) for row in artwork_cursor.fetchall() ]
        con.close()
        return artworks
    #serching for all artwork from a particular artist that is available (stored as 1 in available field)

    def delete_artwork(self, artwork):
        con = sqlite3.connect(db_artist)
        cursor = con.execute('DELETE FROM ARTWORK WHERE name = ?', (artwork,))
        con.commit()
        con.close()
        if cursor.rowcount > 0:
            return True
        else:
            return False

    #deleting artwork by name, returns true of artwork is deleted, false if not
    def change_status(self, artwork, available):

        con = sqlite3.connect(db_artist)
        cursor = con.execute('UPDATE ARTWORK set available = ? where name = ?', (available, artwork))
        con.commit()
        con.close()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    #changes artwork available status, takes artwork name and the status wished to be changed
