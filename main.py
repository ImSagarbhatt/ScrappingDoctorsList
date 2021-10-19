# import the webdriver from selenium

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import pandas as pd
from openpyxl import Workbook

# provide the chrome driver PATH and set the driver

PATH = '/home/sagarbhatt/Desktop/seleniumtut/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(PATH)

# provide the url to scrap

driver.get("https://www.justdial.com/Delhi/Doctors/nct-10892680")

dname = []
dratings = []
dlink = []
doc_name = driver.find_elements_by_class_name('lng_cont_name')
for i in doc_name:
    dname.append(i.text)

rating = driver.find_elements_by_class_name('green-box')
for i in rating:
    dratings.append(i.text)


add = driver.find_elements_by_class_name('jcn')
for i in add:
    dlink.append(i.find_element_by_tag_name('a').get_property('href'))


final_list = list(zip(dname, dratings, dlink))


df = pd.DataFrame(final_list, columns=['Name', 'Ratings', 'Reference link'])
pd.set_option('max_colwidth', 105)
print(df)

wb= Workbook()

wb['Sheet'].title='Doctors List'

sh1= wb.active

sh1.append(['Name','Rating','Link'])

for i in final_list:
    sh1.append(i)
wb.save('ScrappedList.xlsx')

driver.quit()
