from model.hotel_struct_input import InputHotelStruct


class OutputHotelStruct(InputHotelStruct):

    def __init__(self,hotel_input_row,hotel_collecting_info):
        self.hotel_collecting_info=hotel_collecting_info
        super().__init__(hotel_id=hotel_input_row.hotel_id,hotel_name=hotel_input_row.hotel_name,hotel_city=hotel_input_row.hotel_city,hotel_address=hotel_input_row.hotel_address)


    def __repr__(self):
        result=self.hotel_id+","+self.hotel_name+","+self.hotel_city+","+self.hotel_address
        for i in self.hotel_collecting_info:
            result=result+","+i.hotel_url+","+i.hotel_name+","+i.hotel_address
        return result
