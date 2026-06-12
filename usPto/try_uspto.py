# Trying US PTO
#url -- https://www.uspto.gov/
# search - https://ppubs.uspto.gov/basic/

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select


chrome_driver = webdriver.Chrome()
chrome_driver.get("https://ppubs.uspto.gov/basic/")

#text box1 - search
searchTextbox1=chrome_driver.find_element("id","searchText1")
searchTextbox1.send_keys('cryptography')

sleep(3)

#search operator choosing - and, or, not
operator_drop_down=chrome_driver.find_element("id","searchOperator")
select_object=Select(operator_drop_down)
select_object.select_by_value('OR')

sleep(3)

#search text box 2
searchTextbox2=chrome_driver.find_element("id","searchText2")
searchTextbox2.send_keys('security')

sleep(3)

#search button clicking.
searchButton=chrome_driver.find_element("id","basicSearchBtn")
searchButton.click()

sleep(10)

#query result - table (put explicit wait here)
query_result_table=chrome_driver.find_element("id","searchResults")

chrome_driver.execute_script("arguments[0].scrollIntoView()",query_result_table)

#collection of rows
row_entries=query_result_table.find_elements('xpath','//tbody//tr')
print(f'Found {len(row_entries)} entries or rows displayed')

#fetching one record, say 1st.
print('First entry-> ',row_entries[0].text)

#constructing a dictionary of headings- each table field or column's heading. can be used as reference inside the table. eg. td[1] will be 'Result #' and can be # referred by: td[dictionary_variable['Result #']] and this applies to other 6 feilds as well.2 doc/patent no, 3 display .. 7 pages.
# ['Result #', 'Document/Patent number', 'Display', 'Title', 'Inventor name', 'Publication date', 'Pages']
table_columns=query_result_table.find_elements('tag name','th')
column_headings_dictionary={heading.text:index for index,heading in enumerate(table_columns)}
print('Headings found are: ',column_headings_dictionary)

print('3rd row full-> ',row_entries[2].text)
input('waiting to verify 3rd row..')
# trying to print "Inventor name" for the 3rd entry/item in the 3rd row of the table.
third_row=[field_value.text for field_value in row_entries[2].find_elements('tag name','td')]
print(f'3rd entry/row:\n Title : {third_row[column_headings_dictionary['Title']]} \n Inventor(s): {third_row[column_headings_dictionary['Inventor name']]}')
input('is it as expected?')

#total records for the keywords(cryptography and security) given.
total_records=chrome_driver.find_element('id','pageInfo')
print(f'Found {total_records.text.split(' of ')[1]} records.')

chrome_driver.execute_script("arguments[0].scrollIntoView()",total_records)

sleep(5)

print('done')
