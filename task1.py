from selenium import webdriver
import time
# import system
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
# import string
# import sys

# chrome_options = Options()
# chrome_options.add_argument("--use-fake-ui-for-media-stream")
# driver=webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver",chrome_options=chrome_options)
# driver.get('atg.party')
# time.sleep(2)

browser = webdriver.Firefox()
startTime = time.clock()
print(startTime,"____Website Launch Started_____")
browser.get('https://www.atg.party/')
time.sleep(1)
login=browser.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/ul/li[2]/a')
login.click()
endTime = time.clock();
print(endTime,"______Website launched Succesfully______")
toaltime = endTime - startTime

print(toaltime,"______Reponse Time______")

time.sleep(2)
startTime = time.clock();
print(startTime,"____Login Started_____")

email=browser.find_element_by_id('email')
email.send_keys('wiz_saurabh@rediffmail.com')
passw=browser.find_element_by_id('password')
passw.send_keys('Pass@123')
go=browser.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[3]/button')
go.click()
time.sleep(5)
endTime = time.clock();
print(endTime,"______Website launched Succesfully______")
toaltime = endTime - startTime
print(toaltime,"______Reponse Time______")
# slide=find_element_by_id('dropdownMenuButton')
# slide.click()
# article=find_element_by_xpath('/html/body/div[2]/div[1]/nav/div/table/tbody/tr/td[1]/div/div/div/a[1]')
# article.click()
startTime = time.clock();
print(startTime,"____Article Filling_____")
browser.get('https://www.atg.party/article')
time.sleep(2)
title=browser.find_element_by_id('title')
title.send_keys('task1')
upload=browser.find_element_by_id('article_pic')
upload.send_keys('/home/anshul/Desktop/250075-piece-quotes.jpg')
tags=browser.find_element_by_id('tags-tokenfield')
tags.send_keys('tagged')
browser.find_element_by_id('featurebutton').click()

endTime = time.clock();
print(endTime,"____________")
toaltime = endTime - startTime
print(toaltime,"______Post Done______")
print("Url of new page----https://www.atg.party/mypost")




