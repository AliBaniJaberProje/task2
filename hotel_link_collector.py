from selenium import webdriver

from model.hotel_collecting import HotelCollection


class HotelLinkCollector:
    LINKS_XPATH="//li[@class='b_algo']/h2/a"

    def __init__(self,driver):
        self.driver = driver

    def validator_links(self,link):
        START_VALIDATION = "https://www.expedia.com/"
        END_VALIDATION = "Hotel-Information"
        if link.startswith(START_VALIDATION)  and link.endswith(END_VALIDATION):
           return True

        return False

    def get_hotel_links(self):
        hotles_collection=[]
        elements=self.driver.find_elements_by_xpath(self.LINKS_XPATH)
        for element in elements:
            if self.validator_links(element.get_attribute("href")):
                hotles_collection.append(HotelCollection(hotel_url=element.get_attribute("href"),hotel_name=element.text))

        return  hotles_collection





