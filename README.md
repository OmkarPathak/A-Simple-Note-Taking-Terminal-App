# A-Simple-Note-Taking-Terminal-App
A simple terminal note taking application using Python

[![Python](https://img.shields.io/badge/Python-3.6-brightgreen.svg)](http://www.python.org/download/) [![Travis](https://img.shields.io/travis/rust-lang/rust.svg)]

# Features:

* Simple command line application.
* Easy to install and *very* easy to use.
* Written in simple Python. Even a beginner Python developer can contribute to this.
* MySQL Database used, so you can easily play with it.
* Minimum dependencies (Just need the [pymysql](https://github.com/OmkarPathak/A-Simple-Note-Taking-Terminal-App#requirements) and [CronTab](https://github.com/OmkarPathak/A-Simple-Note-Taking-Terminal-App#requirements) modules)

# Requirements:

* For database connectivity, I have used `pymysql` Python module. This module is not a built-in and hence
you have to download it from the PyPI. Execute the following command to install pymysql:<br />
`pip3 install pymysql`

* For sending emails you will need the built-in `smtplib`

* For scheduling emails, you will need to assign the schedule using Crontabs. You can do it manually, but I had used Python-Crontab module to do the job. You can install by:<br />
`pip3 install python-crontab`

* For sending mails via Python, you will first have to change Gmail settings to receive mails via Python. This can be done by visiting the following url and turning the option on: `https://myaccount.google.com/lesssecureapps?pli=1`

# Procedure:

1. First and the most important step is to create a database for storing our notes. I have used MySQL due to its simplicity, but you can use any database you are comfortable. Just ensure to change the code accordingly. For creating our table, first make a database and then just copy and paste the following schema. This will create a table named **notes** in your database.

```mysql

CREATE TABLE `notes` (
`id` INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
`created` TIMESTAMP DEFAULT '0000-00-00 00:00:00',
`updated` TIMESTAMP DEFAULT now() ON UPDATE now(),
`note` VARCHAR(255),
`tags` VARCHAR(200)
);

```

2. If you want to use the email feature, you will have to run the `ScheduleEmail.py` file (You will have to run this file only at the beginning.). This file will ask you for your password of your Email ID (Password is saved in the file `password.txt` in the encrypted form). Also, this file will set the Cron Job to check the time after every single minute. When the date and time matches the one from the Schedules.txt file, you will get a reminder in the form of mail.

3. Else, you can simply run the `NoteTakingApp.py` file. This app provides following options:

| Options | Description |
| --- | --- |
| **-a**  *'New Note in Quotes'* *'Tag in Quotes'* | Adds a new note to the Database |
| **-r** | To read all the notes from the database |
| **-rc** | To read all the notes from the database (One by one) |
| **-u**  *[id]*  *'Updated Note in quotes'* | Updates an already stored note in the database based on id |
| **-d**  *[id]* | Deletes a specific note based on its id|
| **-ut**  *[id]*  *'Updated Tag in Quotes'*| Updates an already existing tag of a note|
| **-rt** | Read all the distinct tags from the database|
| **-st** *'Tag with which note is to be searched in Quotes'* | Search notes using tags|
| **--reminder**  *'Note in Quotes'*  *'Date(dd-mm-yyyy) [SPACE] Time(hh:ss)'* | This will set a reminder which will send an email at the specified time and day|


![](Results/NoteTakinAppResult.gif)


Built with ♥ by [`Omkar Pathak`](http://www.omkarpathak.in/)
