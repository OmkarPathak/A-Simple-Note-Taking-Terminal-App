# A-Simple-Note-Taking-Terminal-App
A simple terminal note taking application using Python

[![Python](https://img.shields.io/badge/Python-3.6-brightgreen.svg)](http://www.python.org/download/) [![Travis](https://img.shields.io/travis/rust-lang/rust.svg)]()

[Omkar Pathak](http://www.omkarpathak.in),<br />
Pune, Maharashtra, India.<br />

# Requirements:

* For database connectivity, I have used `pymysql` Python module. This module is not a built-in and hence
you have to download it fromm the PyPI. Execute the following command to install pymysql:<br />
`pip3 install pymysql`

* For sending emails you will need the built-in smtplib

* For scheduling emails, you will need to assign the schedule using Crontabs. You can do it manually, but I had used Python-Crontab module to do the job. You can install by:<br />
`pip3 install python-crontab`
