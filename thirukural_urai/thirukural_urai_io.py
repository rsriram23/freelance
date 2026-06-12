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


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--headless")
#thirukural.io site
url = "https://thirukkural.io/"

adhigaram_count=int(input("Enter the number of adhigarams(1-133) you need parimelazhagar urai for: "))

browser=webdriver.Chrome(options)
browser.get(url)

time.sleep(5)
compile_text=''


#anchorLinks=browser.find_elements("xpath",'/html/body/main/div/div/table[1]/tbody/tr[1]/td/a')
anchorLinks=browser.find_elements("tag name","a")
anchorList= anchorListMethod(anchorLinks)

#def get_parimelazhagar_urai():
print("Generating.. Please wait!")
for count in range(adhigaram_count): 
        
    browser.get(anchorList[count])
    urai=browser.find_elements("tag name","details")
    kural_number=browser.find_elements("tag name","a")
    knos=[i.text for i in kural_number if i.text.isdigit()]
    adhigaram_number=knos.pop(0)
    adhigaram=browser.find_element("tag name","h1").text
    compile_text+=f'\nஅதிகாரம் : {adhigaram_number} {adhigaram} \n'
    j=0

    for i in range(len(urai)-1):
        if i%2==0:
            try:
                output=knos[j]+' '+urai[i].text.split('\n\n')[0].split('\n')[1]+'\n\n'
                
                #output=knos[j]+' '+actual_urai+'\n\n'
            except:
                output=f"Encountered an error! i={i} j={j}.urai[i] split,j kural number. 21 elements-2 urai*10 and 1 transliteration) is urai.\n"
            compile_text+=output
            #\n\n split is for separating urai and vilakam, \n is for separating 'urai' and actual urai.
            j=j+1


outfile = open("parimelazhagar_urai.txt", "w", encoding='utf-8')
outfile.write(compile_text)
outfile.close()


print(f"Please check the 'parimelazhagar_urai.txt' file generated with urai for {adhigaram_count} adhigarams. \n thank you!!")

