import time


class CSVWriter:


    def __init__(self,max_number_links):
        ts = time.time()
        self.max_number_link=max_number_links
        self.file_output_pointer = open(str(ts) + "__result.csv", "w")
    def write_header(self):
        header_list=["hotel_id","hotel_name","city","address"]
        for i in range(1,self.max_number_link+1):
            header_list.append("link"+str(i))
            header_list.append("hotel_name"+str(i))
            header_list.append("hotel_address" + str(i))
        self.file_output_pointer.write(str(header_list))

    #def write_output(self):



x=CSVWriter(4)
x.write_header()
