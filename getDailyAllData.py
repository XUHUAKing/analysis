from pymongo import MongoClient
import tushare as ts
import pymongo
import json

client = MongoClient('localhost',27017) #'127.0.0.1'
db = client['stock']

dailyData = ts.get_today_all()
if not dailyData.empty:
    #    dD_dict = df[['code', 'name']] #only get code && name
    dD_dict = dailyData.to_dict('records')
    db.instrumentDailyData.insert_many(dD_dict)


#df = ts.get_tick_data('600848', date = '2014-12-22')
#client.king.hello.insert(json.loads(df.to_json(orient='records')))

print ('successfully import') 
#
#df = ts.get_hist_data('000875')
#
#df.to_csv('importdata')
#
#print('success')
