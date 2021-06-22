
class InputHotelStruct:

    def __init__(self,links_list):
        self.links_list=links_list


    def __repr__(self):
         return ",".join(self.links_list)