from selenium import webdriver
from datetime import datetime
from time import sleep

def give_time(input_time,add_hour=0,add_minute=0,add_second=0):
    input_time_split=input_time.split(':')

    input_time+=":"+str(add_second)

    time_dictionary={time_unit:its_value for time_unit,its_value in zip(('h','m','s'),input_time.split(':'))}
    # print(time_dictionary)


url_for_sun_times="https://www.timeanddate.com/sun/india/bengaluru"
#
# browser_option=webdriver.ChromeOptions()
# browser_option.add_argument('--disable-blink-features=AutomationControlled')
browser_connector=webdriver.Chrome()#browser_option)

browser_connector.maximize_window()
browser_connector.get(url_for_sun_times)

## Top of the page
# sunrise_time=browser_connector.find_element('xpath',"//th[text()='Sunrise Today: ']/following-sibling::td").text
# print(sunrise_time)
# sunset_time=browser_connector.find_element('xpath',"//th[text()='Sunset Today: ']/following-sibling::td").text
# print(sunset_time)

today=datetime.now()
sunrise=browser_connector.find_element('xpath',f"//th[text()='{today.day}']/following-sibling::td[1]")#.text
sunset=browser_connector.find_element('xpath',f"//th[text()='{today.day}']/following-sibling::td[2]").text
print(' sunrise: ',sunrise.text[:5],'\n sunset: ',sunset[:5])

browser_connector.execute_script("arguments[0].scrollIntoView(false)",sunrise)
sleep(5)

sunrise_dt=datetime.strptime(sunrise.text[:5],"%H:%M")
sunset_dt=datetime.strptime(sunset[:5],"%H:%M")

daytime_minutes_total=(sunset_dt-sunrise_dt).seconds//60 #total seconds from sun rise to set.
daytime_hours=daytime_minutes_total//60
daytime_minutes=daytime_minutes_total%60

one_kaalam=daytime_minutes_total//5
one_kaalam_hour=one_kaalam//60
one_kaalam_minutes=one_kaalam%60
print(f'total-> {daytime_minutes_total} minutes({daytime_hours} hours and {daytime_minutes} minutes).')
print(f'\n one kaalam: {one_kaalam_hour} hour(s) {one_kaalam_minutes} minutes.')
sleep(5)

each_kaalam=datetime.strptime(f"{one_kaalam_hour}:{one_kaalam_minutes}","%H:%M")

kaalangal=['prataha','sangava','maadhyanhika','aparaanna','saayan']

kaalam_dictionary={}
kaalam_start=sunrise_dt

for kaalam in kaalangal:
    key=kaalam+'Kaalam'

    end_hour=kaalam_start.hour+each_kaalam.hour+((kaalam_start.minute+each_kaalam.minute)//60)
    end_minute=(kaalam_start.minute+each_kaalam.minute)%60
    kaalam_end=datetime.strptime(f"{end_hour}:{end_minute}","%H:%M")
    value=str(kaalam_start.hour).zfill(2)+':'+str(kaalam_start.minute+1).zfill(2)+'-'+str(end_hour).zfill(2)+":"+str(end_minute).zfill(2)
    kaalam_dictionary[key]=value

    if end_minute + 1 == 60:
        kaalam_start=datetime.strptime(f"{end_hour+1}:{0}","%H:%M")
    else:
        kaalam_start=datetime.strptime(f"{end_hour}:{end_minute+1}","%H:%M")
    kaalam_start=kaalam_end

print(kaalam_dictionary)

sleep(10)

