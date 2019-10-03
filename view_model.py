

class ViewModel:

    def __init__(self, db):
        self.db = db

    def insert_artist(self, artist):
        self.db.insert_artist(artist)

    def insert_artwork(self, artwork):
        self.db.insert_artwork(artwork)
    def search_all_artwork(self, artist):
        artworks = self.db.search_all_artwork(artist)
        return artworks;
    def search_available_artwork(self, artist):
        artworks = self.db.search_available_artwork(artist)
        return artworks;
    def delete_artwork(self, artwork):
        isDelete = self.db.delete_artwork(artwork)
        return isDelete
    def change_status(self, artwork, available):
        isChanged = self.db.change_status(artwork, available)
        return isChanged

#this file is called from view with arguments to communicate with the db file, and than
#recieve information from db file and communicate back to view file