from selenium import webdriver

url = "https://www.workingwardrobes.org/donate/donate-money/"

browser = webdriver.Chrome()
browser.get(url)

# browser.find_element_by_xpath('/html/head/script[15]').click
