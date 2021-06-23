from csv import reader

from model.hotel_struct_input import InputHotelStruct


class CSVParser:


    def __init__(self,input_file_path):
        self.input_file_path=input_file_path
        self.hotel_list=[]
        self.start_reading()


    def start_reading(self):
        with open(self.input_file_path, 'r') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            if header != None:
                for row in csv_reader:
                    hotel_id,hotel_name,hotel_city,hotel_address=row
                    hotel=InputHotelStruct(hotel_id=hotel_id,hotel_name=hotel_name,hotel_city=hotel_city,hotel_address=hotel_address)
                    self.hotel_list.append(hotel)

    def get_hotel_at(self,index):
        return self.hotel_list[index]

    def is_found(self,index):
        if len(self.hotel_list) > index:
            return True
        return False

