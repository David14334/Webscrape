# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from cgi import test
from email import header
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers= headers )

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)



table_rows = soup.findAll("tr")
'''
for row in table_rows[2:51]: 
    td = row.findAll("td")
    state = td[1].text
    total_cases = int(td[2].text.replace(',', ''))
    total_death = int(td[4].text.replace(',', ''))
    total_tested = int(td[10].text.replace(',', ''))
    print(f"State: {state}")
    print(f"Total Cases: {total_cases}")
    print(f"Total Deaths: {total_death}")
    print(f"Total Tested: {total_tested}")
    input()
'''


state_death_ratio = ''
state_best_testing = ''
state_worst_testing =''
highest_death_ratio = 0.0
highest_testing_ratio = 0.0
lowest_testing_ratio = 0.0



for row in table_rows[2:51]:
    td = row.findAll("td")
    state = td[1].text
    total_cases = int(td[2].text.replace(',', ''))
    total_death = int(td[4].text.replace(',', ''))
    total_tested = int(td[10].text.replace(',', ''))


    death_ratio = (total_death / total_cases)
    testing_ratio = (total_tested / total_cases)

    if death_ratio > (highest_death_ratio):
        state_death_ratio = state
        highest_death_ratio = death_ratio
    if testing_ratio > (highest_testing_ratio):
        state_best_testing = state
        highest_testing_ratio = testing_ratio
    if testing_ratio < (lowest_testing_ratio):
        state_worst_testing = state
        lowest_testing_ratio = testing_ratio


print()
print("State with the highest death rate:", state_death_ratio)
print("Death Rate:", format(highest_death_ratio, '.2%'))
print()
print("The state with the best testing ratio is:", state_best_testing)
print("Best Testing Ratio:", format(highest_testing_ratio, '.2%'))
print()
print("The state with the worst testing ratio is:", state_worst_testing)
print("Worst Testing Ratio:", format(lowest_testing_ratio, '.2%'))


#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")
