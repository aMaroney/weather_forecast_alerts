import requests
import smtplib
import os
import pymysql
import time
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

data_from_db = []
final_return = []

def dbConnectionLocal(host, user, password, database):
    try:
        connection = pymysql.connect(host=host,user=user,password=password,database=database)
        return connection
    except Exception as e:
                print(e)

def weather_data(key, state, city):
    fileName = 'http://api.wunderground.com/api/'+key+'/forecast/q/'+state+'/'+city+'.json'
    parsed_json = requests.get(fileName).json()
    return parsed_json

processing_date_info = weather_data('key', 'state', 'city')['forecast']['simpleforecast']['forecastday']

def insertIntoTable():
    connection = dbConnectionLocal('local', 'root', 'password', 'db')
    cursor = connection.cursor()
    for i in range(len(processing_date_info)):
        date = processing_date_info[i]['date']
        day_weekday = date['weekday']
        day_monthname = date['monthname']
        day_of_the_week = date['day']
        year = date['year']
        day_temp = processing_date_info[i]
        day_temp_high = day_temp['high']['fahrenheit']
        day_temp_low = day_temp['low']['fahrenheit']
        weekday_month_day_year = day_weekday+', '+day_monthname+' '+str(day_of_the_week)+', '+str(year)
        unix_time = time.time()
        cursor.execute(
            "INSERT INTO table"
            "("
            "high, low, weekday_month_day_year, unix_pulled"
            ")"
            "VALUES (%s, %s, %s, %s)",
            (day_temp_high, day_temp_low, weekday_month_day_year, unix_time))
    connection.commit()
    connection.close()

def dbRemoteInsert():
    with sshtunnel.SSHTunnelForwarder(
            ('ssh'),
            ssh_username='user',
            ssh_password='password!',
            remote_bind_address=('address', 0000)
    )as tunnel:
        connection = pymysql.connect(
            user='user',
            password='password!',
            host='host',
            port=tunnel.local_bind_port,
            database='db',
        )
        cursor = connection.cursor()
        for i in range(len(processing_date_info)):
            date = processing_date_info[i]['date']
            day_weekday = date['weekday']
            day_monthname = date['monthname']
            day_of_the_week = date['day']
            year = date['year']
            day_temp = processing_date_info[i]
            day_temp_high = day_temp['high']['fahrenheit']
            day_temp_low = day_temp['low']['fahrenheit']
            weekday_month_day_year = day_weekday + ', ' + day_monthname + ' ' + str(day_of_the_week) + ', ' + str(year)
            unix_time = time.time()
            cursor.execute(
                "INSERT INTO table"
                "("
                "high, low, weekday_month_day_year, unix_pulled"
                ")"
                "VALUES (%s, %s, %s, %s)",
                (day_temp_high, day_temp_low, weekday_month_day_year, unix_time))
        connection.commit()
        connection.close()

def extractFromTable():
    connection = dbConnectionLocal('local', 'root', 'password', 'db')
    cursor = connection.cursor()
    unix_time = time.time()
    unix_less_2_minutes = unix_time - 120
    cursor.execute('SELECT high, low, weekday_month_day_year FROM table WHERE unix_pulled > %s',
                   (unix_less_2_minutes))
    table = cursor.fetchall()
    for row in table:
        data_from_db.append(row)
    connection.commit()
    connection.close()

def dbRemoteRead():
    with sshtunnel.SSHTunnelForwarder(
            ('ssh'),
            ssh_username='user',
            ssh_password='password!',
            remote_bind_address=('address', 0000)
    )as tunnel:
        connection = pymysql.connect(
            user='user',
            password='password!',
            host='host',
            port=tunnel.local_bind_port,
            database='db',
        )
        cursor = connection.cursor()
        unix_time = time.time()
        unix_less_2_minutes = unix_time - 120
        cursor.execute('SELECT high, low, weekday_month_day_year FROM table WHERE unix_pulled > %s', (unix_less_2_minutes))
        table = cursor.fetchall()
        for row in table:
            data_from_db.append(row)
        connection.commit()
        connection.close()

def format_message():
    for data_point in range(4):
        day_high = data_from_db[data_point][0]
        day_low = data_from_db[data_point][1]
        date =  data_from_db[data_point][2]
        final_msg = date + ' High: ' + str(day_high) + ' Low: ' + str(day_low)
        final_return.append((final_msg))

def send_email(email_user, email_password, to):
    body = str(str(final_return[0]) + ' F' + '\n' + str(final_return[1]) + ' F' + '\n' + str(final_return[2]) + ' F'+'\n'+ str(final_return[3]) + ' F' + '\n')
    subject = 'Weather Forecast'
    email_text = 'Subject: {}\n\n{}'.format(subject, body)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, to, email_text)
        server.close()

        print('Email sent!')
    except Exception as e:
        print(e)

    save_path = '/home/user/directory'

    name_of_file = ("weather.txt")

    completeName = os.path.join(save_path, name_of_file)

    weather_email_text = open(completeName, 'w')
    weather_email_text.write(body)
    weather_email_text.close()

dbRemoteInsert()
dbRemoteRead()
insertIntoTable()
extractFromTable()
format_message()
send_email('emailfrom@gmail.com', 'password', 'emailto@gmail.com')