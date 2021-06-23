from csv_parser import CSVParser
from selenium import webdriver

from csv_writer import CSVWriter
from hotel_info_collector import HotelInfoCollector
from hotel_page_links_collector import HotelPageLinksCollector
from model.hotel_struct_output import OutputHotelStruct
import platform

class HotelRunner:
    BING_URL_PATH = "https://www.bing.com/"
    CHROME_DRIVER_PATH_LINUX = 'drivers/chromedriver_linux64/chromedriver'
    CHROME_DRIVER_PATH_WINDOWS="drivers/chromedriver_win32/chromedriver"

    def __init__(self,input_file_path):
        if platform.system().lower()=="linux":
            self.driver = webdriver.Chrome(self.CHROME_DRIVER_PATH_LINUX)
        elif platform.system().lower()=="windows":
            self.driver = webdriver.Chrome(self.CHROME_DRIVER_PATH_WINDOWS)
        self.driver.get(self.BING_URL_PATH)

        self.input_file_path = input_file_path
        self.csv_parser=CSVParser(self.input_file_path)



        self.max_link_number=0
        self.result_data=[]



    def start_script(self):
        index=0

        while self.csv_parser.is_found(index):
            hotel_under_processing=self.csv_parser.get_hotel_at(index)

            hotel_page_link_collector=HotelPageLinksCollector(self.driver)

            hotel_page_link_collector.get_hotels(hotel_under_processing.get_hotel_info())##

            hotel_link_collector=HotelInfoCollector(self.driver)
            hotels_colecting=hotel_link_collector.get_hotel_info()

            if self.max_link_number < len(hotels_colecting):
                self.max_link_number = len(hotels_colecting)

            index=index+1

            self.driver.get(self.BING_URL_PATH)
            result_row=OutputHotelStruct(hotel_input_row=hotel_under_processing,hotel_collecting_info=hotels_colecting)
            self.result_data.append(result_row)

        csv_writer=CSVWriter(self.max_link_number)
        csv_writer.write_header()
        csv_writer.write_result(self.result_data)
