from xml.etree.ElementTree import fromstring
from bs4 import BeautifulSoup


import json

import requests

#url = 'http://www.ffiec.gov/census/report.aspx?year=2011&state=01&report=demographic&msa=11500'
url = "https://finance.yahoo.com/quote/AAPL/key-statistics/"
#url = 'https://www.investing.com/equities/apple-computer-inc-technical'
rsp = requests.get(url)
#print rsp.content
#html = requests.get(url).content

#rsp = requests.get('https://www.investing.com/equities/apple-computer-inc-technical&output=json')


if rsp.status_code in (200,):

    # This magic here is to cut out various leading characters from the JSON 
    # response, as well as trailing stuff (a terminating ']\n' sequence), and then
    # we decode the escape sequences in the response
    # This then allows you to load the resulting string
    # with the JSON module.
    HTML = rsp.content
    
    
    soup = BeautifulSoup(HTML, 'html.parser')

    table_tag = soup.findAll('table', attrs={'class':'table-qsp-stats'})
    for line in table_tag:
            th = table_tag.find('span')
            print th
    #firstlist = soup.get_text()
    
    print firstlist
    #price = firstlist.find('data-reactid')
    #print price


      #span = soup.find("class", name="Fz(s) Fw(500) Ta(end)", reactid="308")
    #print HTML
    #soup = BeautifulSoup(HTML)
    #data = soup.find("table", attrs={"class":"technicalIndicatorsTbl"})
    

    