

class Artwork():
    def __init__(self, artist, name, price, available):
        self.artist = artist
        self.name = name
        self.price = price
        self.available = available

        def __str__(self):
            return f'Name: {self.name}, Artist: {self.artist}, Price: {self.price}, Available: {self.available}'

class Artist():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}'

#defines both artwork and artist classes which define the objects that will be created