import time


class CSVWriter:


    def __init__(self,max_number_links):
        ts = time.time()
        self.max_number_link=max_number_links
        self.file_output_pointer = open(str(ts) + "__result.csv", "w")
    def write_header(self):
        header="hotel_id,hotel_name,city,address"
        for i in range(1,self.max_number_link+1):
            header=header+",hotel_link"+str(i)+",hotel_name"+str(i)+",hotel_address" + str(i)
        self.file_output_pointer.write(header+"\n")




    def write_result(self, data):
        for  i in data:
            self.file_output_pointer.write(str(i)+"\n")


