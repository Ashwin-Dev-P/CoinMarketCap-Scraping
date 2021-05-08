from selenium import webdriver
driver = webdriver.PhantomJS()
#driver = webdriver.PhantomJS()
driver.get("https://ypa.herokuapp.com/")
p_element = driver.find_element_by_id(id_='target')
print(p_element.text)