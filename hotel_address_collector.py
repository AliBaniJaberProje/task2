from selenium import webdriver



class HotelAddressCollector:
    LOCATION_XPATH="//*[@id='Location']/div/div/div[1]/section/h3"
    CHROME_DRIVER_PATH = 'drivers/chromedriver_linux64/chromedriver'

    def __init__(self,driver):
        self.driver = driver


    def get_hotel_location(self):
        try:
            location = self.driver.find_element_by_xpath(self.LOCATION_XPATH).text
            return location
        except:
            print("error when find location ")
            return "N/A"
            pass
