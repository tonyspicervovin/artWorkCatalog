import sqlite3
import unittest
from unittest import TestCase
from model.Art_Model import Artwork
from model.Art_Model import Artist
from database import ArtWork_DB
from exceptions.artwork_error import ArtworkError


class TestArtworkDB(TestCase):
    test_db_url = 'test_artwork.db'

    def setUp(self):
        ArtWork_DB.db_artist = self.test_db_url
        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('DROP TABLE IF EXISTS ARTIST')
            conn.execute('DROP TABLE IF EXISTS ARTWORK')
        conn.close()
        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('CREATE TABLE ARTIST (artistsName TEXT NOT NULL, email TEXT UNIQUE NOT NULL)')
            conn.execute('CREATE TABLE ARTWORK (artistName TEXT NOT NULL, name TEXT UNIQUE NOT NULL, price FLOAT, available INTEGER, FOREIGN KEY(artistName) REFERENCES ARTIST(artistsName))')
        conn.close()
        self.db_artist = ArtWork_DB.SQLArtworkDB()

        #on setup changes db path to test db path, drops tables and re creates

    def test_add_artwork_without_artist(self):
        with self.assertRaises(sqlite3.DatabaseError):
            a1 = Artwork('Tony', 'artworkName', 400, 0)

        #tests for adding a piece of artwork without first adding an artist in to artist database

    def test_add_duplicate_artist(self):
        a1 = Artist('Tony','tt45@gmail.com')
        a2 = Artist('John', 'tt45@gmail.com')
        with self.assertRaises(ArtworkError):
            self.db_artist.insert_artist(a2)

        #tests for adding duplicate artist

    def test_add_new_artist(self):
        a1 = Artist('Tony', 'tony.spicer.covin@gmail.com')
        self.db_artist.insert_artist(a1)
        expected = { 'Tony' : 'tony.spicer.covin@gmail.com'}
        self.compare_db_add_artist(expected)

        #tests for adding new artist

    def test_add_new_artwork(self):
        a1 = Artwork('Tony', 'Mona', 400, 1)
        self.db_artist.insert_artwork(a1)
        expected = { 'Tony' : "Mona", 400 : 1 }
        self.compare_db_add_artwork(expected)

        #test for adding new artwork

    def test_delete_artwork(self):
        a1 = Artwork('Tony', 'Jody', 400, 1)
        self.db_artist.insert_artwork(a1)
        self.db_artist.delete_artwork('Jody')
        expected = { 'Tony', 'Jody', 400, 1}
        self.check_delete(expected)

        #test for deleting artwork

    def test_duplicate_artwork(self):
        a1 = Artwork('Tony', 'artWorkTitle1', 400, 1)
        self.db_artist.insert_artwork(a1)
        a2 = Artwork('Bee', 'artworkTitle1', 500, 0)
        with self.assertRaises(ArtworkError):
            self.db_artist.insert_artwork(a2)

        #test for adding duplicate artwork, raises error

    def test_change_status_artwork(self):
        a1 = Artwork('Tony', 'Jody', 400, 0)
        self.db_artist.insert_artwork(a1)
        self.db_artist.change_status('Jody', 1)
        expected = { 'Tony' : 'Jody', 400 : 1}
        self.compare_db_add_artwork(expected)

        #test to check change status

    def check_delete(self, expected):
        conn = sqlite3.connect(self.test_db_url)
        all_data = conn.execute('SELECT * FROM ARTWORK').fetchall()
        for row in all_data:
            self.assertNotIn(row[0], expected.keys())

    def compare_db_add_artwork(self, expected):
        conn = sqlite3.connect(self.test_db_url)
        all_data = conn.execute('SELECT * FROM ARTWORK').fetchall()

        for row in all_data:
            self.assertIn(row[0], expected.keys())
            self.assertEqual(expected[row[0]], row[1])

    def compare_db_add_artist(self, expected):
        conn = sqlite3.connect(self.test_db_url)
        all_data = conn.execute('SELECT * FROM ARTIST').fetchall()
        conn.close()
        for row in all_data:
            self.assertIn(row[0], expected.keys())
            self.assertEqual(expected[row[0]], row[1])
        conn.close()

if __name__ == '__main__':
    unittest.main()