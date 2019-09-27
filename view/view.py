
from model.Art_Model import Artist
from model.Art_Model import Artwork
from exceptions.artwork_error import ArtworkError
from database.ArtWork_DB import SQLArtworkDB
from view.view_utils import input_positive_float
from view.view_utils import input_yes_or_no
from view.view_utils import show_all_artwork_list
class View:

    def __init__(self, view_model):
        self.view_model = view_model


    def show_menu(self):
        while True:
            choice = int(input("MENU \n1: Add Artist \n2: "
                               "Search all artwork by artist \n3: Search available artwork by artist \n"
                               "4: Add a new artwork \n5: Delete an artwork  \n6: Change status of artwork \n7: Exit \n"))
            if choice == 1:
                self.add_new_artist()
            elif choice == 2:
                self.search_all_artist()
            elif choice == 3:
                pass
            elif choice == 4:
                self.add_new_artwork()
            elif choice == 5:
                pass
            elif choice == 6:
                pass
            elif choice == 7:
                break
            else:
                print("Unknown option selected")

    def add_new_artist(self):
        print("******Insert a new artist in to the database******\n")

        while True:
            name = input("Enter the artists name to insert or enter to quit: \n")
            if not name:
                break

            email = input(f"Enter the email for {name}: \n")
            artist = Artist(name, email)
            try:
                self.view_model.insert_artist(artist)
                print(artist.name+" added!")
                break
            except ArtworkError as e:
                print(str(e))

    def add_new_artwork(self):
        print('******Insert a new piece of artwork in to the database******\n')

        while True:
            artist = input("Enter the artist of the artwork or enter to quit\n")
            if not artist:
                break
            name = input("Enter the name of the piece\n")
            price = input_positive_float(f'Enter the price for {name}')
            available = input_yes_or_no(f"Is {name} available? yes or no\n")

            artwork = Artwork(artist, name, price, available)
            try:
                self.view_model.insert_artwork(artwork)
                print(artwork.name+" added!")
                break
            except ArtworkError as e:
                print(str(e))
    def search_all_artist(self):
        print('******Search for all artwork by an artist*******')

        while True:
            artist = input('Enter the artist to search for or enter to quit')
            if not artist:
                break
            try:
                all_artwork = self.view_model.search_all_artwork(artist)
                show_all_artwork_list(all_artwork)
                break
            except ArtworkError as e:
                print(str(e))