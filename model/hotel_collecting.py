from model.hotel_struct_input import InputHotelStruct


class  HotelCollection:

    def __init__(self, hotel_url,hotel_name,hotel_address):
        self.hotel_url=hotel_url
        self.hotel_name=hotel_name
        self.hotel_address=hotel_address

    def __str__(self):
        return self.hotel_url+ " _______ "  +self.hotel_name