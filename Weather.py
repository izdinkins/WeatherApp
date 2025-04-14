from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import os
from dotenv import load_dotenv

#api key information
load_dotenv()
api_key = os.getenv('OMW_API_KEY')

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)


def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="imani_python_weather_app")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result= obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")


    #weather
        #calls the api and saves the needed data into variables
        api="https://api.openweathermap.org/data/2.5/weather?q="+ city +f"&appid={api_key}"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind = json_data['wind']['speed']

#sets the information to the variables into the correct labels and textboxes
        temperature.config(text=(temp,"°"))
        c.config(text=(condition,"|", "FEELS","LIKE",temp,"°"))

        windLabel.config(text=wind)
        humidityLabel.config(text=humidity)
        descriptionLabel.config(text=description)
        pressureLabel.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry")










#search box
Search_image=PhotoImage(file="search.png")
myImage=Label(image=Search_image)
myImage.place(x=20,y=20)


textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=80,y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myImage_icon = Button(image=Search_icon,borderwidth=0,cursor="hand1",bg="#404040",command=getWeather)
myImage_icon.place(x=400,y=34)

#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myImage=Label(image=Frame_image)
frame_myImage.pack(padx=5,pady=5,side=BOTTOM)


#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)


#label
windHeader=Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
windHeader.place(x=120, y=400)

humidityHeader=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
humidityHeader.place(x=250,y=400)

descHeader=Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
descHeader.place(x=430, y=400)

pressureHeader=Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
pressureHeader.place(x=650, y=400)

temperature=Label(font=("arial",70,"bold"),fg="#ee666d")
temperature.place(x=400,y=150)
c=Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

windLabel=Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
windLabel.place(x=120, y=430)

humidityLabel=Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
humidityLabel.place(x=280, y=430)

descriptionLabel=Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
descriptionLabel.place(x=450, y=430)

pressureLabel=Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
pressureLabel.place(x=670, y=430)

root.mainloop()
