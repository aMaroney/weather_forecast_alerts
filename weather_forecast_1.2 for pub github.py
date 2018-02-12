import requests
import os
import datetime
import json
import smtplib


{
    "id": 4167147,
    "name": "Orlando",
    "country": "US",
    "coord": {
        "lon": -81.379242,
        "lat": 28.53834
    }
},

#Part 1 - Pull weather from API

parameter = { 'id': 4167147}

def pull_weather():

    response = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=4167147&units=imperial&APPID=xxxxx")

    bytes_orl_weather = response.content

    string_orl_weather = bytes_orl_weather.decode('utf-8')


    writing = string_orl_weather

    weather_raw = open('weather_testing.json', 'w')
    weather_raw.write(writing)
    weather_raw.close()

    return string_orl_weather


string_orl_weather = pull_weather()

#Part 2 Process JSON data from API

def tomorrows_date():
    return datetime.date.today() + datetime.timedelta(days=1)

def filter_one():
    weather_python_temp = json.loads(string_orl_weather)
    return weather_python_temp.get('list', 0)

length_of_list = len(filter_one())

def updating_date_time_list():
    date_time = []
    for i in range(length_of_list):
        date_time_append = filter_one()[i].get('dt_txt', 0)
        date_time.append(date_time_append)
    return date_time

def updating_temp_list():
    temp_list = []
    for i in range(length_of_list):
        filter_two = filter_one()[i]
        filter_three = filter_two.get('main', 0)
        temp_list_append = filter_three.get('temp', 0)
        temp_list.append(temp_list_append)
    return temp_list

def preparing_final_returns():
    final_return_list = []
    for i in range(length_of_list):
        if updating_date_time_list()[i] == str(tomorrows_date()) + ' 06:00:00':
            parsing_tomorrows_date_6am = updating_date_time_list()[i]
            converted_temp = updating_temp_list()[i]
            parsing_tomorrows_weather_6am = converted_temp
            final_6am_return = '06:00 AM' + ' - ' + str(updating_temp_list()[i+1])
            final_return_list.append(final_6am_return)

        if updating_date_time_list()[i] == str(tomorrows_date()) + ' 09:00:00':
            parsing_tomorrows_date_9am = updating_date_time_list()[i]
            converted_temp = str(updating_temp_list()[i])
            parsing_tomorrows_weather_9am = converted_temp
            final_9am_return = '09:00 AM' + ' - ' + str(updating_temp_list()[i+1])
            final_return_list.append(final_9am_return)

        if updating_date_time_list()[i] == str(tomorrows_date()) + ' 18:00:00':
            parsing_tomorrows_date_6pm = updating_date_time_list()[i]
            converted_temp = str(updating_temp_list()[i])
            parsing_tomorrows_weather_6pm = converted_temp
            final_6pm_return = '06:00 PM' + ' - ' + str(updating_temp_list()[i+1])
            final_return_list.append(final_6pm_return)

        if updating_date_time_list()[i] == str(tomorrows_date()) + ' 21:00:00':
            parsing_tomorrows_date_9pm = updating_date_time_list()[i]
            parsing_tomorrows_date_long_version = parsing_tomorrows_date_9pm[5:10]
            converted_temp = str(updating_temp_list()[i])
            parsing_tomorrows_weather_9pm = converted_temp
            final_9pm_return = '09:00 PM' + ' - ' + str(updating_temp_list()[i+1])
            final_return_list.append(final_9pm_return)


    return final_return_list

#########################################################
#Part 3 - Email weather information
def send_email(email_user, email_password, to):
    tomorrow_raw = datetime.datetime.today()
    tomorrow_day = tomorrow_raw.strftime('%A')
    today_day = str(datetime.date.today())[5:10]

    sent_from = email_user

    subject = "Weather for " + str(tomorrow_day)

    body = "Weather for "+ str(tomorrow_day + ' ' + today_day
                                     + '\n' + str(preparing_final_returns()[0]) + ' F'
                                     + '\n' + str(preparing_final_returns()[1]) + ' F'
                                     + '\n' + str(preparing_final_returns()[2]) + ' F'
                                     + '\n' + str(preparing_final_returns()[3]) + ' F')

    email_text = 'Subject: {}\n\n{}'.format(subject, body)

    try:
        #server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except Exception as e:
        print(e)


    print(email_text)

send_email('email_user', 'email_password', 'to ')