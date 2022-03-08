from selenium.webdriver.common.keys import Keys

def send_message(driver, message):
    driver.find_element_by_css_selector(".notranslate").send_keys(message)
    driver.find_element_by_css_selector(".notranslate").send_keys(Keys.RETURN)
