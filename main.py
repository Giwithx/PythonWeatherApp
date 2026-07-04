import sys
import requests
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from requests import HTTPError, Request
from collections import defaultdict, Counter
from datetime import datetime


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__() # accessing the function of the QWidget using the super function
        self.title_label = QLabel("Weather App", self) # This will put a label on app
        self.city_input = QLineEdit(self) # This will put a line edit on the app
        self.get_weather_button = QPushButton("Get Weather", self)
        self.date_today = QLabel(self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.day_title = QLabel(self)
        self.day1_name = QLabel(self)
        self.day2_name = QLabel(self)
        self.day3_name = QLabel(self)
        self.day1_temp = QLabel(self)
        self.day2_temp = QLabel(self)
        self.day3_temp = QLabel(self)
        self.day1_emoji = QLabel(self)
        self.day2_emoji = QLabel(self)
        self.day3_emoji = QLabel(self)
        self.day1_description_label = QLabel(self)
        self.day2_description_label = QLabel(self)
        self.day3_description_label = QLabel(self)
        self.feels_like_label = QLabel(self)
        self.setWindowIcon(QIcon("icons/weather.png"))
        self.get_weather_button.setFocus()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.city_input.setPlaceholderText("Enter City Name")

        main_layout = QVBoxLayout() # This will organize what we put on the app

        city_layout = QVBoxLayout()
        city_layout.addWidget(self.title_label)
        city_layout.addWidget(self.city_input)
        city_layout.addWidget(self.get_weather_button)

        date_layout = QVBoxLayout()
        date_layout.addWidget(self.date_today)

        temperature_layout = QHBoxLayout()
        temperature_layout.addWidget(self.temperature_label)
        temperature_layout.addWidget(self.emoji_label)
        temperature_layout.addWidget(self.description_label)

        feels_like_layout = QVBoxLayout()
        feels_like_layout.addWidget(self.feels_like_label)

        day_forecast_title = QVBoxLayout()
        day_forecast_title.addWidget(self.day_title)

        day_layout_main = QHBoxLayout()

        day1_temp_layout = QVBoxLayout()
        day1_temp_layout.addWidget(self.day1_name)
        day1_temp_layout.addWidget(self.day1_emoji)
        day1_temp_layout.addWidget(self.day1_temp)
        day1_temp_layout.addWidget(self.day1_description_label)
        day2_temp_layout = QVBoxLayout()
        day2_temp_layout.addWidget(self.day2_name)
        day2_temp_layout.addWidget(self.day2_emoji)
        day2_temp_layout.addWidget(self.day2_temp)
        day2_temp_layout.addWidget(self.day2_description_label)
        day3_temp_layout = QVBoxLayout()
        day3_temp_layout.addWidget(self.day3_name)
        day3_temp_layout.addWidget(self.day3_emoji)
        day3_temp_layout.addWidget(self.day3_temp)
        day3_temp_layout.addWidget(self.day3_description_label)

        day_layout_main.addLayout(day1_temp_layout)
        day_layout_main.addLayout(day2_temp_layout)
        day_layout_main.addLayout(day3_temp_layout)

        main_layout.addLayout(city_layout)
        main_layout.addLayout(date_layout)
        main_layout.addLayout(temperature_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(feels_like_layout)
        main_layout.addSpacing(30)
        main_layout.addLayout(day_forecast_title)
        main_layout.addSpacing(30)
        main_layout.addLayout(day_layout_main)

        self.setLayout(main_layout) # This will set all what we declare in our add widget

        self.title_label.setAlignment(Qt.AlignCenter) # This will align all widget in the app to center
        self.city_input.setAlignment(Qt.AlignCenter)
        self.date_today.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.feels_like_label.setAlignment(Qt.AlignCenter)
        self.day_title.setAlignment(Qt.AlignCenter)
        self.day1_temp.setAlignment(Qt.AlignCenter)
        self.day1_emoji.setAlignment(Qt.AlignCenter)
        self.day1_description_label.setAlignment(Qt.AlignCenter)
        self.day2_temp.setAlignment(Qt.AlignCenter)
        self.day2_emoji.setAlignment(Qt.AlignCenter)
        self.day2_description_label.setAlignment(Qt.AlignCenter)
        self.day3_temp.setAlignment(Qt.AlignCenter)
        self.day3_emoji.setAlignment(Qt.AlignCenter)
        self.day3_description_label.setAlignment(Qt.AlignCenter)
        self.day1_name.setAlignment(Qt.AlignCenter)
        self.day2_name.setAlignment(Qt.AlignCenter)
        self.day3_name.setAlignment(Qt.AlignCenter)

        self.title_label.setObjectName("title_label") # This is declaration for the setStyleSheet
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.date_today.setObjectName("date_today")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.feels_like_label.setObjectName("feels_like_label")
        self.day_title.setObjectName("day_title")
        self.day1_name.setObjectName("day1_name")
        self.day1_temp.setObjectName("day1_temp")
        self.day1_emoji.setObjectName("day1_emoji")
        self.day1_description_label.setObjectName("day1_description_label")
        self.day2_name.setObjectName("day2_name")
        self.day2_temp.setObjectName("day2_temp")
        self.day2_emoji.setObjectName("day2_emoji")
        self.day2_description_label.setObjectName("day2_description_label")
        self.day3_name.setObjectName("day3_name")
        self.day3_temp.setObjectName("day3_temp")
        self.day3_emoji.setObjectName("day3_emoji")
        self.day3_description_label.setObjectName("day3_description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#title_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 45px;
            }
            QLabel#emoji_label{
                font-size: 80px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 30px;
            }
            QLabel#day1_temp, QLabel#day2_temp, QLabel#day3_temp, QLabel#day_title{
                font-size: 30px;
                font-family: calibri;
            }
            QLabel#day1_description_label,  QLabel#day2_description_label,  QLabel#day3_description_label{
                font-size: 15px;
                font-family: calibri;
            }
            QLabel#day1_name, QLabel#day2_name, QLabel#day3_name{
                font-size: 20px;
                font-family: calibri;
            }
            QLabel#date_today{
                font-size: 26px;
                font-family: calibri;
                color: gray;
            }
            QLabel#feels_like_label{
                font-size: 26px;
                font-family: calibri;
                color: gray;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather) # This will connect the function of clicked to our method of get_weather

    def get_weather(self):

        api_key = "d5585dc1641641f32c1ea51cb47ec58d" # This is the key from the weather API
        city = self.city_input.text() # this will get what we input in the city_input QLineEdit
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" # This is the url from the API website

        url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

        try:
            response = requests.get(url) # This will get the request from the URL
            forecast_response = requests.get(url_forecast)

            response.raise_for_status() # This will raise an exception if there's an error
            forecast_response.raise_for_status()

            weather_data = response.json() #convert the response to json format
            forecast_data = forecast_response.json()

            if weather_data["cod"] == 200: # 200 means okay connection and will display the weather data
                self.display_weather(weather_data, forecast_data) # passing to the method of display data to display the data on the app

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request: Please check your input") # This will call the display error method and will output on the app
                case 401:
                    self.display_error("Unauthorized: Invalid API Key")
                case 403:
                    self.display_error("Forbidden: Access is denied")
                case 404:
                    self.display_error("Not Found: City not found")
                case 500:
                    self.display_error("Internal Server Error: Please try again later")
                case 502:
                    self.display_error("Bad gateway: Invalid response from the server")
                case 503:
                    self.display_error("Service Unavailable: Server is down")
                case 504:
                    self.display_error("Gateway Timeout: No response from the server")
                case _:
                    self.display_error(f"HTTP error occurred: {http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error: Check your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error: The request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects: Check the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error: {req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;") # This will set the font size to smaller since the error code is big
        self.temperature_label.setText(message)
        self.emoji_label.clear() # This will clear the emoji and the description label to clearly print only the temperature label
        self.description_label.clear()
        self.day1_temp.clear()
        self.day2_temp.clear()
        self.day3_temp.clear()
        self.day_title.clear()
        self.day1_emoji.clear()
        self.day2_emoji.clear()
        self.day3_emoji.clear()
        self.day1_description_label.clear()
        self.day2_description_label.clear()
        self.day3_description_label.clear()
        self.day1_name.clear()
        self.day2_name.clear()
        self.day3_name.clear()
        self.date_today.clear()

    def display_weather(self, data, forecast_data):
        self.temperature_label.setStyleSheet("font-size: 75px;") # Back the font size to original
        temperature_k = data["main"]["temp"] # This will access the dictionary of main and accessing the temp
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        weather_description = data["weather"][0]["description"] # This will access the list of weather in the index of 0 and the value of description
        weather_id = data["weather"][0]["id"] # This will access the id which is essential for the weather emoji
        feels_like = data["main"]["feels_like"] - 273.15

        next_3days, forecast_by_day = self.get_weather_3days(forecast_data) # this will pass the value of the forecast data to the method of get_weather_3days and that will return us a value

        forecast_summary = []

        for date in next_3days: # for every date (item) in next_3days list []
            day_name = datetime.strptime(date, "%Y-%m-%d").strftime("%a")
            forecast = forecast_by_day[date] # declare that the forecast is accessing the dictionary of forecast_by_day and indexing to its every key values in the dict e.g. forecast_by_day['2026-07-05'] and fills up what corresponding value of the key[date] in dict
            avg_temp = sum(item["main"]["temp"] for item in forecast) / len(forecast) - 273.15 # for every detail or key values in forecast in ["main"]["temp"] data (temperature), sum it all and divide it by len of forecast values (how many temp value). e.g. all values of temp in 2026-07-07 will sum it all and divide how many they are to get avg value.
            weather_ids = [ # Collect all weather IDs for this day.
                item["weather"][0]["id"] for item in forecast
            ]
            weather_id = Counter(weather_ids).most_common(1)[0][0] # Find the weather ID that appears most often. This represents the overall weather condition for the day. most_common(1)[0][0] means taking out from (500,3) put [0] so we get 500
            weather_forecast_descriptions = [
                item["weather"][0]["description"] for item in forecast
            ]
            weather_forecast_description = Counter(weather_forecast_descriptions).most_common(1)[0][0]
            forecast_summary.append({
                "day_name": day_name,
                "date": date,
                "avg_temp": avg_temp,
                "weather_id": weather_id,
                "weather_forecast_description": weather_forecast_description
            })

        today = datetime.now()
        formatted_date = today.strftime("%A, \t%b %#d")

        self.temperature_label.setText(f"{temperature_c:.0f}°C") # This will display the data in the weather app
        self.emoji_label.setPixmap(self.get_weather_emoji(weather_id).scaled(100,100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.description_label.setText(weather_description.title())

        self.day_title.setText("3-Day Forecast")

        self.day1_temp.setText(f"{forecast_summary[0]['avg_temp']:.1f}°C")
        self.day2_temp.setText(f"{forecast_summary[1]['avg_temp']:.1f}°C")
        self.day3_temp.setText(f"{forecast_summary[2]['avg_temp']:.1f}°C")

        self.day1_emoji.setPixmap(self.get_weather_emoji(forecast_summary[0]["weather_id"]))
        self.day2_emoji.setPixmap(self.get_weather_emoji(forecast_summary[1]["weather_id"]))
        self.day3_emoji.setPixmap(self.get_weather_emoji(forecast_summary[2]["weather_id"]))

        self.day1_description_label.setText(forecast_summary[0]["weather_forecast_description"].title())
        self.day2_description_label.setText(forecast_summary[1]["weather_forecast_description"].title())
        self.day3_description_label.setText(forecast_summary[2]["weather_forecast_description"].title())

        self.day1_name.setText(forecast_summary[0]["day_name"].upper())
        self.day2_name.setText(forecast_summary[1]["day_name"].upper())
        self.day3_name.setText(forecast_summary[2]["day_name"].upper())

        self.date_today.setText(formatted_date)

        self.feels_like_label.setText(f"Feels like {feels_like:.01f}°C")

    def get_weather_3days(self, forecast_data): # This will get the next 3 days of weather data
        forecast_by_day = defaultdict(list) # Creating a dictionary so we can use it on the whole program
        for item in forecast_data["list"]: # For every data in forecast_data inside the dictionary of ["list"]
            date = item["dt_txt"].split()[0] # declare the date as the date that we can get in every item(data) in forecast_data["list"]
            forecast_by_day[date].append(item) # access what we create a dictionary to key of date follow the append to fill up the key date with its corresponding value from forecast_data["list"]

        today = datetime.now().strftime("%Y-%m-%d")

        next_3days =[] # declare an empty list for storing 3 days of date
        for date in forecast_by_day: # For every date (key) in forecast_by_day dictionary
            if date > today: # check first if the date is greater than today date
                next_3days.append(date) # if so, append the value of the date (key from the forecast_by_day dictionary)

        return next_3days[:3], forecast_by_day # this will return a value of what we process here in this method, [:3] means first 3 dates only

    @staticmethod # belong to a class but not require an instance or any other method
    def get_weather_emoji(weather_id):
        clouds = QPixmap("icons/clouds.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        fog = QPixmap("icons/fog.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        heavy_rain = QPixmap("icons/heavy-rain.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        tornado = QPixmap("icons/hurricane.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        light_rain = QPixmap("icons/light-rain.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        snow = QPixmap("icons/snowflake.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        thunder = QPixmap("icons/thunder.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        windy = QPixmap("icons/windy.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        volcano = QPixmap("icons/volcano.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        sunny = QPixmap("icons/sun.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        none = QPixmap("icons/forbidden.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        if 200 <= weather_id <= 232:
            return thunder
        elif 300 <= weather_id <= 321:
            return light_rain
        elif 500 <= weather_id <= 531:
            return heavy_rain
        elif 600 <= weather_id <= 622:
            return snow
        elif 701 <= weather_id <= 781:
            return fog
        elif weather_id == 762:
            return volcano
        elif weather_id == 771:
            return  windy
        elif weather_id == 781:
            return tornado
        elif weather_id == 800:
            return sunny
        elif 801 <= weather_id <= 804:
            return clouds
        else:
            return none

if __name__ == "__main__":
    app = QApplication(sys.argv) # To access the application
    weather_app = WeatherApp() # To access our class module with is the QWidget of WeatherApp
    weather_app.show() # To show the application on screen
    sys.exit(app.exec_()) # To proper exit the application we created