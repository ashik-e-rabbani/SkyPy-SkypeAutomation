from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from skpy import user
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(' — headless')
# chrome_options.add_argument(' — no-sandbox')
# chrome_options.add_argument(' — disable-dev-shm-usage')
driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)

driver.get("https://web.skype.com/")
# print(driver.page_source)

username = driver.find_element_by_xpath('//*[@id="i0116"]')
username.send_keys("pslsky@outlook.com")
username.send_keys(Keys.ENTER)

password = driver.find_element_by_xpath('//*[@id="i0118"]')
password.send_keys("aer@surecash")

driver.implicitly_wait(2)

singIn = driver.find_element_by_xpath('//*[@id="lightbox"]/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div/div')


singIn.click()