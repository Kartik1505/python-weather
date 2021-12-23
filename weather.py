#571813e6fdf55669ffa63b804c89b297
#http://api.weatherapi.com/v1/current.json?key= 28c6a3c9b00f4defa0a55558213003&q=India&aqi=yes
from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
import requests
import json

root = Tk()
root.resizable(False, False)
#city
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
#13 label 


def live_location_weather():
    ip = requests.get('https://ipinfo.io/')
    data = ip.json()
    city1 = data['city']

    api_request = requests.get('http://api.weatherapi.com/v1/forecast.json?key= 28c6a3c9b00f4defa0a55558213003&q=' + city1 +' &aqi=yes&days= 10')
    api = json.loads(api_request.content)

    weather_condition, is_day = set_weather(api)
    display_image(weather_condition, is_day)

    return api

def get_weather(*args):

    api_request = requests.get('http://api.weatherapi.com/v1/forecast.json?key= 28c6a3c9b00f4defa0a55558213003&q=' + str(enter_city.get()) +' &aqi=yes&days= 10')
    api = json.loads(api_request.content)

    weather_condition, is_day = set_weather(api)
    display_image(weather_condition, is_day)

    return api

def set_weather(api):
    city1 = api['location']['name']
    weather_condition = api['current']['condition']['text']
    temp_today = api['current']['temp_c']
    temp_tomorrow = api['forecast']['forecastday'][0]['day']['maxtemp_c']
    sunrise_time = api['forecast']['forecastday'][1]['astro']['sunrise']
    sunset_time = api['forecast']['forecastday'][1]['astro']['sunset']
    time = api['location']['localtime'][11:13]
    is_day = api['current']['is_day']
    morning_weather_condition = api['forecast']['forecastday'][1]['hour'][6]['condition']['text']
    afternoon_weather_condition = api['forecast']['forecastday'][1]['hour'][13]['condition']['text']
    evening_weather_condition = api['forecast']['forecastday'][1]['hour'][18]['condition']['text']
    night_weather_condition = api['forecast']['forecastday'][1]['hour'][22]['condition']['text']
    morning_temp = api['forecast']['forecastday'][1]['hour'][6]['temp_c']
    afternoon_temp = api['forecast']['forecastday'][1]['hour'][13]['temp_c']
    evening_temp = api['forecast']['forecastday'][1]['hour'][18]['temp_c']
    night_temp = api['forecast']['forecastday'][1]['hour'][22]['temp_c']

    setforecast(city1, weather_condition,temp_today, temp_tomorrow, sunrise_time,sunset_time, time, morning_weather_condition,afternoon_weather_condition,evening_weather_condition,night_weather_condition, morning_temp, afternoon_temp, evening_temp, night_temp)
    return weather_condition, is_day

def getimage(logo):
    logo = ImageTk.PhotoImage(logo)
    logo_label = Label(frame2, image = logo, bg = '#339CFF')
    logo_label.image = logo
    logo_label.grid(column = 0, row = 1)

def display_image(weather_condition, is_day):
    if is_day == 1:
        print('day')
        if weather_condition == 'Sunny':
            logo = Image.open('D:\Icon\Weather Icon\sunny1.png')
            getimage(logo)

        elif weather_condition == 'Haze':
            logo = Image.open('D:\Icon\Weather Icon\Haze.png')
            getimage(logo)

        elif weather_condition == 'Partly cloudy':
            logo = Image.open('D:\Icon\Weather Icon\Partialy cloudy.png')
            getimage(logo)

        elif weather_condition == 'Overcast':
            logo = Image.open('D:\Icon\Weather Icon\overcast.png')
            getimage(logo)
        
        elif weather_condition == 'Moderate snow' or weather_condition == 'Snow' or weather_condition == 'Light snow':
            logo = Image.open('D:\Icon\Weather Icon\Moderate snow.png')
            getimage(logo)
        elif weather_condition == 'Cloudy':
            logo = Image.open('D:\Icon\Weather Icon\cloudy.png')
            getimage(logo)
        elif weather_condition == 'Light drizzle' or weather_condition == 'Light rain' or weather_condition == 'Light rain shower' or weather_condition == 'Moderate or heavy rain shower':
            logo = Image.open('D:\Icon\Weather Icon\lightdrizzle.png')
            getimage(logo)
        elif weather_condition == 'Mist':
            logo = Image.open('D:\Icon\Weather Icon\mist.png')
            getimage(logo)
        elif weather_condition == 'Patchy rain possible' or weather_condition == 'Patchy light drizzle':
            logo = Image.open('D:\Icon\Weather Icon\patchyrainpossible.png')
            getimage(logo)
        elif weather_condition == 'Blowing snow':
            logo = Image.open('D:\Icon\Weather Icon\snow1.png')
            getimage(logo)
        elif weather_condition == 'Blizzard':
            logo = Image.open('D:\Icon\Weather Icon\snowblizzard.png')
            getimage(logo)
        
        
    #night    
    else:    
        print('night')
        if weather_condition == 'Clear':
            logo = Image.open('D:\Icon\Weather Icon\clear.png')
            getimage(logo)
           
        elif weather_condition == 'Haze':
            logo = Image.open('D:\Icon\Weather Icon\Haze.png')
            getimage(logo)

        elif weather_condition == 'Partly cloudy':
            logo = Image.open('D:\Icon\Weather Icon\Partialy cloudy Night.png')
            getimage(logo)

        elif weather_condition == 'Overcast':
            logo = Image.open('D:\Icon\Weather Icon\overcast.png')
            getimage(logo)
        
        elif weather_condition == 'Moderate snow' or weather_condition == 'Snow' or weather_condition == 'Light snow':
            logo = Image.open('D:\Icon\Weather Icon\Moderate snow.png')
            getimage(logo)
        
        elif weather_condition == 'Light drizzle' or weather_condition == 'Light rain' or weather_condition == 'Light rain shower':
            logo = Image.open('D:\Icon\Weather Icon\lightdrizzle.png')
            getimage(logo)

        elif weather_condition == 'Patchy rain possible' or weather_condition == 'Patchy light drizzle':
            logo = Image.open('D:\Icon\Weather Icon\patchyrainpossible.png')
            getimage(logo)

        elif weather_condition == 'Mist':
            logo = Image.open('D:\Icon\Weather Icon\mist.png')
            getimage(logo)
        elif weather_condition == 'Blizzard':
            logo = Image.open('D:\Icon\Weather Icon\snowblizzard.png')
            getimage(logo)
        elif weather_condition == 'Cloudy':
            logo = Image.open('D:\Icon\Weather Icon\cloudynight.png')
            getimage(logo)

def on_click_hour():
    
    api = live_location_weather()

    city1 = api['location']['name']
    region = api['location']['region']
    country = api['location']['country']
    max_temp = api['forecast']['forecastday'][0]['day']['maxtemp_c']
    min_temp = api['forecast']['forecastday'][0]['day']['mintemp_c']
    sunrise_time = api['forecast']['forecastday'][1]['astro']['sunrise']
    sunset_time = api['forecast']['forecastday'][1]['astro']['sunset']
    moonrise_time = api['forecast']['forecastday'][1]['astro']['moonrise']
    moonset_time = api['forecast']['forecastday'][1]['astro']['moonset']
    phase = api['forecast']['forecastday'][1]['astro']['moon_phase']
    illum = api['forecast']['forecastday'][1]['astro']['moon_illumination']
    time = api['location']['localtime']
    
    top = Toplevel()
    top.resizable(0,0)

    frame1 = Frame(top, bg = '#339CFF')
    frame2 = Frame(top, bg = '#339CFF')
    frame3 = Frame(top, bg = '#339CFF')
    
    frame1.grid(column = 0, row = 0, sticky = 'nsew')
    frame2.grid(column = 0, row = 1, sticky = 'nsew')
    frame3.grid(column = 0, row = 2)

    label_city = Label(frame1, text = city1 + ' Weather' + ' , ' + region + ' , ' + country + '\t\t', bg = '#339CFF', font = ('roboto', 15, 'bold'), fg = 'white')
    time_city = Label(frame1, text = time, bg = '#339CFF', fg = 'white')
    label_city.grid(column = 0, row = 0, sticky = 'nsew')
    time_city.grid(column = 1, row = 0, sticky = 'nsew')

    max_temp_label0 = Label(frame2, text = 'Max   :  ' + str(max_temp) + '\t', bg = '#339CFF', fg = 'white')
    min_temp_label0 = Label(frame2, text = 'Min   : ' + str(min_temp)+ '\t', bg = '#339CFF', fg = 'white')
    sunrise_label0 =Label(frame2, text = 'Sunrise  : ' + str(sunrise_time)+ '\t', bg = '#339CFF', fg = 'white')
    sunset_label0 = Label(frame2, text = '\t' + 'Sunset    : '+ str(sunset_time)+ '\t', bg = '#339CFF', fg = 'white')
  

    moon_rise_label0 = Label(frame2, text = 'Moonrise  : ' + str(moonrise_time)+ '\t', bg = '#339CFF', fg = 'white')
    moonset_label0 = Label(frame2, text = 'Moonset  : ' + str(moonset_time)+ '\t', bg = '#339CFF', fg = 'white')
    phase_label0 =Label(frame2, text = 'Phase    : ' + str(phase)+ '\t', bg = '#339CFF', fg = 'white')
    illum_label0 = Label(frame2, text = 'Illum    : ' + str(illum)+ '\t', bg = '#339CFF', fg = 'white')

    max_temp_label0.grid(column = 0, row = 0, sticky = 'nsew')
    min_temp_label0.grid(column = 1, row = 0, sticky = 'nsew')
    sunrise_label0.grid(column = 2, row = 0, sticky = 'nsew')
    sunset_label0.grid(column = 3, row = 0, sticky = 'nsew')

    moon_rise_label0.grid(column = 0, row = 1, sticky = 'nsew')
    moonset_label0.grid(column = 1, row = 1, sticky = 'nsew')
    phase_label0.grid(column = 2, row = 1, sticky = 'nsew')
    illum_label0.grid(column = 3, row = 1, sticky = 'nsew')

    my_canvas = Canvas(frame3, width = 625, height = 300)
    my_canvas.grid(column = 0, row = 0, sticky = 'nsew')

    scrollbar = Scrollbar(frame3, orient = VERTICAL, command = my_canvas.yview)
    scrollbar.grid(column = 1, row =0, sticky = 'nsew')

    my_canvas.configure(yscrollcommand = scrollbar.set)
    my_canvas.bind('<Configure>', lambda e : my_canvas.configure(scrollregion = my_canvas.bbox('all')))

    sub_frame3 = Frame(my_canvas, width = 620, height = 300)
    my_canvas.create_window((0,0), window = sub_frame3)

    hours_frame = Frame(sub_frame3, background = '#339CFF')
    empty_frame = Frame(sub_frame3, background = '#339CFF')
    temp_frame = Frame(sub_frame3, background = '#339CFF')
    wind_frame = Frame(sub_frame3, background = '#339CFF')
    gust_frame = Frame(sub_frame3, background = '#339CFF')
    rain_frame = Frame(sub_frame3, background = '#339CFF')

    

    hour_label0 = Label(hours_frame, text = 'Hour', bg = 'gray', fg = 'white', padx = 35)
    empty_label0 = Label(empty_frame, text = 'cond.', bg = 'gray', fg = 'white', padx = 35)
    temp_label0 = Label(temp_frame, text = 'Temp', bg = 'gray', fg = 'white', padx = 35)
    wind_label0 = Label(wind_frame, text = 'Wind', bg = 'gray', fg = 'white', padx = 35)
    gust_label0 = Label(gust_frame, text = 'Gust', bg = 'gray', fg = 'white', padx = 35)
    rain_label0 = Label(rain_frame, text = 'Rain', bg = 'gray', fg = 'white', padx = 35)

    hour_label0.grid(column = 0, row = 0, sticky = 'nsew', padx  = 2)
    empty_label0.grid(column = 0, row = 0, sticky = 'nsew', padx = 2)
    temp_label0.grid(column = 0, row = 0, sticky = 'nsew', padx  = 2)
    wind_label0.grid(column = 0, row = 0, sticky = 'nsew', padx = 2)
    gust_label0.grid(column = 0, row = 0, sticky = 'nsew', padx = 2)
    rain_label0.grid(column = 0, row = 0, sticky = 'nsew', padx = 2) 
    
   
    for i in range(0, 24):
        hours = api['forecast']['forecastday'][1]['hour'][i]['time'][11:16]
        label1 = Label(hours_frame, text = hours, bg = '#339CFF', pady = 8)
        label1.grid(column = 0, sticky = 'nsew', pady = 2)
    
    for i in range(0, 24):
        is_day = api['forecast']['forecastday'][1]['hour'][i]['is_day']
        weather_condition = api['forecast']['forecastday'][1]['hour'][i]['condition']['text']
        
        def image1(logo):
            logo = ImageTk.PhotoImage(logo)
            logo_label = Label(empty_frame, image = logo, bg = '#339CFF')
            logo_label.image = logo
            logo_label.grid(column = 0, pady = 2)
            
        #day
        if is_day == 1:
            if weather_condition == 'Sunny':
                logo = Image.open('D:\Icon\Weather Icon\sunnyday.png')
                image1(logo)
            elif weather_condition == 'Partly cloudy':
                logo = Image.open('D:\Icon\Weather Icon\partialcloudydaysmall.png')
                image1(logo)
            elif weather_condition == 'Overcast':
                logo = Image.open('D:\Icon\Weather Icon\overcastsmall.png')
                image1(logo)
            elif weather_condition == 'Mist':
                logo = Image.open('D:\Icon\Weather Icon\mistsmall.png')
                image1(logo)
            elif weather_condition == 'Patchy rain possible' or weather_condition == 'Moderate rain at times' or weather_condition == 'Patchy light drizzle':
                logo = Image.open('D:\Icon\Weather Icon\patchrainpossiblesmallday.png')
                image1(logo)
            elif weather_condition == 'Fog':
                logo = Image.open('D:\Icon\Weather Icon\dayfogsmall.png')
                image1(logo)
            elif weather_condition == 'Moderate or heavy rain shower' or weather_condition == 'Light rain shower':
                logo = Image.open('D:\Icon\Weather Icon\moderateorheavyrainshower.png')
                image1(logo) 
            elif weather_condition == 'Blizzard':
                logo = Image.open('D:\Icon\Weather Icon\blizzardsmall.png')
                image1(logo)
                
        elif is_day == 0:
            if weather_condition == 'Clear':
                logo = Image.open('D:\Icon\Weather Icon\clearnight.png')
                image1(logo)
            
            elif weather_condition == 'Patchy heavy snow' or weather_condition == 'Heavy snow':
                logo = Image.open('D:\Icon\Weather Icon\patchyheavysnowsmall.png')
                image1(logo)
            
            elif weather_condition == 'Overcast':
                logo = Image.open('D:\Icon\Weather Icon\overcastsmall.png')
                image1(logo)

            elif weather_condition == 'Partly cloudy':
                logo = Image.open('D:\Icon\Weather Icon\partialycloudynightsmall.png')
                image1(logo)
            elif weather_condition == 'Mist':
                logo = Image.open('D:\Icon\Weather Icon\mistsmall.png')
                image1(logo)
            elif weather_condition == 'Patchy rain possible' or weather_condition == 'Moderate rain at times' or weather_condition == 'Light rain shower' or weather_condition == 'Moderate or heavy rain shower':
                logo = Image.open('D:\Icon\Weather Icon\patchyrainpossiblenightsmall.png')
                image1(logo)
            elif weather_condition == 'Fog':
                logo = Image.open('D:\Icon\Weather Icon\dayfogsmall.png')
                image1(logo)
            elif weather_condition == 'Moderate or heavy rain shower' or weather_condition == 'Torrential rain shower':
                logo = Image.open('D:\Icon\Weather Icon\moderateorheavyrainshower.png')
                image1(logo) 
            elif weather_condition == 'Cloudy':
                logo = Image.open('D:\Icon\Weather Icon\cloudynightsmall.png')
                image1(logo)
            elif weather_condition == 'Blizzard':
                logo = Image.open('D:\Icon\Weather Icon\blizzardsmall.png')
                image1(logo)
        
    
    
    for i in range(0, 24):
        temp1 = api['forecast']['forecastday'][1]['hour'][i]['temp_c']

        def temp(color):    
            label2 = Label(temp_frame, text = str(temp1) + ' km/h', bg = color , pady = 8)
            label2.grid(column = 0, sticky = 'nsew', pady = 2)
        
        if int(temp1) in range(0,25):
            color = '#C4EE36'
            temp(color)
        elif int(temp1) in range(25, 28):
            color = '#E9D97E'
            temp(color)
        elif int(temp1) in range(28, 34):
            color = '#F1C151'
            temp(color)
        elif int(temp1) in range(34, 37):
            color = '#E4AD2B'
            temp(color)
        elif int(temp1) in range(37, 40):
            color = '#F98B0F'
            temp(color)
    
    for i in range(0, 24):
        wind = api['forecast']['forecastday'][1]['hour'][i]['wind_kph']

        def wind1(color):   
            label3 = Label(wind_frame, text = str(wind) + ' km/h', bg = color, pady = 8)
            label3.grid(column = 0,sticky = 'nsew', pady = 2, padx = 2)
        
        if int(wind) in range(0, 11):
            color = '#9BF6F3'
            wind1(color) 
        elif int(wind) in range(11,14):
            color = '#A4F6E9' 
            wind1(color)
        elif int(wind) in range(14,19):
            color = '#80F9CC' 
            wind1(color)
        elif int(wind) in range(19,27):
            color = '#73F6AB' 
            wind1(color)
        
    
    for i in range(0,24):
        gust = api['forecast']['forecastday'][1]['hour'][i]['gust_kph']
        def gust1(color):   
            label4 = Label(gust_frame, text = str(gust) + ' km/h', bg = color, pady = 8)
            label4.grid(column = 0,sticky = 'nsew', pady = 2, padx = 2)

        if int(gust) in range(0, 11):
            color = '#9BF6F3'
            gust1(color) 
        elif int(gust) in range(11,14):
            color = '#A4F6E9' 
            gust1(color)
        elif int(gust) in range(14,19):
            color = '#80F9CC' 
            gust1(color)
        elif int(gust) in range(19,27):
            color = '#73F6AB' 
            gust1(color)

    
    for i in range(0,24):
        rain = api['forecast']['forecastday'][1]['hour'][i]['will_it_rain']

        def rain1(color): 
            label5 = Label(rain_frame, text = str(rain) + ' %', bg = color, pady = 8)
            label5.grid(column = 0, sticky = 'nsew', pady = 2)
        
        if int(rain) in range(0, 1):
            color = 'white'
            rain1(color)
        elif int(rain) in range(1, 67):
            color = '#DDF0F7'
            rain1(color)
        elif int(rain) in range(67, 76):
            color = '#6BD0F2'
            rain1(color)
        elif int(rain) in range(76, 90):
            color = '#4DCBF6'
            rain1(color)
        elif int(rain) in range(90, 101):
            color = '#2CBBEC'
            rain1(color)
        


    hours_frame.grid(column = 0, row = 0, sticky = 'nsew')
    empty_frame.grid(column = 1, row = 0, sticky = 'nsew')
    temp_frame.grid(column = 2, row = 0, sticky = 'nsew')
    wind_frame.grid(column = 3, row = 0, sticky = 'nsew')
    gust_frame.grid(column = 4, row = 0, sticky = 'nsew')
    rain_frame.grid(column = 5, row = 0, sticky = 'nsew')

#
def on_click_three_hour():
    api = get_weather()

    city1 = api['location']['name']
    region = api['location']['region']
    country = api['location']['country']
    max_temp = api['forecast']['forecastday'][0]['day']['maxtemp_c']
    min_temp = api['forecast']['forecastday'][0]['day']['mintemp_c']
    sunrise_time = api['forecast']['forecastday'][1]['astro']['sunrise']
    sunset_time = api['forecast']['forecastday'][1]['astro']['sunset']
    moonrise_time = api['forecast']['forecastday'][1]['astro']['moonrise']
    moonset_time = api['forecast']['forecastday'][1]['astro']['moonset']
    phase = api['forecast']['forecastday'][1]['astro']['moon_phase']
    illum = api['forecast']['forecastday'][1]['astro']['moon_illumination']
    time = api['location']['localtime']
    
    top = Toplevel()
    top.resizable(0,0)

    frame1 = Frame(top, bg = 'white')
    frame2 = Frame(top, bg = 'white')
    frame3 = Frame(top, bg = 'white')
    
    frame1.grid(column = 0, row = 0, sticky = 'nsew')
    frame2.grid(column = 0, row = 1, sticky = 'nsew')
    frame3.grid(column = 0, row = 2)

    label_city = Label(frame1, text = city1 + ' Weather' + ' , ' + region + ' , ' + country + '\t\t', bg = 'white', font = ('roboto', 15, 'bold'))
    time_city = Label(frame1, text = time, bg = 'white')
    label_city.grid(column = 0, row = 0, sticky = 'nsew')
    time_city.grid(column = 1, row = 0, sticky = 'nsew')

    max_temp_label0 = Label(frame2, text = 'Max   :  ' + str(max_temp) + '\t', bg = 'white')
    min_temp_label0 = Label(frame2, text = 'Min   : ' + str(min_temp)+ '\t', bg = 'white')
    sunrise_label0 =Label(frame2, text = 'Sunrise  : ' + str(sunrise_time)+ '\t', bg = 'white')
    sunset_label0 = Label(frame2, text = '\t' + 'Sunset    : '+ str(sunset_time)+ '\t', bg = 'white')
  

    moon_rise_label0 = Label(frame2, text = 'Moonrise  : ' + str(moonrise_time)+ '\t', bg = 'white')
    moonset_label0 = Label(frame2, text = 'Moonset  : ' + str(moonset_time)+ '\t', bg = 'white')
    phase_label0 =Label(frame2, text = 'Phase    : ' + str(phase)+ '\t', bg = 'white')
    illum_label0 = Label(frame2, text = 'Illum    : ' + str(illum)+ '\t', bg = 'white')

    max_temp_label0.grid(column = 0, row = 0, sticky = 'nsew')
    min_temp_label0.grid(column = 1, row = 0, sticky = 'nsew')
    sunrise_label0.grid(column = 2, row = 0, sticky = 'nsew')
    sunset_label0.grid(column = 3, row = 0, sticky = 'nsew')

    moon_rise_label0.grid(column = 0, row = 1, sticky = 'nsew')
    moonset_label0.grid(column = 1, row = 1, sticky = 'nsew')
    phase_label0.grid(column = 2, row = 1, sticky = 'nsew')
    illum_label0.grid(column = 3, row = 1, sticky = 'nsew')

    my_canvas = Canvas(frame3, width = 625, height = 300)
    my_canvas.grid(column = 0, row = 0, sticky = 'nsew')

    scrollbar = Scrollbar(frame3, orient = VERTICAL, command = my_canvas.yview)
    scrollbar.grid(column = 1, row =0, sticky = 'nsew')

    my_canvas.configure(yscrollcommand = scrollbar.set)
    my_canvas.bind('<Configure>', lambda e : my_canvas.configure(scrollregion = my_canvas.bbox('all')))

    sub_frame3 = Frame(my_canvas, width = 620, height = 300)
    my_canvas.create_window((0,0), window = sub_frame3)

    hours_frame = Frame(sub_frame3, background = 'white')
    empty_frame = Frame(sub_frame3, background = 'white')
    temp_frame = Frame(sub_frame3, background = 'white')
    wind_frame = Frame(sub_frame3, background = 'white')
    gust_frame = Frame(sub_frame3, background = 'white')
    rain_frame = Frame(sub_frame3, background = 'white')

    

    hour_label0 = Label(hours_frame, text = 'Hour', bg = 'gray', fg = 'white', padx = 35)
    empty_label0 = Label(empty_frame, text = 'cond.', bg = 'gray', fg = 'white', padx = 35)
    temp_label0 = Label(temp_frame, text = 'Temp', bg = 'gray', fg = 'white', padx = 35)
    wind_label0 = Label(wind_frame, text = 'Wind', bg = 'gray', fg = 'white', padx = 35)
    gust_label0 = Label(gust_frame, text = 'Gust', bg = 'gray', fg = 'white', padx = 35)
    rain_label0 = Label(rain_frame, text = 'Rain', bg = 'gray', fg = 'white', padx = 35)

    hour_label0.grid(column = 0, row = 0, sticky = 'nsew', padx  = 2)
    empty_label0.grid(column = 0, row = 0, sticky = 'nsew', padx = 2)
    temp_label0.grid(column = 0, row = 0, sticky = 'nsew', padx  = 2)
    wind_label0.grid(column = 0, row = 0, sticky = 'nsew', padx = 2)
    gust_label0.grid(column = 0, row = 0, sticky = 'nsew', padx = 2)
    rain_label0.grid(column = 0, row = 0, sticky = 'nsew', padx = 2) 
    
   
    for i in range(0, 24):
        if i % 3 == 0:
            hours = api['forecast']['forecastday'][1]['hour'][i]['time'][11:16]
            label1 = Label(hours_frame, text = hours, bg = 'white', pady = 8)
            label1.grid(column = 0, sticky = 'nsew', pady = 2)
        else:
            print('nothing hour')
        
    for i in range(0, 24):
        if i % 3 == 0:
            is_day = api['forecast']['forecastday'][1]['hour'][i]['is_day']
            weather_condition = api['forecast']['forecastday'][1]['hour'][i]['condition']['text']
        
            def image1(logo):
                logo = ImageTk.PhotoImage(logo)
                logo_label = Label(empty_frame, image = logo, bg = 'white')
                logo_label.image = logo
                logo_label.grid(column = 0, pady = 2)
            
        #day
            if is_day == 1:
                if weather_condition == 'Sunny':
                    logo = Image.open('D:\Icon\Weather Icon\sunnyday.png')
                    image1(logo)
                elif weather_condition == 'Partly cloudy':
                    logo = Image.open('D:\Icon\Weather Icon\partialcloudydaysmall.png')
                    image1(logo)
                elif weather_condition == 'Overcast':
                    logo = Image.open('D:\Icon\Weather Icon\overcastsmall.png')
                    image1(logo)
                elif weather_condition == 'Mist':
                    logo = Image.open('D:\Icon\Weather Icon\mistsmall.png')
                    image1(logo)
                elif weather_condition == 'Patchy rain possible' or weather_condition == 'Moderate rain at times' or weather_condition == 'Patchy light drizzle':
                    logo = Image.open('D:\Icon\Weather Icon\patchrainpossiblesmallday.png')
                    image1(logo)
                elif weather_condition == 'Fog':
                    logo = Image.open('D:\Icon\Weather Icon\dayfogsmall.png')
                    image1(logo)
                elif weather_condition == 'Moderate or heavy rain shower' or weather_condition == 'Light rain shower':
                    logo = Image.open('D:\Icon\Weather Icon\moderateorheavyrainshower.png')
                    image1(logo) 
                elif weather_condition == 'Blizzard':
                    logo = Image.open('D:\Icon\Weather Icon\blizzardsmall.png')
                    image1(logo)
                    
            elif is_day == 0:
                if weather_condition == 'Clear':
                    logo = Image.open('D:\Icon\Weather Icon\clearnight.png')
                    image1(logo)
                
                elif weather_condition == 'Patchy heavy snow' or weather_condition == 'Heavy snow':
                    logo = Image.open('D:\Icon\Weather Icon\patchyheavysnowsmall.png')
                    image1(logo)
                
                elif weather_condition == 'Overcast':
                    logo = Image.open('D:\Icon\Weather Icon\overcastsmall.png')
                    image1(logo)

                elif weather_condition == 'Partly cloudy':
                    logo = Image.open('D:\Icon\Weather Icon\partialycloudynightsmall.png')
                    image1(logo)
                elif weather_condition == 'Mist':
                    logo = Image.open('D:\Icon\Weather Icon\mistsmall.png')
                    image1(logo)
                elif weather_condition == 'Patchy rain possible' or weather_condition == 'Moderate rain at times' or weather_condition == 'Light rain shower' or weather_condition == 'Moderate or heavy rain shower':
                    logo = Image.open('D:\Icon\Weather Icon\patchyrainpossiblenightsmall.png')
                    image1(logo)
                elif weather_condition == 'Fog':
                    logo = Image.open('D:\Icon\Weather Icon\dayfogsmall.png')
                    image1(logo)
                elif weather_condition == 'Moderate or heavy rain shower' or weather_condition == 'Torrential rain shower':
                    logo = Image.open('D:\Icon\Weather Icon\moderateorheavyrainshower.png')
                    image1(logo) 
                elif weather_condition == 'Cloudy':
                    logo = Image.open('D:\Icon\Weather Icon\cloudynightsmall.png')
                    image1(logo)
                elif weather_condition == 'Blizzard':
                    logo = Image.open('D:\Icon\Weather Icon\blizzardsmall.png')
                    image1(logo)

        else:
            print('')
    
    
    for i in range(0, 24):
        if i % 3 == 0:
            temp1 = api['forecast']['forecastday'][1]['hour'][i]['temp_c']

            def temp(color):    
                label2 = Label(temp_frame, text = str(temp1) + ' km/h', bg = color , pady = 8)
                label2.grid(column = 0, sticky = 'nsew', pady = 2)
            
            if int(temp1) in range(0,25):
                color = '#C4EE36'
                temp(color)
            elif int(temp1) in range(25, 28):
                color = '#E9D97E'
                temp(color)
            elif int(temp1) in range(28, 34):
                color = '#F1C151'
                temp(color)
            elif int(temp1) in range(34, 37):
                color = '#E4AD2B'
                temp(color)
            elif int(temp1) in range(37, 40):
                color = '#F98B0F'
                temp(color)
        else:
            print('')
    
    for i in range(0, 24):
        if i % 3 == 0:
            wind = api['forecast']['forecastday'][1]['hour'][i]['wind_kph']

            def wind1(color):   
                label3 = Label(wind_frame, text = str(wind) + ' km/h', bg = color, pady = 8)
                label3.grid(column = 0,sticky = 'nsew', pady = 2, padx = 2)
            
            if int(wind) in range(0, 11):
                color = '#9BF6F3'
                wind1(color) 
            elif int(wind) in range(11,14):
                color = '#A4F6E9' 
                wind1(color)
            elif int(wind) in range(14,19):
                color = '#80F9CC' 
                wind1(color)
            elif int(wind) in range(19,27):
                color = '#73F6AB' 
                wind1(color)
        else:
            print('')    
    
    for i in range(0,24):
        if i % 3 == 0:
            gust = api['forecast']['forecastday'][1]['hour'][i]['gust_kph']
            def gust1(color):   
                label4 = Label(gust_frame, text = str(gust) + ' km/h', bg = color, pady = 8)
                label4.grid(column = 0,sticky = 'nsew', pady = 2, padx = 2)

            if int(gust) in range(0, 11):
                color = '#9BF6F3'
                gust1(color) 
            elif int(gust) in range(11,14):
                color = '#A4F6E9' 
                gust1(color)
            elif int(gust) in range(14,19):
                color = '#80F9CC' 
                gust1(color)
            elif int(gust) in range(19,27):
                color = '#73F6AB' 
                gust1(color)
        else:
            print('')
    
    for i in range(0,24):
        if i % 3 == 0:
            rain = api['forecast']['forecastday'][1]['hour'][i]['will_it_rain']

            def rain1(color): 
                label5 = Label(rain_frame, text = str(rain) + ' %', bg = color, pady = 8)
                label5.grid(column = 0, sticky = 'nsew', pady = 2)
            
            if int(rain) in range(0, 1):
                color = 'white'
                rain1(color)
            elif int(rain) in range(1, 67):
                color = '#DDF0F7'
                rain1(color)
            elif int(rain) in range(67, 76):
                color = '#6BD0F2'
                rain1(color)
            elif int(rain) in range(76, 90):
                color = '#4DCBF6'
                rain1(color)

            elif int(rain) in range(90, 101):
                color = '#2CBBEC'
                rain1(color)

        else:
            print('')     


    hours_frame.grid(column = 0, row = 0, sticky = 'nsew')
    empty_frame.grid(column = 1, row = 0, sticky = 'nsew')
    temp_frame.grid(column = 2, row = 0, sticky = 'nsew')
    wind_frame.grid(column = 3, row = 0, sticky = 'nsew')
    gust_frame.grid(column = 4, row = 0, sticky = 'nsew')
    rain_frame.grid(column = 5, row = 0, sticky = 'nsew')
#
def on_click_ten_days():
    pass


          
def setforecast(city1, weather_condition,temp_today, temp_tomorrow, sunrise_time,sunset_time, time, morning_weather_condition,afternoon_weather_condition,evening_weather_condition,night_weather_condition, morning_temp, afternoon_temp, evening_temp, night_temp):
 
    var1.set(city1)
    var2.set(weather_condition)
    var3.set(temp_today)

    #framee 2
    city_name = Label(frame2, textvariable = var1,font = ('public sans', 15,'bold'), bg = '#339CFF', fg = 'white')
    weather_cond_label = Label(frame2, textvariable = var2,font = ('public sans', 10, 'bold'), bg = '#339CFF', fg = 'white')
    today_temp_label = Label(frame2, textvariable = var3, font =('public sans', 11,'bold'), bg = '#339CFF', fg = 'white')
    
    #frame 6

    
    sun_label = Label(frame6, text = ' ', bg = '#339CFF', fg = 'white')
    sun_label.grid(column = 0,row  = 0)
    sun_label = Label(frame6, text = ' ', bg = '#339CFF',fg = 'white')
    sun_label.grid(column = 1,row  = 0)
    sun_label = Label(frame6, text = ' ', bg = '#339CFF',fg = 'white')
    sun_label.grid(column = 2,row  = 0)
    sun_label = Label(frame6, text = ' ', bg = '#339CFF',fg = 'white')
    sun_label.grid(column = 3,row  = 0)
    sun_label = Label(frame6, text = ' ', bg = '#339CFF',fg = 'white')
    sun_label.grid(column = 4,row  = 0)
    sun_label = Label(frame6, text = ' ', bg = '#339CFF',fg = 'white')
    sun_label.grid(column = 5,row  = 0)
    sun_label = Label(frame6, text = ' ', bg = '#339CFF',fg = 'white')
    sun_label.grid(column = 6,row  = 0)
    sun_label = Label(frame6, text = ' ', bg = '#339CFF',fg = 'white')
    sun_label.grid(column = 7,row  = 0)
    sun_label = Label(frame6, text = ' ', bg = '#339CFF',fg = 'white')
    sun_label.grid(column = 8,row  = 0)
    sun_label = Label(frame6, text = ' ', bg = '#339CFF',fg = 'white')
    sun_label.grid(column = 9,row  = 0)
    sun_label = Label(frame6, text = ' ', bg = '#339CFF',fg = 'white')
    sun_label.grid(column = 10,row  = 0)
    sun_label = Label(frame6, text = ' ', bg = '#339CFF',fg = 'white')
    sun_label.grid(column = 11,row  = 0)
    sun_label = Label(frame6, text = ' ', bg = '#339CFF',fg = 'white')
    sun_label.grid(column = 12,row  = 0)
    sun_label = Label(frame6, text = ' ', bg = '#339CFF',fg = 'white')
    sun_label.grid(column = 13,row  = 0)
    
    print(time)

    logo010 = Image.open('D:\Icon\Weather Icon\sunnyday.png')
    new_img = logo010.resize((15,15))
    logo010 = ImageTk.PhotoImage(new_img)
    logo010.label = Label(frame6, image = logo010, bg = '#339CFF')
    logo010.image = logo010
    

    if time == '06':
        logo010.label.grid(column = 0, row = 0)
    elif time == '08':
        logo010.label.grid(column = 1, row = 0)
    elif time == '9':
        logo010.label.grid(column = 2, row = 0)
    elif time == '10':
        logo010.label.grid(column = 4, row = 0)
    elif time == '11':
        logo010.label.grid(column = 5, row = 0)
    elif time == '12':
        logo010.label.grid(column = 6, row = 0)
    elif time == '13':
        logo010.label.grid(column = 7, row = 0)
    elif time == '14':
        logo010.label.grid(column = 8, row = 0)
    elif time == '15':
        logo010.label.grid(column = 9, row = 0)
    elif time == '16':
        logo010.label.grid(column = 10, row = 0)
    elif time == '17':
        logo010.label.grid(column = 11, row = 0)
    elif time == '18':
        logo010.label.grid(column = 12, row = 0)
    else:
        logo010.label.grid(column = 13, row = 0)
    

    #frame3
    sunrise_time_label = Label(frame3, text = 'Sunrise'+'\t\t\t'+'\n' + sunrise_time + '\t\t', bg = '#339CFF', fg = 'white', font = ('public sans', 8,'bold'))
    sunset_time_label = Label(frame3, text = 'Sunset  ' +'\n'+ sunset_time, bg = '#339CFF', fg = 'white', font = ('public sans', 8,'bold'))

    #frame4
    morning_label = Label(frame4, text = 'Morning', bg = '#339CFF', fg = 'white',font = ('public sans', 8,'bold'))
    afternoon_label = Label(frame4, text = 'Afterno.', bg = '#339CFF', fg = 'white',font = ('public sans', 8,'bold'))
    evening_label = Label(frame4, text = 'Evening', bg = '#339CFF', fg = 'white',font = ('public sans', 8,'bold'))
    night_label = Label(frame4, text = 'Night', bg = '#339CFF', fg = 'white',font = ('public sans', 8,'bold'))

    #frame5
    hourly_button1 = Button(frame5, text = 'Hourly', bg = '#1b6ec2', fg = '#fff',font = ('public sans', 8, 'bold') ,padx = 5, pady = 5, command = on_click_hour)
    three_hourly_button1 = Button(frame5, text = '3 Hourly', bg = '#1b6ec2', fg = '#fff',font = ('public sans', 8, 'bold') ,padx = 5, pady = 5, command = on_click_three_hour)
    live_button1 = Button(frame5, text = 'Live', bg = '#1b6ec2', fg = '#fff',font = ('public sans', 8, 'bold') ,padx = 10, pady = 5, command = live_location_weather)
    

    
    #frame2 grid
    city_name.grid(column = 0, row = 0)  
    weather_cond_label.grid(column =0, row = 2)
    today_temp_label.grid(column =0 ,row =3)
   
    
    #frame3 grid
    sunrise_time_label.grid(column = 0, row = 0)
    sunset_time_label.grid(column = 1, row = 0)
    
    #frame4 gird
    morning_label.grid(column = 0, row = 0)
    afternoon_label.grid(column = 1, row = 0)
    evening_label.grid(column = 2, row = 0)
    night_label.grid(column = 3, row = 0, padx = 8)
    
    #frame5 grid
    hourly_button1.grid(column = 0, row = 0, padx = 5, pady = 5)
    three_hourly_button1.grid(column = 1, row = 0, padx =5 , pady =5)
    live_button1.grid(column = 2, row = 0, padx = 5, pady = 5)

    #frame5 data
    def image(logo):
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(frame4, image = logo,bg = '#339CFF')
        logo_label.image = logo
        logo_label.grid(column = 0, row = 1)
    
    def image1(logo):
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(frame4, image = logo, bg = '#339CFF')
        logo_label.image = logo
        logo_label.grid(column = 1, row = 1)
    
    def image2(logo):
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(frame4, image = logo, bg = '#339CFF')
        logo_label.image = logo
        logo_label.grid(column = 2, row = 1)

    def image3(logo):
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(frame4, image = logo, bg = '#339CFF')
        logo_label.image = logo
        logo_label.grid(column = 3, row = 1)

   #6131822
    #morning
    if morning_weather_condition == 'Sunny':
        logo = Image.open('D:\Icon\Weather Icon\sunnyday.png')
        image(logo)
    elif morning_weather_condition == 'Partly cloudy':
        logo = Image.open('D:\Icon\Weather Icon\partialcloudydaysmall.png')
        image(logo)
    elif morning_weather_condition == 'Overcast':
        logo = Image.open('D:\Icon\Weather Icon\overcastsmall.png')
        image(logo)
    elif morning_weather_condition == 'Mist':
        logo = Image.open('D:\Icon\Weather Icon\mistsmall.png')
        image(logo)
    elif morning_weather_condition == 'Patchy rain possible' or morning_weather_condition == 'Moderate rain at times' or morning_weather_condition == 'Patchy light drizzle':
        logo = Image.open('D:\Icon\Weather Icon\patchrainpossiblesmallday.png')
        image(logo)
    elif morning_weather_condition == 'Fog':
        logo = Image.open('D:\Icon\Weather Icon\dayfogsmall.png')
        image(logo)
    elif morning_weather_condition == 'Moderate or heavy rain shower' or morning_weather_condition == 'Light rain shower':
        logo = Image.open('D:\Icon\Weather Icon\moderateorheavyrainshower.png')
        image(logo) 
    elif morning_weather_condition == 'Blizzard':
        logo = Image.open('D:\Icon\Weather Icon\blizzardsmall.png')
        image(logo)
    else:
        logo =Image.open('D:\Icon\Weather Icon\sunnyday.png')
        getimage(logo)
        
    
    #afternoon
    if afternoon_weather_condition == 'Sunny':
        logo = Image.open('D:\Icon\Weather Icon\sunnyday.png')
        image1(logo)
    elif afternoon_weather_condition == 'Partly cloudy':
        logo = Image.open('D:\Icon\Weather Icon\partialcloudydaysmall.png')
        image1(logo)
    elif afternoon_weather_condition == 'Overcast':
        logo = Image.open('D:\Icon\Weather Icon\overcastsmall.png')
        image1(logo)
    elif afternoon_weather_condition == 'Mist':
        logo = Image.open('D:\Icon\Weather Icon\mistsmall.png')
        image1(logo)
    elif afternoon_weather_condition == 'Patchy rain possible' or afternoon_weather_condition == 'Moderate rain at times' or afternoon_weather_condition == 'Patchy light drizzle':
        logo = Image.open('D:\Icon\Weather Icon\patchrainpossiblesmallday.png')
        image1(logo)
    elif afternoon_weather_condition == 'Fog':
        logo = Image.open('D:\Icon\Weather Icon\dayfogsmall.png')
        image1(logo)
    elif afternoon_weather_condition == 'Moderate or heavy rain shower' or afternoon_weather_condition == 'Light rain shower':
        logo = Image.open('D:\Icon\Weather Icon\moderateorheavyrainshower.png')
        image1(logo)
    elif afternoon_weather_condition == 'Blizzard':
        logo = Image.open('D:\Icon\Weather Icon\blizzardsmall.png')
        image1(logo)
    else:
        logo =Image.open('D:\Icon\Weather Icon\sunnyday.png')
        getimage(logo)
    
    #evenin
    if evening_weather_condition == 'Clear':
        logo = Image.open('D:\Icon\Weather Icon\clearnight.png')
        image2(logo)
    
    elif evening_weather_condition == 'Patchy heavy snow' or evening_weather_condition == 'Heavy snow':
        logo = Image.open('D:\Icon\Weather Icon\patchyheavysnowsmall.png')
        image2(logo)
    
    elif evening_weather_condition == 'Overcast':
        logo = Image.open('D:\Icon\Weather Icon\overcastsmall.png')
        image2(logo)

    elif evening_weather_condition == 'Partly cloudy':
        logo = Image.open('D:\Icon\Weather Icon\partialycloudynightsmall.png')
        image2(logo)
    elif evening_weather_condition == 'Mist':
        logo = Image.open('D:\Icon\Weather Icon\mistsmall.png')
        image2(logo)
    elif evening_weather_condition == 'Patchy rain possible' or evening_weather_condition == 'Moderate rain at times' or evening_weather_condition == 'Patchy light drizzle':
        logo = Image.open('D:\Icon\Weather Icon\patchyrainpossiblenightsmall.png')
        image2(logo)
    elif evening_weather_condition == 'Fog':
        logo = Image.open('D:\Icon\Weather Icon\dayfogsmall.png')
        image2(logo)
    elif evening_weather_condition == 'Moderate or heavy rain shower' or evening_weather_condition == 'Torrential rain shower':
        logo = Image.open('D:\Icon\Weather Icon\moderateorheavyrainshower.png')
        image2(logo) 
    elif evening_weather_condition == 'Cloudy':
        logo = Image.open('D:\Icon\Weather Icon\cloudynightsmall.png')
        image2(logo)
    elif evening_weather_condition == 'Blizzard':
        logo = Image.open('D:\Icon\Weather Icon\blizzardsmall.png')
        image2(logo)
    else:
        logo =Image.open('D:\Icon\Weather Icon\clearnight.png')
        getimage(logo)

    #night
    if night_weather_condition == 'Clear':
        logo = Image.open('D:\Icon\Weather Icon\clearnight.png')
        image3(logo)
    
    elif night_weather_condition == 'Patchy heavy snow' or night_weather_condition == 'Heavy snow':
        logo = Image.open('D:\Icon\Weather Icon\patchyheavysnowsmall.png')
        image3(logo)
    
    elif night_weather_condition == 'Overcast':
        logo = Image.open('D:\Icon\Weather Icon\overcastsmall.png')
        image3(logo)

    elif night_weather_condition == 'Partly cloudy':
        logo = Image.open('D:\Icon\Weather Icon\partialycloudynightsmall.png')
        image3(logo)
    elif night_weather_condition == 'Mist':
        logo = Image.open('D:\Icon\Weather Icon\mistsmall.png')
        image3(logo)
    elif night_weather_condition == 'Patchy rain possible' or night_weather_condition == 'Moderate rain at times':
        logo = Image.open('D:\Icon\Weather Icon\patchyrainpossiblenightsmall.png')
        image3(logo)
    elif night_weather_condition == 'Fog':
        logo = Image.open('D:\Icon\Weather Icon\dayfogsmall.png')
        image3(logo)
    elif night_weather_condition == 'Moderate or heavy rain shower' or night_weather_condition == 'Torrential rain shower':
        logo = Image.open('D:\Icon\Weather Icon\moderateorheavyrainshower.png')
        image3(logo) 
    elif night_weather_condition == 'Cloudy':
        logo = Image.open('D:\Icon\Weather Icon\cloudynightsmall.png')
        image3(logo)
    elif night_weather_condition == 'Blizzard':
        logo = Image.open('D:\Icon\Weather Icon\blizzardsmall.png')
        image3(logo)
    else:
        logo =Image.open('D:\Icon\Weather Icon\clearnight.png')
        getimage(logo)

    symbol = chr(176)
    def morning_tempreature(color):
        morning_temp_label = Label(frame4, text = str(morning_temp) + symbol + 'c', bg = color, font = ('public sans', 8,'bold'), padx = 5, pady = 2)
        morning_temp_label.grid(column = 0, row = 2, sticky = 'nsew', padx = 3, pady = 5)
    
    def afternoon_tempreature(color):
        afternoon_temp_label = Label(frame4, text = str(afternoon_temp) + symbol + 'c', bg = color,font = ('public sans', 8,'bold'), padx = 5, pady = 2)
        afternoon_temp_label.grid(column = 1, row = 2, sticky = 'nsew', padx = 3, pady =5)

    def evening_tempreature(color):
        evening_temp_label = Label(frame4, text = str(evening_temp) + symbol + 'c', bg = color,font = ('public sans', 8,'bold'), padx =5, pady = 3)
        evening_temp_label.grid(column = 2, row = 2, sticky = 'nsew', padx = 3, pady =5)
    
    def night_tempreature(color):
        night_temp_label = Label(frame4, text = str(night_temp) + symbol + 'c', bg = color,font = ('public sans', 8,'bold'), padx = 5, pady = 3)
        night_temp_label.grid(column = 3, row = 2, sticky = 'nsew', padx = 3, pady =5)

    #morning temp
    if int(morning_temp) in range(0,25):
        color = '#C4EE36'
        morning_tempreature(color)
    elif int(morning_temp) in range(25, 28):
        color = '#E9D97E'
        morning_tempreature(color)
    elif int(morning_temp) in range(28, 34):
        color = '#F1C151'
        morning_tempreature(color)
    elif int(morning_temp) in range(34, 37):
        color = '#E4AD2B'
        morning_tempreature(color)
    elif int(morning_temp) in range(37, 40):
        color = '#F98B0F'
        morning_tempreature(color)

    #afternoon
    if int(afternoon_temp) in range(0,25):
        color = '#C4EE36'
        afternoon_tempreature(color)
    elif int(afternoon_temp) in range(25, 28):
        color = '#E9D97E'
        afternoon_tempreature(color)
    elif int(afternoon_temp) in range(28, 34):
        color = '#F1C151'
        afternoon_tempreature(color)
    elif int(afternoon_temp) in range(34, 37):
        color = '#E4AD2B'
        afternoon_tempreature(color)
    elif int(afternoon_temp) in range(37, 40):
        color = '#F98B0F'
        afternoon_tempreature(color)  

    #evening
    if int(evening_temp) in range(0,25):
        color = '#C4EE36'
        evening_tempreature(color)
    elif int(evening_temp) in range(25, 28):
        color = '#E9D97E'
        evening_tempreature(color)
    elif int(evening_temp) in range(28, 34):
        color = '#F1C151'
        evening_tempreature(color)
    elif int(evening_temp) in range(34, 37):
        color = '#E4AD2B'
        evening_tempreature(color)
    elif int(evening_temp) in range(37, 40):
        color = '#F98B0F'
        evening_tempreature(color) 

    #night
    if int(night_temp) in range(0,25):
        color = '#C4EE36'
        night_tempreature(color)
    elif int(night_temp) in range(25, 28):
        color = '#E9D97E'
        night_tempreature(color)
    elif int(night_temp) in range(28, 34):
        color = '#F1C151'
        night_tempreature(color)
    elif int(night_temp) in range(34, 37):
        color = '#E4AD2B'
        night_tempreature(color)
    elif int(night_temp) in range(37, 40):
        color = '#F98B0F'
        night_tempreature(color)   



main_frame = Frame(root, background = '#339CFF')
main_frame.pack(side = LEFT)
frame1 = Frame(main_frame, background = '#339CFF')
frame2 = Frame(main_frame, background = '#339CFF')
frame3 = Frame(main_frame, background = '#339CFF')
frame4 = Frame(main_frame, background = '#339CFF')
frame5 = Frame(main_frame, background = '#339CFF')
frame6 = Frame(main_frame, background = '#339CFF')


left_frame = Frame(root)
left_frame.pack(side = RIGHT)

frame1.grid(column = 0 , row = 0)
frame2.grid(column = 0, row = 1)
frame6.grid(column = 0, row = 2)
frame3.grid(column = 0, row = 3)
frame4.grid(column = 0, row  =4)
frame5.grid(column = 0, row = 5)



#Add image to button
logo1 = Image.open('D:\Icon\Weather Icon\search.png')
new_img = logo1.resize((32,20))
image_test = ImageTk.PhotoImage(new_img)

#frame1 
enter_city = Entry(frame1, width = 30, bg= '#91BFEA')
button1 = Button(frame1, text = 'Enter',image = image_test, command = get_weather, borderwidth = 0, bg = '#339CFF')

#frame1 Grid
button1.grid(column = 1, row = 0)
enter_city.grid(column =0, row = 0, padx = 5, pady = 5)

#bind Enter Key
root.bind('<Return>', get_weather)

live_location_weather()

icon = PhotoImage(file = 'D:\Icon\Weather Icon\weathericon.png')
root.iconphoto(False, icon)
root.title('Weather')
root.mainloop()