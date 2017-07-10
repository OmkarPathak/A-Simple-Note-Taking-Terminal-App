from crontab import CronTab

# Get the crontab file for specific user. Type your username here
my_cron = CronTab(user='omkarpathak')
# Creating a new cron job
job = my_cron.new(command='python /home/omkarpathak/Desktop/test.py')
# Run this job every minute
job.minute.every(1)
# Write this job in the cronjob file of this system
my_cron.write()
