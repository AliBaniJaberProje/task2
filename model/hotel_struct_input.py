

class InputHotelStruct:

    def __init__(self,hotel_id,hotel_name, hotel_city,hotel_address):
        self.hotel_id=hotel_id
        self.hotel_name=hotel_name
        self.hotel_city=hotel_city
        self.hotel_address=hotel_address

    def get_hotel_info(self):
        return self.hotel_name+" "+self.hotel_city+" "+"expedia"

