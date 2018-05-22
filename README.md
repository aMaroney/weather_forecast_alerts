# weather_forecast_alerts

A script that will send you weather alerts via email or sms. 
I used gmail to send the alerts from one email address to another.
Adding security is not hard with the smtplib module. Simply add the module and change the port.
You'll need to enter you own email/sms. 

My live implementation of this script is hosted on PythonAnywhere.com and runs daily. My script inserts the weather and a unix timestamp into a MySQL database also hosted on PythonAnywhere.com. The script queries the database and formats the output and enails me the data every morning. 

Feel free to ask any questions or leave questions.
Thanks!
