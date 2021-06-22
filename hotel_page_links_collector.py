from selenium import webdriver


class HotelPageLinksCollector:

    INPUT_SEARCH_HOTEL_XPATH="//*[@id='sb_form_q']"
    BUTTON_SEARCH_XPATH="//*[@id='sb_form']/label"

    def __init__(self,driver):
        self.driver = driver


    def get_url_hotel(self,hotel_info):
         search = self.driver.find_element_by_xpath(self.INPUT_SEARCH_HOTEL_XPATH)
         search.send_keys(hotel_info)
         search_button=self.driver.find_element_by_xpath(self.BUTTON_SEARCH_XPATH)
         search_button.click()
         return self.driver.current_url
