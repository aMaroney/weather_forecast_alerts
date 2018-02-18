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

    response = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=4167147&units=imperial&APPID=xxxx")

    bytes_orl_weather = response.content

    # bytes_orl_weather = b'{"cod":"200","message":0.0044,"cnt":38,"list":[{"dt":1518760800,"main":{"temp":62.85,"temp_min":62.85,"temp_max":63.05,"pressure":1034.29,"sea_level":1037.08,"grnd_level":1034.29,"humidity":95,"temp_kf":-0.11},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":20},"wind":{"speed":3.09,"deg":297.002},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-16 06:00:00"},{"dt":1518771600,"main":{"temp":59.18,"temp_min":59.18,"temp_max":59.31,"pressure":1033.57,"sea_level":1036.44,"grnd_level":1033.57,"humidity":94,"temp_kf":-0.08},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"02n"}],"clouds":{"all":8},"wind":{"speed":2.73,"deg":143.501},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-16 09:00:00"},{"dt":1518782400,"main":{"temp":57.6,"temp_min":57.6,"temp_max":57.66,"pressure":1033.96,"sea_level":1036.84,"grnd_level":1033.96,"humidity":93,"temp_kf":-0.04},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":3.04,"deg":158},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-16 12:00:00"},{"dt":1518793200,"main":{"temp":73.05,"temp_min":73.05,"temp_max":73.05,"pressure":1034.77,"sea_level":1037.6,"grnd_level":1034.77,"humidity":66,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":3.74,"deg":227.009},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-16 15:00:00"},{"dt":1518804000,"main":{"temp":79.05,"temp_min":79.05,"temp_max":79.05,"pressure":1033.09,"sea_level":1035.85,"grnd_level":1033.09,"humidity":64,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":6.73,"deg":281.501},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-16 18:00:00"},{"dt":1518814800,"main":{"temp":79.65,"temp_min":79.65,"temp_max":79.65,"pressure":1031.19,"sea_level":1034.01,"grnd_level":1031.19,"humidity":57,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":10.76,"deg":275.502},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-16 21:00:00"},{"dt":1518825600,"main":{"temp":73.56,"temp_min":73.56,"temp_max":73.56,"pressure":1032.25,"sea_level":1035.03,"grnd_level":1032.25,"humidity":58,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":8.61,"deg":269.003},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-17 00:00:00"},{"dt":1518836400,"main":{"temp":66.51,"temp_min":66.51,"temp_max":66.51,"pressure":1033.54,"sea_level":1036.3,"grnd_level":1033.54,"humidity":77,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":6.85,"deg":276.502},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-17 03:00:00"},{"dt":1518847200,"main":{"temp":61.51,"temp_min":61.51,"temp_max":61.51,"pressure":1033.13,"sea_level":1036.1,"grnd_level":1033.13,"humidity":97,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":0},"wind":{"speed":4.74,"deg":278.5},"rain":{"3h":0.005},"sys":{"pod":"n"},"dt_txt":"2018-02-17 06:00:00"},{"dt":1518858000,"main":{"temp":59.81,"temp_min":59.81,"temp_max":59.81,"pressure":1032.56,"sea_level":1035.49,"grnd_level":1032.56,"humidity":97,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":48},"wind":{"speed":3.56,"deg":279.001},"rain":{"3h":0.01},"sys":{"pod":"n"},"dt_txt":"2018-02-17 09:00:00"},{"dt":1518868800,"main":{"temp":60.75,"temp_min":60.75,"temp_max":60.75,"pressure":1033.34,"sea_level":1036.18,"grnd_level":1033.34,"humidity":99,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":88},"wind":{"speed":3.56,"deg":284},"rain":{"3h":0.1},"sys":{"pod":"n"},"dt_txt":"2018-02-17 12:00:00"},{"dt":1518879600,"main":{"temp":65.22,"temp_min":65.22,"temp_max":65.22,"pressure":1034.72,"sea_level":1037.54,"grnd_level":1034.72,"humidity":88,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":48},"wind":{"speed":2.15,"deg":84.501},"rain":{"3h":0.12},"sys":{"pod":"d"},"dt_txt":"2018-02-17 15:00:00"},{"dt":1518890400,"main":{"temp":76.64,"temp_min":76.64,"temp_max":76.64,"pressure":1033.18,"sea_level":1035.9,"grnd_level":1033.18,"humidity":69,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":3.83,"deg":185.503},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-17 18:00:00"},{"dt":1518901200,"main":{"temp":80.62,"temp_min":80.62,"temp_max":80.62,"pressure":1031.13,"sea_level":1033.92,"grnd_level":1031.13,"humidity":53,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":4.18,"deg":233},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-17 21:00:00"},{"dt":1518912000,"main":{"temp":75.89,"temp_min":75.89,"temp_max":75.89,"pressure":1031.81,"sea_level":1034.59,"grnd_level":1031.81,"humidity":59,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":92},"wind":{"speed":3.6,"deg":260.006},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-18 00:00:00"},{"dt":1518922800,"main":{"temp":72.09,"temp_min":72.09,"temp_max":72.09,"pressure":1033.08,"sea_level":1035.76,"grnd_level":1033.08,"humidity":63,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":32},"wind":{"speed":6.4,"deg":294.505},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-18 03:00:00"},{"dt":1518933600,"main":{"temp":63.82,"temp_min":63.82,"temp_max":63.82,"pressure":1032.63,"sea_level":1035.44,"grnd_level":1032.63,"humidity":81,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":4.38,"deg":296.518},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-18 06:00:00"},{"dt":1518944400,"main":{"temp":58.89,"temp_min":58.89,"temp_max":58.89,"pressure":1032.13,"sea_level":1035.06,"grnd_level":1032.13,"humidity":96,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":2.71,"deg":298.5},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-18 09:00:00"},{"dt":1518955200,"main":{"temp":55.99,"temp_min":55.99,"temp_max":55.99,"pressure":1033.33,"sea_level":1036.29,"grnd_level":1033.33,"humidity":96,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":12},"wind":{"speed":3.24,"deg":266.501},"rain":{"3h":0.01},"sys":{"pod":"n"},"dt_txt":"2018-02-18 12:00:00"},{"dt":1518966000,"main":{"temp":64.54,"temp_min":64.54,"temp_max":64.54,"pressure":1035.21,"sea_level":1038.03,"grnd_level":1035.21,"humidity":86,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":0},"wind":{"speed":4.16,"deg":297.001},"rain":{"3h":0.03},"sys":{"pod":"d"},"dt_txt":"2018-02-18 15:00:00"},{"dt":1518976800,"main":{"temp":76.5,"temp_min":76.5,"temp_max":76.5,"pressure":1033.77,"sea_level":1036.63,"grnd_level":1033.77,"humidity":63,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":3.6,"deg":315.501},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-18 18:00:00"},{"dt":1518987600,"main":{"temp":79.7,"temp_min":79.7,"temp_max":79.7,"pressure":1032.08,"sea_level":1034.87,"grnd_level":1032.08,"humidity":53,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":3.83,"deg":203.501},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-18 21:00:00"},{"dt":1518998400,"main":{"temp":72.62,"temp_min":72.62,"temp_max":72.62,"pressure":1032.62,"sea_level":1035.57,"grnd_level":1032.62,"humidity":66,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":36},"wind":{"speed":2.48,"deg":100.5},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-19 00:00:00"},{"dt":1519009200,"main":{"temp":72.65,"temp_min":72.65,"temp_max":72.65,"pressure":1033.8,"sea_level":1036.85,"grnd_level":1033.8,"humidity":61,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":48},"wind":{"speed":7.99,"deg":106.001},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-19 03:00:00"},{"dt":1519020000,"main":{"temp":68.15,"temp_min":68.15,"temp_max":68.15,"pressure":1034.09,"sea_level":1036.89,"grnd_level":1034.09,"humidity":81,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":9.42,"deg":127.001},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-19 06:00:00"},{"dt":1519030800,"main":{"temp":65.13,"temp_min":65.13,"temp_max":65.13,"pressure":1033.62,"sea_level":1036.58,"grnd_level":1033.62,"humidity":93,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":7.29,"deg":131.004},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-19 09:00:00"},{"dt":1519041600,"main":{"temp":60.83,"temp_min":60.83,"temp_max":60.83,"pressure":1034.48,"sea_level":1037.42,"grnd_level":1034.48,"humidity":93,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":2.93,"deg":110.505},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-19 12:00:00"},{"dt":1519052400,"main":{"temp":75.39,"temp_min":75.39,"temp_max":75.39,"pressure":1035.64,"sea_level":1038.57,"grnd_level":1035.64,"humidity":69,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":5.75,"deg":107.5},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-19 15:00:00"},{"dt":1519063200,"main":{"temp":76.54,"temp_min":76.54,"temp_max":76.54,"pressure":1034.69,"sea_level":1037.42,"grnd_level":1034.69,"humidity":73,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":12},"wind":{"speed":7.63,"deg":136.501},"rain":{"3h":0.43},"sys":{"pod":"d"},"dt_txt":"2018-02-19 18:00:00"},{"dt":1519074000,"main":{"temp":82.04,"temp_min":82.04,"temp_max":82.04,"pressure":1032.68,"sea_level":1035.51,"grnd_level":1032.68,"humidity":53,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":56},"wind":{"speed":9.1,"deg":110.504},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-19 21:00:00"},{"dt":1519084800,"main":{"temp":77.33,"temp_min":77.33,"temp_max":77.33,"pressure":1033.32,"sea_level":1036.1,"grnd_level":1033.32,"humidity":57,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":10.42,"deg":109.002},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-20 00:00:00"},{"dt":1519095600,"main":{"temp":71.75,"temp_min":71.75,"temp_max":71.75,"pressure":1034.72,"sea_level":1037.52,"grnd_level":1034.72,"humidity":79,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":11.54,"deg":121.501},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-20 03:00:00"},{"dt":1519106400,"main":{"temp":69.15,"temp_min":69.15,"temp_max":69.15,"pressure":1035.01,"sea_level":1037.82,"grnd_level":1035.01,"humidity":92,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":9.64,"deg":133.501},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-20 06:00:00"},{"dt":1519117200,"main":{"temp":67.93,"temp_min":67.93,"temp_max":67.93,"pressure":1034.69,"sea_level":1037.55,"grnd_level":1034.69,"humidity":95,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":7.96,"deg":131},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-20 09:00:00"},{"dt":1519128000,"main":{"temp":67.15,"temp_min":67.15,"temp_max":67.15,"pressure":1035.77,"sea_level":1038.64,"grnd_level":1035.77,"humidity":96,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":6.44,"deg":123.501},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-20 12:00:00"},{"dt":1519138800,"main":{"temp":74.71,"temp_min":74.71,"temp_max":74.71,"pressure":1037.36,"sea_level":1040.19,"grnd_level":1037.36,"humidity":80,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":12},"wind":{"speed":7.74,"deg":123.501},"rain":{"3h":0.1125},"sys":{"pod":"d"},"dt_txt":"2018-02-20 15:00:00"},{"dt":1519149600,"main":{"temp":82.98,"temp_min":82.98,"temp_max":82.98,"pressure":1035.91,"sea_level":1038.84,"grnd_level":1035.91,"humidity":61,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":76},"wind":{"speed":10.65,"deg":136.002},"rain":{"3h":0.0375},"sys":{"pod":"d"},"dt_txt":"2018-02-20 18:00:00"},{"dt":1519160400,"main":{"temp":80.4,"temp_min":80.4,"temp_max":80.4,"pressure":1034.86,"sea_level":1037.73,"grnd_level":1034.86,"humidity":66,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":92},"wind":{"speed":12.48,"deg":131.502},"rain":{"3h":0.475},"sys":{"pod":"d"},"dt_txt":"2018-02-20 21:00:00"}],"city":{"id":4167147,"name":"Orlando","coord":{"lat":28.5383,"lon":-81.3793},"country":"US"}}'


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
    website_text = body

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

    writing_email_text = website_text

    save_path = '/home/user/website'

    name_of_file = ("weather_for_website.txt")

    completeName = os.path.join(save_path, name_of_file)

    weather_email_text = open(completeName, 'w')
    weather_email_text.write(writing_email_text)
    weather_email_text.close()


send_email('email_user', 'email_password', 'to ')