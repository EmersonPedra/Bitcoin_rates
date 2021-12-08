from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import csv


def scrap_the_page(page):

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(page)
    table = driver.find_element_by_tag_name('table')
    data = table.text.split('\n') 
    driver.close()    
    return data 

def parser(extratedDate):
    rows = []
    parsed = []
    for row in extratedDate:
        rows.append(row.split(' '))
    for row in rows[2:12]:
        parsed.append({'Date': row[0] + ' ' + row[1][0:-1] + ' ' + row[2], 'BTC Closing Value': row[7]})
    return parsed

def write_csv_file(name, data):
    with open(name, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'BTC Closing Value']
        csvWriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvWriter.writeheader()
        for row in data:
            csvWriter.writerow(row)                                                                                                                                                                                                                                                                                          

page = scrap_the_page('https://finance.yahoo.com/quote/BTC-EUR/history?p=BTC-EUR')
parsedData = parser(page)
write_csv_file('eur_btc_rates.csv', parsedData)
