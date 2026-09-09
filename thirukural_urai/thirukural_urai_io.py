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

def give_for_adhigaram(number):
    global compile_text
    browser.get(anchorList[number])
    uraigal = browser.find_elements("tag name", "details")  # 21 details tag(10x2 urai, 1 transliteration).
    kural_number = browser.find_elements("tag name", "a")
    kural_nos = [number.text for number in kural_number if number.text.isdigit()]
    adhigaram_number = kural_nos.pop(0)
    adhigaram = browser.find_element("tag name", "h1").text
    compile_text += f'\nஅதிகாரம் : {adhigaram_number} {adhigaram} \n'
    kural = 0

    for urai in range(len(uraigal) - 1):
        if urai % 2 == 0:  # every kural-0 parimelazhagar, 1 manikudavar.
            try:
                output = kural_nos[kural] + ' ' + uraigal[urai].text.split('\n\n')[0].split('\n')[1] + '\n\n'

                # output=knos[j]+' '+actual_urai+'\n\n'
            except:
                output = f"Encountered an error! i={urai} j={kural}.urai[i] split,j kural number. 21 elements-2 urai(mankudavar,parimelazhagar)*10 and 1 transliteration(10 kurals in english)) is urai.\n"
            compile_text += output
            '''
            \n\n split is for separating urai and vilakam, \n is for separating 'urai' and actual urai.
            '''
            kural = kural + 1



options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--headless")
#thirukural.io site
url = "https://thirukkural.io/"

print('*********\n Welcome to the Sri.பரிமேலழகர்(Parimelazhagar) urai extraction utility.\n Site used:https://thirukkural.io/ \n *********')


adhigaram_count=int(input("Enter the number of adhigarams(1-133) you need parimelazhagar urai for(3 will print 1 to 3 adhigaarams): "))
adhigaram_number=int(input("Enter the adhigaram number(1-133) you want the urai for: "))
if 0<adhigaram_number<134 and 0<adhigaram_count<134:
    print('Please enter only 1 to 133.\n\n Thank You!')
    exit(0)


print('proceeding..')
browser=webdriver.Chrome(options)

browser.get(url)

time.sleep(5)
compile_text='Source: https://thirukkural.io/ \n'


#anchorLinks=browser.find_elements("xpath",'/html/body/main/div/div/table[1]/tbody/tr[1]/td/a')
anchorLinks=browser.find_elements("tag name","a")
anchorList= anchorListMethod(anchorLinks)


#def get_parimelazhagar_urai():
print("Generating.. Please wait!")
if adhigaram_count>0:

    for count in range(adhigaram_count):
        give_for_adhigaram(count)
    adhigaram_count=str(adhigaram_count)+' adhigarangal.'
else:
    give_for_adhigaram(adhigaram_number-1)
    suffix_dictionary={1:'st',2:'nd',3:'rd'}
    suffix_dictionary.update({num:'th' for num in (0,4,5,6,7,8,9)})
    suffix=suffix_dictionary[adhigaram_number%10]
    adhigaram_count=str(adhigaram_number)+suffix+' adhigaram.'


outfile = open("parimelazhagar_urai.txt", "w", encoding='utf-8')
outfile.write(compile_text)
outfile.close()


print(f"Please check the 'parimelazhagar_urai.txt' file generated with urai for {adhigaram_count} \n\n Thank you!!")

