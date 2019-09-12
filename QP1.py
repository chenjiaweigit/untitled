from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.set_window_size(700,1000)
driver.get("https://hao.360.com")

# 定位到要悬停的元素
above = driver.find_element_by_link_text('58 同 城')
# 对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()
time.sleep(3)
youji = driver.find_element_by_id('search-kw')
ActionChains(driver).context_click(youji).perform()