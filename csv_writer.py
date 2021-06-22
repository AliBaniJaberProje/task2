from datetime import time


class CSVWriter:


    def __init__(self,max_number_links):
        ts = time.time()
        self.max_number_link=max_number_links
        self.file_output_pointer = open(str(ts) + "__result.csv", "w")
    def write_header(self):
        header_list=["hotel_name","location"]
        for i in range(0,self.max_number_link):
            header_list.append("link"+i)


    #def write_output(self):



