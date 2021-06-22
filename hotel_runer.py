from csv_parser import CSVParser
from selenium import webdriver

from csv_writer import CSVWriter
from hotel_link_collector import HotelLinkCollector
from hotel_page_links_collector import HotelPageLinksCollector


class HotelRunner:
    BING_URL_PATH = "https://www.bing.com/"
    CHROME_DRIVER_PATH = 'chromedriver_linux64/chromedriver'


    def __init__(self,input_file_path):
        self.input_file_path = input_file_path
        self.driver = webdriver.Chrome(self.CHROME_DRIVER_PATH)
        self.csv_parser=CSVParser(self.input_file_path)
        self.driver.get(self.BING_URL_PATH)
        self.max_link_number=0
        self.result_data_collecting=[]



    def start_script(self):
        index=0
        while self.csv_parser.is_found(index):
            hotel_under_processing=self.csv_parser.get_hotel_at(index)
            hotel_page_link_collector=HotelPageLinksCollector(self.driver)
            hotels_page_url=hotel_page_link_collector.get_url_hotel(hotel_under_processing.get_hotel_info())##
            self.driver.get(hotels_page_url)##
            hotel_link_collector=HotelLinkCollector(self.driver)
            hotels_colectiong=hotel_link_collector.get_hotel_links()

            if self.max_link_number < len(hotels_colectiong):
                self.max_link_number = len(hotels_colectiong)

            self.result_data_collecting.append(hotels_colectiong)
            index=index+1
            self.driver.get(self.BING_URL_PATH)

        #csv_writer=CSVWriter(self.max_link_number)
        #csv_writer.
        for  i in self.result_data_collecting:
            for x in i:
                print(x)
            print("================================================")
