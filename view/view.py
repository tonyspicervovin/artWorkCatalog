from model.Art_Model import Artist
from model.Art_Model import Artwork
from exceptions.artwork_error import ArtworkError
from view.view_utils import input_positive_float
from view.view_utils import input_yes_or_no


class View:

    def __init__(self, view_model):
        self.view_model = view_model

    #sets view model

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
                self.search_available_artist()
            elif choice == 4:
                self.add_new_artwork()
            elif choice == 5:
                self.delete_an_artwork()
            elif choice == 6:
                self.change_status()
            elif choice == 7:
                break
            else:
                print("Unknown option selected")

    #shows menu options and calls methods

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

    #method to insert artist to database, recieves input and email and creates new artist object
    #  calls view model to call db to insert

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

    #method to add artwork, recieves artist, name, price and availability and creates new artwork object
    #calls view model to call db file to insert object in to db

    def search_all_artist(self):
        print('******Search for all artwork by an artist*******')
        while True:
            artist = input('Enter the artist to search for or enter to quit\n')
            if not artist:
                break
            try:
                all_artwork = self.view_model.search_all_artwork(artist)
                if not all_artwork:
                    print(f"Nothing found for artist {artist}")
                for row in all_artwork:
                    if row.available == 1:
                        available = "Yes"
                    elif row.available == 0:
                        available = "No"
                    print(f'Name: {row.name} Artist: {row.artist} Price: {row.price} Available: {available}' )
                break
            except ArtworkError as e:
                print(str(e))

    #method to search artist, takes an input and calls view model to call db file to search db and display results

    def search_available_artist(self):
        print('******Search for artwork available by an artist******')
        while True:
            artist = input('Enter the artist to search for or enter to quit\n')
            if not artist:
                break
            try:
                available_artwork = self.view_model.search_available_artwork(artist)
                for row in available_artwork:
                    print(f'Name: {row.name} Artist: {row.artist} Price: {row.price} Available: Yes')
                break
            except ArtworkError as e:
                print(str(e))

    #method to search artist, takes an input and calls view model to call db file to search db and display results
    #only returns artwork that is available

    def delete_an_artwork(self):
        print('******Delete an artwork by name******')
        while True:
            artwork = input('Enter the artworks name to be deleted or enter to quit\n')
            if not artwork:
                break
            try:
                isDelete = self.view_model.delete_artwork(artwork)
                if isDelete is False:
                    print(artwork+" not found")
                else:
                    print(artwork+" deleted")
                break
            except ArtworkError as e:
                print(str(e))

    #method to delete artwork, recieves an artwork piece's name and calls view model to call db file
    #to delete from db, displays results of deleted or not

    def change_status(self):
        print('******Change status of artwork to available or not available******')
        while True:
            artwork = input('Enter the artworks name to be changed or enter to quit\n')
            available = input_yes_or_no(f"set {artwork} available? yes or no\n")
            if not artwork:
                break
            try:
                changed_artwork = self.view_model.change_status(artwork, available)
                if changed_artwork is False:
                    print(artwork+' not found')
                else:
                    print(f'{artwork} updated')
                break
            except ArtworkError as e:
                print(str(e))

    #method to change the available status of a piece of artwork, displays whether
    #piece was changed, or if none was found that is displayed