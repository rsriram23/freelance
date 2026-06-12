# Trying Tn reginet
#url -- https://tnreginet.gov.in/portal/

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

driver = webdriver.Chrome(opt)

driver.get("https://tnreginet.gov.in/portal/")
time.sleep(60)
# zone - zoneList
# sub-registrar - id SROList
# village - villageList
# street - text - streetName

zones= Select(driver.find_element('id','zoneList'))
print('total zones: ',len(zones.options))
count=0
for zone in zones.options:
    
    count=count+1
    print(f'zone {count}')

#for i in range(1,len(zones.options)):

    zones.select_by_visible_text(zone.text)
    time.sleep(2)
    SROs_forThis_zone=Select(driver.find_element('id','SROList'))
    for sro in SROs_forThis_zone.options:

        sri=0

        SROs_forThis_zone.select_by_visible_text(sro.text)
        time.sleep(2)
        # villageList
        villageUnderSro=Select(driver.find_element('id','villageList'))
        for village in villageUnderSro.options:
            print(f'sri={sri} Zone--{zone.text}  --  SRO--{sro.text}  --  Village--{village.text}')
            if sri < 5:
                sri += 1
            else:
                break

print('done')

