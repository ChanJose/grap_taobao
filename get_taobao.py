# 访问页面
from selenium import webdriver

browser = webdriver.Chrome()  # 声明Chrome对象
browser.get('https://www.taobao.com')  # 访问淘宝，获取源代码
print(browser.page_source)  # 打印淘宝页面源代码
browser.close()  # 关闭浏览器