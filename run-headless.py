from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#add option to using headless
options = Options()
options.headless = True

#using option to using headless
driver = webdriver.Chrome(chrome_options=options)

#open google.com
driver.get("http://www.google.com")

#assert google title and print to log
assert "Google" in driver.title
print(driver.title)

#find search bar
elem = driver.find_element_by_name("q")

#write pycon in search bar
elem.send_keys("pycon")

#press enter
elem.send_keys(Keys.RETURN)

#assert for google title again and print to log
assert "pycon - Google Search" in driver.title
print(driver.title)

#close browser and end the test
driver.close()
