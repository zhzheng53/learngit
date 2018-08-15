from selenium import webdriver
import time

A = time.ctime()
print("开始时间:%s" % A)
driver = webdriver.Firefox()
#for i in range(5):
driver.get("http://www.baidu.com")
driver.maximize_window()  # 浏览器最大化
driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()
time.sleep(1)
driver.quit()
B = time.ctime()
print("结束时间:%s" %B )
print("")









'''
Mon Jul 23 09:59:50 2018
Mon Jul 23 10:00:08 2018     18
Mon Jul 23 10:05:52 2018
Mon Jul 23 10:06:08 2018     16 
Mon Jul 23 10:07:47 2018
Mon Jul 23 10:08:04 2018     17

Mon Jul 23 10:01:55 2018
Mon Jul 23 10:02:11 2018     16
Mon Jul 23 10:04:58 2018
Mon Jul 23 10:05:14 2018     16
Mon Jul 23 10:06:52 2018
Mon Jul 23 10:07:10 2018     18
'''