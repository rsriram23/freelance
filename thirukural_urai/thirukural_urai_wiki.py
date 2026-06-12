from selenium import webdriver
import time

for i in anchorLinks:
    i.get_attribute('href')

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--headless")
#thirukural.io site
url = "https://ta.wikisource.org/wiki/%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AF%81%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AF%81%E0%AE%B1%E0%AE%B3%E0%AF%8D_%E0%AE%AA%E0%AE%B0%E0%AE%BF%E0%AE%AE%E0%AF%87%E0%AE%B2%E0%AE%B4%E0%AE%95%E0%AE%B0%E0%AF%8D_%E0%AE%89%E0%AE%B0%E0%AF%88"

browser=webdriver.Chrome(options)
browser.get(url)
browser.maximize_window()
time.sleep(5)
compile_text=''

#anchorLinks=browser.find_element("xpath",'//*[@id="mw-content-text"]/div[1]/dl[2]/dd[1]/a')
anchorLinks=browser.find_elements("xpath",'//*[@id="mw-content-text"]//a')
dictionary_of_athigaarams_and_its_links=[]
for i in anchorLinks:
    if len(i.text.split('.')) >1:
        dictionary_of_athigaarams_and_its_links[i.text.split('.')[1]]=i.get_attribute('href')


 #link text - 1.கடவுள்வாழ்த்து
browser.find_element("link text","1.கடவுள்வாழ்த்து").click()
thirukural_number=browser.find_elements("xpath","//h2[contains(text(),'திருக்குறள்')]")
#for i in thirukural_number:
#    # print(i.text)
#    compile_text+=i.text
# <dl><dd><b>பரிமேலழகர் உரை</b>:</dd></dl>
##<dl><dd>(இதன் பொருள்) <i>தனக்கு உவமை இல்லாதான் தாள் சேர்ந்தார்க்கு அல்லால்</i> = (ஒருவாற்றானும்) தனக்கு நிகர்இல்லாதவனது, தாளைச்
##சேர்ந்தார்க்கல்லது;</dd>
##<dd><i>மனம் கவலை மாற்றல் அரிது</i> = மனத்தின்கண் நிகழும் துன்பங்களை நீக்குதல் உண்டாகாது.</dd></dl>
##<dl><dd><b>பரிமேலழகர் உரைவிளக்கம்:</b></dd></dl>
##<dl><dd>"உறற்பால- தீண்டா விடுத லரிது"<sup style="font-size:66%; vertical-align:0.6em; line-height:0px;">#</sup> (நாலடியார்,109) என்றாற் போல, ஈண்டு
##‘அருமை’ இன்மைமேல்</dd>
##<dd>நின்றது.</dd></dl>
##<dl><dd>தாள் சேராதார், பிறவிக்கு ஏதுவாய காம வெகுளி மயக்கங்களை மாற்ற மாட்டாமையின், பிறந்து இறந்து அவற்றான் வரும் துன்பங்களுள் அழுந்துவர் என்பதாம்.</dd></dl>
# 10th kural urai
# //*[@id="mw-content-text"]/div[1]/dl[62]/dd[1]
#1st kural urai
# //*[@id="mw-content-text"]/div[1]/dl[2]/dd/b
#thiru_parimelAzhagar=browser.find_elements("xpath","//b[contains(text(),'பரிமேலழகர் உரை')]")
#thiru_parimelAzhagar=browser.find_elements("xpath","//dl[text()='பரிமேலழகர் உரை:']")

thiru_parimelAzhagar=[]

# kural 1
eachUrai=''
eachUrai=browser.find_element("xpath",'//*[@id="mw-content-text"]/div[1]/dl[2]/dd[1]').text
eachUrai+= browser.find_element("xpath",'//*[@id="mw-content-text"]/div[1]/dl[3]/dd[1]').text
thiru_parimelAzhagar.append(eachUrai)


#kural 2
thiru_parimelAzhagar.append(browser.find_element("xpath",'//*[@id="mw-content-text"]/div[1]/dl[11]/dd[1]').text)
thiru_parimelAzhagar.append(browser.find_element("xpath",'//*[@id="mw-content-text"]/div[1]/dl[12]/dd[1]').text)

#kural 10
thiru_parimelAzhagar.append(browser.find_element("xpath",'//*[@id="mw-content-text"]/div[1]/dl[62]/dd[1]').text)
thiru_parimelAzhagar.append(browser.find_element("xpath",'//*[@id="mw-content-text"]/div[1]/dl[62]/dd[2]').text)

#print(len(thiru_parimelAzhagar))
for i,j in zip(thirukural_number,thiru_parimelAzhagar):
##    i.click()
##    time.sleep(5)
##    print(i.text)
    compile_text+=i.text+' - உரை:\n'+j+'\n\n'
    

print(f'compiled text:\n{compile_text} \n thank you!!')
#browser.close()
