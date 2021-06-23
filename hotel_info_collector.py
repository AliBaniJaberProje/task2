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
        try:
            elements=self.driver.find_elements_by_xpath(self.LINKS_XPATH)
            for element in elements:
                hotel_link=element.get_attribute("href")
                hotel_name=element.text
                if self.validator_links(hotel_link):
                    hotles_collection.append(HotelCollection(hotel_url=hotel_link,hotel_name=hotel_name))


            i=0
            while (i<len(hotles_collection)):
                try:
                    self.driver.get(hotles_collection[i].hotel_url)
                    hotel_address_collection = HotelAddressCollector(self.driver)
                    address = hotel_address_collection.get_hotel_location()
                    hotles_collection[i].set_address(address)
                except:
                    print("error in find location")
                    break
                i=i+1


        except:
            print("error in find elemants ")






        return  hotles_collection





