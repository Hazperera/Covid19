from datetime import datetime
import requests
import json


filter_date = "2020-05-01"
flags = open('data/flag.json','r',encoding='utf-8')
flags_data = json.load(flags)

def covid_data_filter(filter_date):
    covid_data = requests.get('https://thevirustracker.com/timeline/map-data.json')
    filter_data = []
    for elem in covid_data.json()['data']:
        olddate = elem["date"]
        newdate = datetime.strptime(olddate, "%m/%d/%y").date()
        if str(newdate) == filter_date:
            dd=elem["date"]
            dd=newdate
            cc = elem["countrycode"]
            ca = elem["cases"]
            de= elem["deaths"]
            re=elem["recovered"]
            try:
                elem['country'] = flags_data[elem["countrycode"]]
                elem['flag']=f"static/img/flags/{elem['countrycode'].lower()}.png"
            except Exception as e:
                print(e)
                elem['country']=None
                elem['flag'] =None

            filter_data.append(elem)
            # print("For the Date {} \nThe Country Code {} \nThe number of cases are {} \nThe number of deaths are {} \nThe number of recovery is {}  ".format(dd,cc,ca,de,re))
            # print ('\n')
        else:
            # print("date not found")
            # print(newdate)
            print(filter_date,newdate)
    return filter_data

# covid_data_filter(filter_date)

