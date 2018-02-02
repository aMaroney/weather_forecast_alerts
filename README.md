# weather_forecast_alerts

A script that will send you weather alerts via email or sms. 
I used gmail to send the alerts from one email address to another.
THERE IS NO SECURITY IN THIS PROGRAM - Everything is saved and transmitted in plain text.
Adding security is not hard with the smtplib module. Simply add the it via the module and change the port.
You'll need to enter you own email/sms for the "sent_from" and "to" fields. 
The alerts are for following day and provide weather for the following times 6 AM, 9 AM, 6 PM, and 9 PM.
I chose the alerts for the next day and those times becuase that's what I find most useful most of the time.
I didn't include my API key but you can easily register for one for free like I did.

My future plans for this script are to break it up into functions and host/run it on a serve. 
My longterm plan is to build this into a webapp.

Thanks for reading!
