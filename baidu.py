from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# driver = webdriver.Firefox()
driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

print(driver.title)
# driver.quit

# 参数数字为像素点
print("设置浏览器宽1100、高800显示")
driver.set_window_size(1100, 1000)
# driver.maximize_window()  #全屏显示
# driver.quit()   #退出浏览器

# from splinter.browser import Browser

# b = Browser("chrome")#指定浏览器，使用chrome浏览器
# b.visit("http://www.baidu.com/")
# dict={"wd":"性能测试"}
# #b.fill("wd","性能测试")
# b.fill_form(dict)
# button = b.find_by_value(u"百度一下")
# button.click()


baidu_url= 'http://www.baidu.com'
print("now access %s" %(baidu_url))
driver.get(baidu_url)
print("start : %s" % time.ctime())
time.sleep(2)
print("END : %s" % time.ctime())

new360_url= 'http://hao.360.com'
print("now access %s" %(new360_url))
driver.get(new360_url)
print("start : %s" % time.ctime())
time.sleep(2)
print("END : %s" % time.ctime())


print("back to %s" % (baidu_url))
driver.back() #返回上一级
print("start : %s" % time.ctime)
time.sleep(2)
print("END : %s" % time.ctime())


print("forward to %s" % (new360_url))
driver.forward()  #前进到360主页
locator = (By.ID,'search-kw')
# driver.refresh()  #刷新操作
print("开始异常处理......")
try:
    WebDriverWait(driver,10).until(EC.presence_of_element_located((locator)))
    driver.find_element_by_id("search-kw").send_keys('python+selenium')
    driver.find_element_by_id("search-btn").click()
    #定位到要悬停的元素
    above = driver.find_element_by_link_text("登录")
    # 对定位到的元素执行鼠标悬停操作
    ActionChains(driver).move_to_element(above).perform()
    driver.find_element_by_id("search-kw").clear()
except:
    print("Exception found yuansu")
    # driver.find_element_by_id("search-btn").click()
    # driver.find_element_by_id("search-kw").send_keys('clear用法')
    # driver.implicitly_wait(10)   #隐性等待，最长等待30秒
    # driver.find_element_by_id("search-btn").click()
# finally:
#     baidu_url = 'http://www.baidu.com'
#     print("now access %s" % (baidu_url))
#     driver.get(baidu_url)
#     # 定位到要悬停的元素
#     above = driver.find_element_by_link_text("登录")
#     # 对定位到的元素执行鼠标悬停操作
#     ActionChains(driver).move_to_element(above).perform()