from selenium import webdriver
import time

def anchorListMethod(links):
    aList=[]
    for l in links:
        link=l.get_attribute('href')
        linkSplit= link.split('/')
        if linkSplit[3].isdigit() and link not in aList:
            aList.append(link)
    return aList

def genOp(l):
    count=l[1]-1
    i=l[0]
    browser.get(anchorList[count])
    urai=browser.find_elements("tag name","details")
    l1=urai[i].text.split('\n')

    #remove newline
    for i1 in l1:
        if i1=='':
            l1.remove(i1)

    actual_urai=l1[1] #urai text-0, vilakkam-2
    #print(actual_urai)
    print(l1)

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--headless")
#thirukural.io site
url = "https://thirukkural.io/"

browser=webdriver.Chrome(options)
browser.get(url)

anchorLinks=browser.find_elements("tag name","a")
anchorList= anchorListMethod(anchorLinks)


#t=[[6, 40], [4, 42], [2, 46], [18, 62], [4, 97], [0, 101], [8, 114], [18, 117], [16, 123], [14, 125], [18, 126]]
t=[[6, 40],[5,60]]

for i in t:
    genOp(i)

print('Thank you!!')

