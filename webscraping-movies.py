from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

wb = xl.Workbook()
ms = wb.active
ms.title = 'First Sheet'

mv_table = soup.find('table')

mv_rows = mv_table.findAll('tr')

#print(mv_rows[1])

ms['A1'] = "No."
ms['B1'] = "Title"
ms['C1'] = 'Gross'
ms['D1'] = 'Total Gross'
ms['E1'] = "Percent of Gross"

 


wb.save('Box Office Report.xlsx')

for x in range(1,6):
    td = mv_rows[x].findAll('td')
    rank = td[0].text
    title = td[1].text
    gross = int(td[5].text.replace(",","").replace("$",""))
    t_gross = int(td[7].text.replace(",","").replace("$",""))

    percent = round((gross/t_gross)*100,2)
    
    wb.save('Box Office Report.xlsx')
