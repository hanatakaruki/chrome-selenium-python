from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#setup  chromedriver
driver = webdriver.Chrome()

#open google.com
driver.get("http://www.google.com")

#assert for google title
assert "Google" in driver.title

#find search bar
elem = driver.find_element_by_name("q")

#write pycon in search bar
elem.send_keys("pycon")

#press enter
elem.send_keys(Keys.RETURN)

#assert for google title again
assert "pycon - Google Search" in driver.title

#close browser and end the test
driver.close()
