import requests
import smtplib
import os
import sqlite3
import time
import datetime

def weather_data(key, state, city):
    fileName = 'http://api.wunderground.com/api/'+key+'/forecast/q/'+state+'/'+city+'.json'
    parsed_json = requests.get(fileName).json()
    return parsed_json

processing_date_info = weather_data('xxx', 'FL', 'Orlando')['forecast']['simpleforecast']['forecastday']

def create_table():
    conn = sqlite3.connect('xxx.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS xxx'
              '('
              'high REAL, low REAL, weekday TEXT, month TEXT, day REAL, year REAL, date_pulled TEXT'
              ')'
              )


def write_to_db():
    conn = sqlite3.connect('xxx.db')
    c = conn.cursor()
    for i in range(len(processing_date_info)):
        date = processing_date_info[i]['date']
        day_weekday = date['weekday']
        day_monthname = date['monthname']
        day_of_the_week = date['day']
        year = date['year']
        day_temp = processing_date_info[i]
        day_temp_high = day_temp['high']['fahrenheit']
        day_temp_low = day_temp['low']['fahrenheit']
        unix = time.time()
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        c.execute(
            "INSERT INTO xxx"
            "("
            "high, low, weekday, month, day, year, date_pulled"
            ")"
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (day_temp_high, day_temp_low, day_weekday, day_monthname, day_of_the_week, year, date))
        conn.commit()
    c.close()
    conn.close()

final_return = []

def pull_from_db():
    conn = sqlite3.connect('xxx.db')
    c = conn.cursor()
    c.execute('SELECT * FROM xxx')
    data = c.fetchall()
    len_data_total = len(data)-1
    len_data_minus_four = len(data)-4
    for i in range(len_data_minus_four, len_data_total):
        day_weekday = data[i][2]
        day_monthname = data[i][3]
        day_of_the_week = int(data[i][4])
        year = int(data[i][5])
        day_temp_high = data[i][0]
        day_temp_low = data[i][1]
        day_one_final_msg = day_weekday + ', ' + day_monthname + ' ' + str(day_of_the_week) + ', ' + str(year) \
                            + ' High: ' + str(day_temp_high) + ' Low: ' + str(day_temp_low)
        final_return.append((day_one_final_msg))
    c.close()
    conn.close()

def send_email(email_user, email_password, to):
    body = str(str(final_return[0]) + ' F' + '\n' + str(final_return[1]) + ' F' + '\n' + str(final_return[2]) + ' F' + '\n')
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

    print(email_text)

create_table()
write_to_db()
pull_from_db()

send_email('xxx', 'xxx', 'xxx')