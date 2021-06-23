
class OutputHotelStruct:

    def __init__(self,hotel_input_row,hotel_collecting_info):
        self.links_list=hotel_collecting_info
        self.hotel_input_row=hotel_input_row



    def __repr__(self):
         return ",".join(self.links_list)