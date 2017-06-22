from crontab import CronTab

user_cron = CronTab() #Don't load anything from any user crontab
#cmd = 'python ~/Desktop/getDailyAllData.py'
cmd = 'python ~/Desktop/getDailyAllData.py' #command waiting for execution


#creat a new cron job
job = user_cron.new(cmd, comment='This is for auto get data')

#setting the job's time restrictions
job.minute.every(1)
#job.minute.on(50)
#job.hour.on(14)
#job.hour.every(4)
#job.day.on(4, 5, 6)

#job.dow.on('SUN')
#job.dow.on('SUN', 'FRI')
#job.month.during('APR', 'NOV')
job.enable()

#writes content to crontab
#user_cron.write( 'output.tab' )
#print user_cron.render()
