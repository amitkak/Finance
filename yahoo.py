import json

import requests

rsp = requests.get('https://finance.google.com/finance?q=AAPL&output=json')


#rsp = requests.get('https://www.investing.com/equities/apple-computer-inc-technical&output=json')


if rsp.status_code in (200,):

    # This magic here is to cut out various leading characters from the JSON 
    # response, as well as trailing stuff (a terminating ']\n' sequence), and then
    # we decode the escape sequences in the response
    # This then allows you to load the resulting string
    # with the JSON module.
    fin_data = json.loads(rsp.content[6:-2].decode('unicode_escape'))
    
    #print fin_data
    # print out some quote data
    
    shares = fin_data['shares']
    print shares      

    div_yield = fin_data['dy']
    print div_yield      

    qtr_div = fin_data['ldiv']
    print qtr_div    


    Net_Profit_Margin = fin_data['keyratios'][0]['ttm']
    print Net_Profit_Margin

    Operating_Profit_Margin = fin_data['keyratios'][1]['ttm']
    print Operating_Profit_Margin


    EBITDA_Profit_Margin = fin_data['keyratios'][2]['ttm']
    print EBITDA_Profit_Margin

    ROA = fin_data['keyratios'][3]['ttm']
    print ROA
    ROE = fin_data['keyratios'][4]['ttm']
    print ROE
    Employees = fin_data['keyratios'][5]['recent_quarter']
    print Employees





    #array = '{"fruits": ["apple", "banana", "orange"]}'
    #data  = json.loads(array)
    #print data['fruits']
    eps = fin_data['eps']
    print eps      
    
    pe = fin_data['pe']
    print pe      
    hi52 = fin_data['hi52']
    print hi52      
    lo52 = fin_data['lo52']
    print lo52      
    vol = fin_data['vo']
    print vol      
    avgvol = fin_data['avvo']
    print avgvol      

    #print('Opening Price: {}'.format(fin_data['op']))
    #print('Price/Earnings Ratio: {}'.format(fin_data['pe']))
    #print('52-week high: {}'.format(fin_data['hi52']))
    #print('52-week low: {}'.format(fin_data['lo52']))
    #print('Volume: {}'.format(fin_data['vo']))
    #print('AvgVolume: {}'.format(fin_data['avvo']))