from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import argparse
import requests
from io import open as iopen
from uploader import uploader

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--searchterm", required=True, help="Keyword want to search in google images")
ap.add_argument("-b", "--bucket", help="S3 bucket name you want to upload files")
ap.add_argument("-d", "--directory", help="Files directory to upload to S3")
args = vars(ap.parse_args())

searchterm = args["searchterm"] 

url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"

browser = webdriver.Chrome()
browser.get(url)
header="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
counter = 0
succounter = 0

if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in range(500):
    browser.execute_script("window.scrollBy(0,10000)")

for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print("Total Count:", counter)
    print("Succsessful Count:", succounter)
    print("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])

    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
    print("url : " + img)
    try:
        i = requests.get(img, headers={"User-Agent":header})
        print("url : " + img)
        with iopen(os.path.join(searchterm , searchterm + "_" + str(counter) + "." + imgtype), 'wb') as file:
            file.write(i.content)
        succounter = succounter + 1
    except Exception as e:
            print(e)

print(succounter, "pictures succesfully downloaded")
browser.close()


if args["bucket"] != None:
    print('Uploading to S3...')
    uploader.upload(bucket_name=args["bucket"], direction=args["directory"])
else:
    print('Uploading is done!')