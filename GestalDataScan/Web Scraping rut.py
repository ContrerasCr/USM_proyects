from selenium import webdriver
base_url="https://www.mercantil.com/"
# declare and initialize driver variable
driver = webdriver.Chrome()
# driver should wait implicitly for a given duration, for the element under consideration to load.
# to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
driver.implicitly_wait(10) #10 is in seconds
# to load a given URL in browser window
driver.get(base_url)
print(driver.title)
# test whether correct URL/ Web Site has been loaded or not
assert "mercantil" in driver.title
# to close the browser
driver.close()