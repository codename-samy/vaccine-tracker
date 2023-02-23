import json
import datetime
import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"89d3-KKYZI7pX5M/kvDip5WNQEbDLEuc"',
    'origin': 'https://www.cowin.gov.in',
    'referer': 'https://www.cowin.gov.in/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
somedata = {}

while True:
    date = datetime.datetime.today().strftime('%d-%m-%Y')
    i = 0 
    for i in range(0,5):
        daten = (datetime.datetime.now() + datetime.timedelta(days=i)).strftime('%d-%m-%Y')
        if(daten in somedata.keys()):
            headers['if-none-match'] = somedata[daten]
        resp = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=312&date='+daten,headers=headers)
        if (resp.status_code == 200):
            jsonval = json.loads(resp.text)
            length = len(jsonval['centers'])
            for i in range(0, length-1):
                if ((int(jsonval['centers'][i]['sessions'][0]['min_age_limit']) == 18) and (int(jsonval['centers'][i]['sessions'][0]['available_capacity']) != 0)):
                    print (jsonval['centers'][i]['name'])
                #else:
                    #print('no data')
            newtag = resp.headers['ETag']
            if(daten in somedata.keys()):
                somedata.update(daten = newtag)
            else:
                somedata[daten] = newtag
       # else:
            #print('no new data 305')
        