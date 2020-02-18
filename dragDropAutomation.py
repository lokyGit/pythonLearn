from selenium import webdriver
driver = webdriver.Chrome(r'C:\Users\lorib\loky\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")