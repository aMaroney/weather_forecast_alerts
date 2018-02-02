import requests
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

parameter = { 'id': 2172797}

response = requests.get(
    "http://api.openweathermap.org/data/2.5/forecast?id=4167147&units=imperial&APPID=xxxxxxxxxx"
                        )

bytes_orl_weather = response.content

#bytes_orl_weather = b'{"cod":"200","message":0.0025,"cnt":40,"list":[{"dt":1517432400,"main":{"temp":73.69,"temp_min":67.12,"temp_max":73.69,"pressure":1033.91,"sea_level":1036.76,"grnd_level":1033.91,"humidity":55,"temp_kf":3.65},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":8.75,"deg":81.0004},"sys":{"pod":"d"},"dt_txt":"2018-01-31 21:00:00"},{"dt":1517443200,"main":{"temp":63.52,"temp_min":59.13,"temp_max":63.52,"pressure":1034.45,"sea_level":1037.41,"grnd_level":1034.45,"humidity":67,"temp_kf":2.43},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":7.4,"deg":80.5003},"sys":{"pod":"n"},"dt_txt":"2018-02-01 00:00:00"},{"dt":1517454000,"main":{"temp":53.35,"temp_min":51.15,"temp_max":53.35,"pressure":1034.73,"sea_level":1037.72,"grnd_level":1034.73,"humidity":94,"temp_kf":1.22},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":4.97,"deg":88.5105},"sys":{"pod":"n"},"dt_txt":"2018-02-01 03:00:00"},{"dt":1517464800,"main":{"temp":47.21,"temp_min":47.21,"temp_max":47.21,"pressure":1033.93,"sea_level":1036.85,"grnd_level":1033.93,"humidity":88,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":4.36,"deg":108.001},"sys":{"pod":"n"},"dt_txt":"2018-02-01 06:00:00"},{"dt":1517475600,"main":{"temp":45.4,"temp_min":45.4,"temp_max":45.4,"pressure":1033.23,"sea_level":1036.14,"grnd_level":1033.23,"humidity":86,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"02n"}],"clouds":{"all":8},"wind":{"speed":3.38,"deg":108.5},"sys":{"pod":"n"},"dt_txt":"2018-02-01 09:00:00"},{"dt":1517486400,"main":{"temp":43.96,"temp_min":43.96,"temp_max":43.96,"pressure":1034.08,"sea_level":1037.16,"grnd_level":1034.08,"humidity":86,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":2.71,"deg":81.5002},"sys":{"pod":"n"},"dt_txt":"2018-02-01 12:00:00"},{"dt":1517497200,"main":{"temp":63.62,"temp_min":63.62,"temp_max":63.62,"pressure":1035.53,"sea_level":1038.41,"grnd_level":1035.53,"humidity":66,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":3.96,"deg":87.5006},"sys":{"pod":"d"},"dt_txt":"2018-02-01 15:00:00"},{"dt":1517508000,"main":{"temp":72.65,"temp_min":72.65,"temp_max":72.65,"pressure":1033.71,"sea_level":1036.56,"grnd_level":1033.71,"humidity":59,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":4.63,"deg":157.501},"sys":{"pod":"d"},"dt_txt":"2018-02-01 18:00:00"},{"dt":1517518800,"main":{"temp":73.67,"temp_min":73.67,"temp_max":73.67,"pressure":1031.48,"sea_level":1034.33,"grnd_level":1031.48,"humidity":51,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":20},"wind":{"speed":4.74,"deg":167.003},"sys":{"pod":"d"},"dt_txt":"2018-02-01 21:00:00"},{"dt":1517529600,"main":{"temp":63.54,"temp_min":63.54,"temp_max":63.54,"pressure":1031.83,"sea_level":1034.69,"grnd_level":1031.83,"humidity":69,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"02n"}],"clouds":{"all":8},"wind":{"speed":4.18,"deg":153.504},"sys":{"pod":"n"},"dt_txt":"2018-02-02 00:00:00"},{"dt":1517540400,"main":{"temp":59.63,"temp_min":59.63,"temp_max":59.63,"pressure":1032.54,"sea_level":1035.56,"grnd_level":1032.54,"humidity":82,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":44},"wind":{"speed":6.96,"deg":138.002},"sys":{"pod":"n"},"dt_txt":"2018-02-02 03:00:00"},{"dt":1517551200,"main":{"temp":60.72,"temp_min":60.72,"temp_max":60.72,"pressure":1032.37,"sea_level":1035.28,"grnd_level":1032.37,"humidity":81,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":92},"wind":{"speed":3.6,"deg":162.001},"sys":{"pod":"n"},"dt_txt":"2018-02-02 06:00:00"},{"dt":1517562000,"main":{"temp":57.2,"temp_min":57.2,"temp_max":57.2,"pressure":1031.95,"sea_level":1034.89,"grnd_level":1031.95,"humidity":92,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":56},"wind":{"speed":2.57,"deg":271.501},"sys":{"pod":"n"},"dt_txt":"2018-02-02 09:00:00"},{"dt":1517572800,"main":{"temp":55.89,"temp_min":55.89,"temp_max":55.89,"pressure":1033.01,"sea_level":1035.94,"grnd_level":1033.01,"humidity":92,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":76},"wind":{"speed":2.71,"deg":309.003},"sys":{"pod":"n"},"dt_txt":"2018-02-02 12:00:00"},{"dt":1517583600,"main":{"temp":66.98,"temp_min":66.98,"temp_max":66.98,"pressure":1034.51,"sea_level":1037.38,"grnd_level":1034.51,"humidity":62,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":12},"wind":{"speed":3.83,"deg":295.002},"sys":{"pod":"d"},"dt_txt":"2018-02-02 15:00:00"},{"dt":1517594400,"main":{"temp":74.25,"temp_min":74.25,"temp_max":74.25,"pressure":1033.16,"sea_level":1035.98,"grnd_level":1033.16,"humidity":57,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"02d"}],"clouds":{"all":8},"wind":{"speed":7.4,"deg":319.003},"sys":{"pod":"d"},"dt_txt":"2018-02-02 18:00:00"},{"dt":1517605200,"main":{"temp":75.03,"temp_min":75.03,"temp_max":75.03,"pressure":1031.82,"sea_level":1034.76,"grnd_level":1031.82,"humidity":52,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":64},"wind":{"speed":8.01,"deg":335.501},"sys":{"pod":"d"},"dt_txt":"2018-02-02 21:00:00"},{"dt":1517616000,"main":{"temp":70.48,"temp_min":70.48,"temp_max":70.48,"pressure":1033.7,"sea_level":1036.75,"grnd_level":1033.7,"humidity":58,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":92},"wind":{"speed":8.97,"deg":17.5107},"sys":{"pod":"n"},"dt_txt":"2018-02-03 00:00:00"},{"dt":1517626800,"main":{"temp":61.69,"temp_min":61.69,"temp_max":61.69,"pressure":1036.05,"sea_level":1038.93,"grnd_level":1036.05,"humidity":68,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":8},"wind":{"speed":10.92,"deg":40},"rain":{"3h":0.1875},"sys":{"pod":"n"},"dt_txt":"2018-02-03 03:00:00"},{"dt":1517637600,"main":{"temp":55.37,"temp_min":55.37,"temp_max":55.37,"pressure":1035.88,"sea_level":1038.83,"grnd_level":1035.88,"humidity":56,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":10.65,"deg":25.0001},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-03 06:00:00"},{"dt":1517648400,"main":{"temp":52.85,"temp_min":52.85,"temp_max":52.85,"pressure":1034.92,"sea_level":1037.92,"grnd_level":1034.92,"humidity":76,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":8.9,"deg":17.5032},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-03 09:00:00"},{"dt":1517659200,"main":{"temp":53.05,"temp_min":53.05,"temp_max":53.05,"pressure":1035.11,"sea_level":1038.16,"grnd_level":1035.11,"humidity":87,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":20},"wind":{"speed":7.99,"deg":21.5024},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-02-03 12:00:00"},{"dt":1517670000,"main":{"temp":65.46,"temp_min":65.46,"temp_max":65.46,"pressure":1035.72,"sea_level":1038.66,"grnd_level":1035.72,"humidity":63,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":36},"wind":{"speed":6.96,"deg":47.0002},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-03 15:00:00"},{"dt":1517680800,"main":{"temp":71.59,"temp_min":71.59,"temp_max":71.59,"pressure":1034.11,"sea_level":1037.02,"grnd_level":1034.11,"humidity":55,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":64},"wind":{"speed":10,"deg":79.0048},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-03 18:00:00"},{"dt":1517691600,"main":{"temp":71.01,"temp_min":71.01,"temp_max":71.01,"pressure":1032.07,"sea_level":1034.98,"grnd_level":1032.07,"humidity":53,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":{"all":92},"wind":{"speed":10.09,"deg":86.0007},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-03 21:00:00"},{"dt":1517702400,"main":{"temp":66.57,"temp_min":66.57,"temp_max":66.57,"pressure":1032.51,"sea_level":1035.32,"grnd_level":1032.51,"humidity":64,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":9.98,"deg":91.5002},"rain":{"3h":0.0125},"sys":{"pod":"n"},"dt_txt":"2018-02-04 00:00:00"},{"dt":1517713200,"main":{"temp":63.63,"temp_min":63.63,"temp_max":63.63,"pressure":1032.5,"sea_level":1035.35,"grnd_level":1032.5,"humidity":80,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":100},"wind":{"speed":8.66,"deg":96.5005},"rain":{"3h":0.275},"sys":{"pod":"n"},"dt_txt":"2018-02-04 03:00:00"},{"dt":1517724000,"main":{"temp":61.13,"temp_min":61.13,"temp_max":61.13,"pressure":1031.42,"sea_level":1034.31,"grnd_level":1031.42,"humidity":97,"temp_kf":0},"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10n"}],"clouds":{"all":100},"wind":{"speed":5.75,"deg":80.0032},"rain":{"3h":3.325},"sys":{"pod":"n"},"dt_txt":"2018-02-04 06:00:00"},{"dt":1517734800,"main":{"temp":61.48,"temp_min":61.48,"temp_max":61.48,"pressure":1028.99,"sea_level":1031.86,"grnd_level":1028.99,"humidity":99,"temp_kf":0},"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":5.64,"deg":75.0014},"rain":{"3h":3.7125},"sys":{"pod":"n"},"dt_txt":"2018-02-04 09:00:00"},{"dt":1517745600,"main":{"temp":62.78,"temp_min":62.78,"temp_max":62.78,"pressure":1027.94,"sea_level":1030.74,"grnd_level":1027.94,"humidity":97,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":5.14,"deg":161.001},"rain":{"3h":1.125},"sys":{"pod":"n"},"dt_txt":"2018-02-04 12:00:00"},{"dt":1517756400,"main":{"temp":65.64,"temp_min":65.64,"temp_max":65.64,"pressure":1028.04,"sea_level":1030.94,"grnd_level":1028.04,"humidity":97,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":92},"wind":{"speed":8.63,"deg":172.002},"rain":{"3h":0.5},"sys":{"pod":"d"},"dt_txt":"2018-02-04 15:00:00"},{"dt":1517767200,"main":{"temp":68.86,"temp_min":68.86,"temp_max":68.86,"pressure":1025.94,"sea_level":1028.82,"grnd_level":1025.94,"humidity":96,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":92},"wind":{"speed":9.28,"deg":199},"rain":{"3h":0.875},"sys":{"pod":"d"},"dt_txt":"2018-02-04 18:00:00"},{"dt":1517778000,"main":{"temp":68.56,"temp_min":68.56,"temp_max":68.56,"pressure":1023.65,"sea_level":1026.46,"grnd_level":1023.65,"humidity":99,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":76},"wind":{"speed":10.89,"deg":223.502},"rain":{"3h":2.625},"sys":{"pod":"d"},"dt_txt":"2018-02-04 21:00:00"},{"dt":1517788800,"main":{"temp":65.83,"temp_min":65.83,"temp_max":65.83,"pressure":1024.33,"sea_level":1027.21,"grnd_level":1024.33,"humidity":95,"temp_kf":0},"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10n"}],"clouds":{"all":76},"wind":{"speed":13.09,"deg":228.503},"rain":{"3h":5.35},"sys":{"pod":"n"},"dt_txt":"2018-02-05 00:00:00"},{"dt":1517799600,"main":{"temp":66.33,"temp_min":66.33,"temp_max":66.33,"pressure":1025.63,"sea_level":1028.46,"grnd_level":1025.63,"humidity":97,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":10.02,"deg":255.505},"rain":{"3h":0.2125},"sys":{"pod":"n"},"dt_txt":"2018-02-05 03:00:00"},{"dt":1517810400,"main":{"temp":65.43,"temp_min":65.43,"temp_max":65.43,"pressure":1026.02,"sea_level":1028.94,"grnd_level":1026.02,"humidity":97,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":6.76,"deg":280},"rain":{"3h":0.5375},"sys":{"pod":"n"},"dt_txt":"2018-02-05 06:00:00"},{"dt":1517821200,"main":{"temp":61.02,"temp_min":61.02,"temp_max":61.02,"pressure":1026.53,"sea_level":1029.43,"grnd_level":1026.53,"humidity":100,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":5.95,"deg":355},"rain":{"3h":0.225},"sys":{"pod":"n"},"dt_txt":"2018-02-05 09:00:00"},{"dt":1517832000,"main":{"temp":55.52,"temp_min":55.52,"temp_max":55.52,"pressure":1029.19,"sea_level":1032.14,"grnd_level":1029.19,"humidity":100,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":8.1,"deg":356.001},"rain":{"3h":0.125},"sys":{"pod":"n"},"dt_txt":"2018-02-05 12:00:00"},{"dt":1517842800,"main":{"temp":56.07,"temp_min":56.07,"temp_max":56.07,"pressure":1032.05,"sea_level":1034.97,"grnd_level":1032.05,"humidity":100,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":20},"wind":{"speed":6.96,"deg":356.002},"rain":{"3h":0.037500000000001},"sys":{"pod":"d"},"dt_txt":"2018-02-05 15:00:00"},{"dt":1517853600,"main":{"temp":61.5,"temp_min":61.5,"temp_max":61.5,"pressure":1031.89,"sea_level":1034.73,"grnd_level":1031.89,"humidity":97,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"02d"}],"clouds":{"all":8},"wind":{"speed":7.54,"deg":351.5},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-02-05 18:00:00"}],"city":{"id":4167147,"name":"Orlando","coord":{"lat":28.5383,"lon":-81.3793},"country":"US"}}'


string_orl_weather = bytes_orl_weather.decode('utf-8')


writing = string_orl_weather

weather_raw = open('weather_testing.json', 'w')
weather_raw.write(writing)
weather_raw.close()

########################################################
#Part 2 Process JSON data from API

weather_raw = open('weather_testing.json', 'r')
weather_raw = weather_raw.read()
weather_python_temp = json.loads(weather_raw)


filter_one = (weather_python_temp.get('list', 0))


date_time = []
temp_max_list = []
temp_min_list = []
temp_list = []
converted_temp_list = []

length_of_list = len(filter_one)

for i in range(length_of_list):
    filter_two = filter_one[i]
    filter_three = filter_two.get('main', 0)
    date_time_append = filter_one[i].get('dt_txt', 0)
    date_time.append(date_time_append)
    temp_list_append = filter_three.get('temp', 0)
    temp_list.append(temp_list_append)

for i in range(length_of_list):
    converted_temp = str(((1.8 * (int(temp_list[i]) - 273)) + 32))
    converted_temp_list.append(converted_temp)

tomorrows_date = datetime.date.today() + datetime.timedelta(days=1)

for i in range(length_of_list):
    if date_time[i] == str(tomorrows_date) + ' 06:00:00':
        parsing_tomorrows_date_6am = date_time[i]
        converted_temp = str(temp_list[i])
        parsing_tomorrows_weather_6am = converted_temp
        final_6am_return = '06:00 AM' + ' - ' + str(temp_list[i])

    if date_time[i] == str(tomorrows_date) + ' 09:00:00':
        parsing_tomorrows_date_9am = date_time[i]
        converted_temp = str(temp_list[i])
        parsing_tomorrows_weather_9am = converted_temp
        final_9am_return = '09:00 PM' + ' - ' + str(temp_list[i])

    if date_time[i] == str(tomorrows_date) + ' 18:00:00':
        parsing_tomorrows_date_6pm = date_time[i]
        converted_temp = str(temp_list[i])
        parsing_tomorrows_weather_6pm = converted_temp
        final_6pm_return = '06:00 PM' + ' - ' + str(temp_list[i])

    if date_time[i] == str(tomorrows_date) + ' 21:00:00':
        parsing_tomorrows_date_9pm = date_time[i]
        parsing_tomorrows_date_long_version = parsing_tomorrows_date_9pm[5:10]
        converted_temp = str(temp_list[i])
        parsing_tomorrows_weather_9pm = converted_temp
        final_9pm_return = '09:00 PM' + ' - ' + str(temp_list[i])

#########################################################
#Part 3 - Email weather information

gmail_user = 'xxxxx'
gmail_password = 'xxxxx'


tomorrow_raw = datetime.datetime.today() + datetime.timedelta(days=1)
tomorrow_day = tomorrow_raw.strftime('%A')

weather_raw = open('weather_testing.json', 'r')

sent_from = 'xxxxx'

to = ['xxxxx']

subject = "Weather for " + str(tomorrow_day)






body = "Weather for "+ str(tomorrow_day + ' ' + parsing_tomorrows_date_long_version
                                 + '\n' + final_6am_return + ' F'
                                 + '\n' + final_9am_return + ' F'
                                 + '\n' + final_6pm_return + ' F'
                                 + '\n' + final_9pm_return + ' F')

email_text = 'Subject: {}\n\n{}'.format(subject, body)

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    #server.sendmail(sent_from, to, subject, email_text,)
    server.close()

    print('Email sent!')
except Exception as e:
    print(e)

print(email_text)

weather_raw.close()