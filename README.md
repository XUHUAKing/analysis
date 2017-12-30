# king_analysis

## @note: this branch is a fork of master for king

### "crontab-auto-data"
  Include the library for crontab so must create cron job files inside
  A template is shown inside "autoInstrumentDailyData.py", where "cmd = python ~/directory of your .py"
  More references:
1."crontab.py" file
2.https://pypi.python.org/pypi?name=python-crontab&:action=display 
3.http://blog.appliedinformaticsinc.com/managing-cron-jobs-with-python-crontab/

### "getDailyAllData.py"
  update today_all_data to database named "instrumentDailyData"
  More references:
1.https://github.com/waditu/tushare

## Initialize Mongodb
1) use docker image 

docker run -p 27017:27017 --name mongo -d mongo

// use mongo-express or robomongo

docker container run -p 27017:27017 --name mongodb -d mongo && docker container run -it -p 8081:8081 --name mongo_express --link mongodb:mongo -d mongo-express

2) python importdata/instrument.py
3) python importdata/instrumentDailyData.py
