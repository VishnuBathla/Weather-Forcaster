import requests
from datetime import datetime

api_key = '202e0e1d76b19428fd0bf15a53bff82d'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link) # accessing link
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15) # temperature in main dictionary convert it to celsius
weather_desc = api_data['weather'][0]['description'] # weather list 0th element dictionary detail about description
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p") # current date and time in string format

print ("-"*55)
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-"*55)

print ("Current temperature is: {:.2f} deg C".format(temp_city)) # only upto 2 decimal values
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

print("="*55)


# making a list so that i can print the info to a txt 
txtlist = [temp_city , weather_desc , hmdt , wind_spd , date_time]
#using open() buit-in function to write to a text file
with open("textfile.txt" , mode= 'w' ,encoding= 'utf-8')as f :      #encoding = utf-8for linux and cp1252 for win
    f.write("-"*55+"\n")   
    f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    f.write("\n"+"-"*55+"\n")
    f.write("Current temperature is: {:.2f} deg C\n".format(txtlist[0]))
    
    f.write("{} {} \n".format("Current weather desc  :" ,txtlist[1]))
    f.write("{} {} {} \n".format("Current Humidity      :",txtlist[2],"%"))
    f.write("{} {} {} \n".format("Current wind speed    :",txtlist[3],"kmph"))
    f.write("="*55)