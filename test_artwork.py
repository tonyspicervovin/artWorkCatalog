import sqlite3
import unittest
from unittest import TestCase
from model.Art_Model import Artwork
from model.Art_Model import Artist
from database import ArtWork_DB




class TestArtworkDB(TestCase):
    test_db_url = 'test_artwork.db'



    def setUp(self):
        ArtWork_DB.db_artist = self.test_db_url

        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('DROP TABLE IF EXISTS ARTIST')
            conn.execute('DROP TABLE IF EXISTS ARTWORK')
        conn.close()

        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('CREATE TABLE ARTIST (artistsName TEXT NOT NULL, email TEXT NOT NULL)')
            conn.execute('CREATE TABLE ARTWORK (artistName TEXT NOT NULL, name TEXT UNIQUE NOT NULL, price FLOAT, available INTEGER, FOREIGN KEY(artistName) REFERENCES ARTIST(artistsName))')
        conn.close()

        self.db_artist = ArtWork_DB.SQLArtworkDB()





    def test_add_new_artist(self):
        a1 = Artist('Tony', 'tony.spicer.covin@gmail.com')
        self.db_artist.insert_artist(a1)
        expected = { 'Tony' : 'tony.spicer.covin@gmail.com'}
        self.compare_db_add_artist(expected)



    def test_add_new_artwork(self):
        a1 = Artwork('Tony', 'Mona', 400, 1)
        self.db_artist.insert_artwork(a1)

        expected = { 'Tony' : "Mona", 400 : 1 }

        self.compare_db_add_artwork(expected)


    def test_delete_artwork(self):
        a1 = Artwork('Tony', 'Jody', 400, 1)
        self.db_artist.insert_artwork(a1)
        self.db_artist.delete_artwork('Jody')
        expected = { 'Tony', 'Jody', 400, 1}
        self.check_delete(expected)

    def test_change_status_artwork(self):
        a1 = Artwork('Tony', 'Jody', 400, 0)
        self.db_artist.insert_artwork(a1)
        self.db_artist.change_status('Jody', 1)
        expected = { 'Tony' : 'Jody', 400 : 1}
        self.compare_db_add_artwork(expected)


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