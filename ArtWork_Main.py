from view.view import View
from view_model import ViewModel
from database.ArtWork_DB import SQLArtworkDB


def main():

    artwork_db = SQLArtworkDB()
    artwork_view_model = ViewModel(artwork_db)
    artwork_view = View(artwork_view_model)
    artwork_view.show_menu()

#main method to intialize db, get a view model, and than set that view. Than show menu

if __name__ == '__main__':
    main()
