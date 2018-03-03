import requests
import smtplib
import os

def weather_data(key, state, city):
    fileName = 'http://api.wunderground.com/api/'+key+'/forecast/q/'+state+'/'+city+'.json'
    parsed_json = requests.get(fileName).json()
    return parsed_json

processing_date_info = weather_data('xxx', 'FL', 'Orlando')['forecast']['simpleforecast']['forecastday']
final_return = []
for i in range(len(processing_date_info)):
    date = processing_date_info[i]['date']
    day_weekday = date['weekday']
    day_monthname = date['monthname']
    day_of_the_week = date['day']
    year = date['year']
    day_temp = processing_date_info[i]
    day_temp_high = day_temp['high']['fahrenheit']
    day_temp_low = day_temp['low']['fahrenheit']
    day_one_final_msg = day_weekday + ', ' + day_monthname + ' ' + str(day_of_the_week) + ', ' + str(year) \
                        + ' High: ' + str(day_temp_high) + ' Low: ' + str(day_temp_low)
    final_return.append((day_one_final_msg))

def send_email(email_user, email_password, to):
    body = str(str(final_return[0]) + ' F' + '\n' + str(final_return[1]) + ' F' + '\n' + str(final_return[2]) + ' F' + '\n' + str(final_return[3]) + ' F')
    subject = 'Weather Forecast'
    email_text = 'Subject: {}\n\n{}'.format(subject, body)

    try:
        #server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, to, email_text)
        server.close()

        print('Email sent!')
    except Exception as e:
        print(e)

    save_path = 'xxx'
    name_of_file = ("xxx.txt")
    completeName = os.path.join(save_path, name_of_file)

    weather_email_text = open(completeName, 'w')
    weather_email_text.write(body)
    weather_email_text.close()

send_email('xxx', 'xxx', 'xxx')