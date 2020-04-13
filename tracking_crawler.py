import os
import time
import json
from os import listdir
from selenium import webdriver
from upu_standards import check_code
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-agent=[Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36]")
options.add_argument(f"user-agent=[{UserAgent().random}]")
options.add_argument('headless')

browser = webdriver.Chrome(chrome_options=options)

tracking_codes = []
row = 1
time_end = time.time()+500

db_dir = './db/'
dbs = listdir(db_dir)
crawl_dbs = []
for item in dbs:
    if 'crawl_' in item:
        crawl_dbs.append(item)
filename = db_dir+crawl_dbs[-1]
with open(filename, 'r') as openfile: 
    db = json.load(openfile)

code_list = []
for doc in db:
    code_list.append(doc['code'])

while True:
    try:
        tracking_code = browser.find_element_by_xpath(f'//*[@id="smallWidth"]/div[3]/div/a[{row}]').text
        if tracking_code[-2:] == 'CN' and check_code(tracking_code) and tracking_code not in code_list:
            code_list.append(tracking_code)
            code = {
                "code": tracking_code,
                "included": time.strftime("%d/%m/%Y %H:%M:%S")
            }
            tracking_codes.append(code)
        row+=1
    except:
        os.system('cls')
        print(f'Time left: {int(time_end-time.time())} seconds')
        time.sleep(10)
        row = 1
        browser.get("https://linketrack.com/?utm_source=home")
    if time.time() > time_end:
        break

print(f"\nDone! Acquired {len(tracking_codes)} new codes.\n")
browser.quit()

## Save DB with the same name as the open one
# filename = db_dir+'crawl_'+str(int(time.time()))+'.json'
with open('./db/crawl_bkp.json', "w") as outfile:
    json.dump(db, outfile)
db += tracking_codes
with open(filename, "w") as outfile: 
    json.dump(db, outfile)