# Real time weather API with CSV storage
import os
import csv
from datetime import datetime
import requests
FILENAME = "Weather_logs.csv"
API_KEY = "26b4af140336a4f67c57c7d71d77f0bd"
# KEYS ARE USUALLY HIDEN IN .env FILES BUT THAT IS FOR LATER
if not os.path.exists(FILENAME):
    with open(FILENAME,'w', newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City" ,"Temprature" ,"Condition"])
def log_weather():
    city = input("Give the name of the city : ")
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILENAME,'r', newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["date"] == date and row["City"].lower() == city.lower():
                print("Entry for this city is duplicate")
                return

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city }&appid={API_KEY}"
        # Accept the request
        response = requests.get(url)
        # convert into string
        data = response.json()
        # if have any error
        if response.status_code != 200:
            print(f"API ERRROR {data.get('message')}")
            
        temp = data['main']['temp']
        condition =  data['weather'][0]['main']
        with open(FILENAME,'a',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([date, city.title(), temp, condition])
            print(f"Logged : {temp} {condition} in {city.title()} on {date} ")
        
    except Exception as e :
        print("failed to make API call")

def view_logs():
    with open(FILENAME , "r" , newline= "", encoding= "utf-8") as f:
        reader = list(csv.reader(f))
        for row in reader[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

def main():
    while True:
        print("Real time weather logger")
        print("1. Add Weather log")
        print("2. View Weather log")

        choice = input("Choose the option : ")
        match choice :
            case "1": 
                log_weather()
            case "2": 
                view_logs()
            case _ : print("Choose Correct option")

if __name__ == "__main__":
    main()




