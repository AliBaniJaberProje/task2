from selenium import webdriver

from hotel_address_collector import HotelAddressCollector
from model.hotel_collecting import HotelCollection


class HotelInfoCollector:
    LINKS_XPATH="//li[@class='b_algo']/h2/a"

    def __init__(self,driver):
        self.driver = driver

    def validator_links(self,link):
        START_VALIDATION = "https://www.expedia.com/"
        END_VALIDATION = "Hotel-Information"
        if link.startswith(START_VALIDATION)  and link.endswith(END_VALIDATION):
           return True

        return False

    def get_hotel_info(self):
        hotles_collection=[]
        elements=self.driver.find_elements_by_xpath(self.LINKS_XPATH)
        for element in elements:
            hotel_link=element.get_attribute("href")
            hotel_name=element.text
            if self.validator_links(hotel_link):
                # self.driver.get(hotel_link)
                hotel_location_collector=HotelAddressCollector(hotel_link)#####
                hotel_address=hotel_location_collector.get_hotel_location()
                hotles_collection.append(HotelCollection(hotel_url=hotel_link,hotel_name=hotel_name,hotel_address="hotel_address"))
        return  hotles_collection





