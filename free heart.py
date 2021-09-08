from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.page_load_strategy = 'eager'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)



driver.get("https://padlet.com/nguyenanh15041996/r950znc6raabs8zp")
time.sleep(10)

element = driver.find_element_by_css_selector("#wish-1718183161 > div > article > div.bg-light-ui-100.overflow-hidden.rounded-xl > section > div.flex.flex-row.flex-1.justify-between > div.flex.flex-row.items-center > i")
    
driver.execute_script("arguments[0].click();", element)

driver.delete_all_cookies()

driver.quit()
print("+1 like")
