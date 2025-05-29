from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Page object for the Nova Poshta tracking page 
# This class encapsulates the behavior of the tracking page 
class TrackingPage(BasePage):
    URL = "https://tracking.novaposhta.ua/#/uk"

    # Open the tracking page
    def go_to(self):
        self.driver.get(TrackingPage.URL)

    # Enter the TTN number 
    def search_ttn(self, ttn_number):
        print(f"\033[94mOpen the field for entering the TTN\033[0m")
        ttn_input = self.driver.find_element(By.ID, "en")
        ttn_input.clear()  # Clear the field before entering 
        print(f"\033[94mEnter the TTN number\033[0m {ttn_number}")
        ttn_input.send_keys(ttn_number)

        # Wait for the search button to be clickable 
        search_button = self.driver.find_element(By.ID, "np-number-input-desktop-btn-search-en")
        print(f"\033[94mClick the 'Search' button\033[0m ")
        search_button.click()

    # Wait for the result text to appear
    def get_result_text(self):
        try:
            
            # Search for the element that contains the error text 
            error_block = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "np-number-input-desktop-message-error-message"))
            )
            
            # Return the text of the error block 
            return error_block.text.strip()
        
        # Wait for the result block to appear 
        except TimeoutException:
            print("\033[94mStill no result block after timeout\033[0m")
            return ""
        

           
