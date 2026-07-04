import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from requests import HTTPError, Request


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__() # accessing the function of the QWidget using the super function
        self.city_label = QLabel("Enter city name: ", self) # This will put a label on app to enter the city name
        self.city_input = QLineEdit(self) # This will put a line edit on the app
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.day_title = QLabel(self)
        self.day1_temp = QLabel(self)
        self.day2_temp = QLabel(self)
        self.day3_temp = QLabel(self)
        self.day1_emoji = QLabel(self)
        self.day2_emoji = QLabel(self)
        self.day3_emoji = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        main_layout = QVBoxLayout() # This will organize what we put on the app

        city_layout = QVBoxLayout()
        city_layout.addWidget(self.city_label)
        city_layout.addWidget(self.city_input)
        city_layout.addWidget(self.get_weather_button)

        temperature_layout = QHBoxLayout()
        temperature_layout.addWidget(self.temperature_label)
        temperature_layout.addWidget(self.emoji_label)
        temperature_layout.addWidget(self.description_label)

        day_forecast_title = QVBoxLayout()
        day_forecast_title.addWidget(self.day_title)

        day_layout_main = QHBoxLayout()

        day1_temp_layout = QVBoxLayout()
        day1_temp_layout.addWidget(self.day1_temp)
        day1_temp_layout.addWidget(self.day1_emoji)
        day2_temp_layout = QVBoxLayout()
        day2_temp_layout.addWidget(self.day2_temp)
        day2_temp_layout.addWidget(self.day2_emoji)
        day3_temp_layout = QVBoxLayout()
        day3_temp_layout.addWidget(self.day3_temp)
        day3_temp_layout.addWidget(self.day3_emoji)

        day_layout_main.addLayout(day1_temp_layout)
        day_layout_main.addLayout(day2_temp_layout)
        day_layout_main.addLayout(day3_temp_layout)

        main_layout.addLayout(city_layout)
        main_layout.addLayout(temperature_layout)
        main_layout.addLayout(day_forecast_title)
        main_layout.addLayout(day_layout_main)

        self.setLayout(main_layout) # This will set all what we declare in our add widget

        self.city_label.setAlignment(Qt.AlignCenter) # This will align all widget in the app to center
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.day_title.setAlignment(Qt.AlignCenter)
        self.day1_temp.setAlignment(Qt.AlignCenter)
        self.day1_emoji.setAlignment(Qt.AlignCenter)
        self.day2_temp.setAlignment(Qt.AlignCenter)
        self.day2_emoji.setAlignment(Qt.AlignCenter)
        self.day3_temp.setAlignment(Qt.AlignCenter)
        self.day3_emoji.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label") # This is declaration for the setStyleSheet
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.day_title.setObjectName("day_title")
        self.day1_temp.setObjectName("day1_temp")
        self.day1_emoji.setObjectName("day1_emoji")
        self.day2_temp.setObjectName("day2_temp")
        self.day2_emoji.setObjectName("day2_emoji")
        self.day3_temp.setObjectName("day3_temp")
        self.day3_emoji.setObjectName("day3_emoji")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
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
            QLabel#day1_emoji, QLabel#day2_emoji, QLabel#day3_emoji, QLabel#day_emoji{
                font-size: 30px;
                font-family: Segoe UI emoji;
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

    def display_weather(self, data, forecast_data):
        self.temperature_label.setStyleSheet("font-size: 75px;") # Back the font size to original
        temperature_k = data["main"]["temp"] # This will access the dictionary of main and accessing the temp
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        weather_description = data["weather"][0]["description"] # This will access the list of weather in the index of 0 and the value of description
        weather_id = data["weather"][0]["id"] # This will access the id which is essential for the weather emoji
        ave_temp_day1 = self.get_average_temp(forecast_data, 0)
        ave_temp_day2 = self.get_average_temp(forecast_data, 1)
        ave_temp_day3 = self.get_average_temp(forecast_data, 2)
        day1_weather_id = forecast_data["list"][0]["weather"][0]["id"]
        day2_weather_id = forecast_data["list"][8]["weather"][0]["id"]
        day3_weather_id = forecast_data["list"][16]["weather"][0]["id"]

        self.temperature_label.setText(f"{temperature_c:.0f}°C") # This will display the data in the weather app
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description.upper())

        self.day_title.setText("3 Day Weather Forecast")

        self.day1_temp.setText(f"{ave_temp_day1:.0f}°C")
        self.day2_temp.setText(f"{ave_temp_day2:.0f}°C")
        self.day3_temp.setText(f"{ave_temp_day3:.0f}°C")

        self.day1_emoji.setText(self.get_weather_emoji(day1_weather_id))
        self.day2_emoji.setText(self.get_weather_emoji(day2_weather_id))
        self.day3_emoji.setText(self.get_weather_emoji(day3_weather_id))

    @staticmethod
    def get_average_temp(forecast_data, day):
        start = day * 8
        end = start + 8

        return sum(
            item["main"]["temp"]
            for item in forecast_data["list"][start:end]
        ) / 8 - 273.15

    @staticmethod # belong to a class but not require an instance or any other method
    def get_weather_emoji(weather_id):

        if 200 <= weather_id <= 232:
            return  "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 781:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return  "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv) # To access the application
    weather_app = WeatherApp() # To access our class module with is the QWidget of WeatherApp
    weather_app.show() # To show the application on screen
    sys.exit(app.exec_()) # To proper exit the application we created