import requests
from datetime import datetime
from tkinter import *

api_key = "XXXXXXXX" # Enter Your API Key here

def do():
    location=E1.get()
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
    api_link = requests.get(complete_api_link) # accessing link
    api_data = api_link.json()

    #create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15) # convert it to celsius
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print ("-"*60)
    print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print ("-"*60)

    print ("Current temperature is: {:.2f} deg C".format(temp_city))
    print ("Current weather desc  :",weather_desc)
    print ("Current Humidity      :",hmdt, '%')
    print ("Current wind speed    :",wind_spd ,'kmph')

    print("="*60)

    # making a list so that i can print the info to a txt 
    txtlist = [temp_city,weather_desc,hmdt,wind_spd,date_time]
    #using open() buit-in function to write to a text file
    with open("textfile.txt" , mode= 'w' ,encoding= 'utf-8') as f:
        # encoding = utf-8 for linux and cp1252 for win
        f.write("------------------------------------------------------------- \n ")   
        f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
        f.write("\n ------------------------------------------------------------- \n")
        f.write("Current temperature is: {:.2f} deg C\n".format(txtlist[0]))
    
        f.write("{},{} \n".format("Current weather desc  :" ,txtlist[1]))
        f.write("{},{},{} \n".format("Current Humidity      :",txtlist[2],"%"))
        f.write("{},{},{} \n".format("Current wind speed    :",txtlist[3],"kmph"))
        f.write("====================================================")
top = Tk()
top.geometry('240x240')

L1 = Label(top, text="Enter the city name: ")
L1.pack( side = LEFT)

E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)
# def helloCallBack():
#    tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Button(top, text ="Get Weather",command=do)
B.place(x=120,y=200)

top.mainloop()
