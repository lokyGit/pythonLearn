from selenium import webdriver
driver = webdriver.Chrome(r'C:\Users\lorib\loky\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello Cimcon World!!! This is Lokesh Palacharla')
showMessage = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessage.click()
additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('45')
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('55')
getTotalbutton =  driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalbutton.click()