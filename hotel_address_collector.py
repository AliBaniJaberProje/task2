from selenium import webdriver



class HotelAddressCollector:
    LOCATION_XPATH="//*[@id='Location']/div/div/div[1]/section/h3"
    CHROME_DRIVER_PATH = 'chromedriver_linux64/chromedriver'

    def __init__(self,hotel_url):
        self.driver = webdriver.Chrome(self.CHROME_DRIVER_PATH)
        self.hotel_url = hotel_url

    def get_hotel_location(self):
        try:
            self.driver.get(self.hotel_url)
            location = self.driver.find_element_by_xpath(self.LOCATION_XPATH).text
            self.driver.quit()
            return location
        except:
            print("error when find location ")