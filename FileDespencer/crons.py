from crontab import CronTab
cron = CronTab(user="ibergx00")
my_crom= CronTab(user=True)
job = cron.new(command='python3 File_dispencer.py')
job.hour.every(1)
## The job takes place on the 4th, 5th, and 6th day of the week.
# job.day.on(4, 5, 6)
cron.write()

