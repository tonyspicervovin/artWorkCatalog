

class ViewModel:

    def __init__(self, db):
        self.db = db

    def insert_artist(self, artist):
        self.db.insert_artist(artist)

    def insert_artwork(self, artwork):
        self.db.insert_artwork(artwork)
    def search_all_artwork(self, artist):
        self.db.search_all_artwork(artist)
    def search_available_artwork(self, artist):
        self.db.search_available_artwork(artist)
    def delete_artwork(self, artwork):
        self.db.delete_artwork(artwork)
    def change_status(self, artwork, available):
        self.db.change_status(artwork, available)