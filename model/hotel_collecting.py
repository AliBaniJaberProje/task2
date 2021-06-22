class  HotelCollection:

    def __init__(self, hotel_url,hotel_name):
        self.hotel_url=hotel_url
        self.hotel_name=hotel_name

    def __str__(self):
        return self.hotel_url+ " _______ "  +self.hotel_name