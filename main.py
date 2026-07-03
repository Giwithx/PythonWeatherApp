import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from requests import HTTPError, Request


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__() # accessing the function of the QWidget using the super function
        self.city_label = QLabel("Enter city name: ", self) # This will put a label on app to enter the city name
        self.city_input = QLineEdit(self) # This will put a line edit on the app
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel( self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout() # This will organize what we put on the app

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox) # This will set all what we declare in our add widget

        self.city_label.setAlignment(Qt.AlignCenter) #T This will align all widget in the app to center
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label") # This is declaration for the setStyleSheet
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

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
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather) # This will connect the function of clicked to our method of get_weather

    def get_weather(self):

        api_key = "d5585dc1641641f32c1ea51cb47ec58d" # This is the key from the weather API
        city = self.city_input.text() # this will get what we input in the city_input QLineEdit
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" # This is the url from the API website

        try:
            response = requests.get(url) # This will get the request from the URL
            response.raise_for_status() # This will raise an exception if theres an error
            data = response.json() #convert the response to json format

            if data["cod"] == 200: # 200 means okay connection and will display the weather data
                self.display_weather(data) # passing to the method of display data to display the data on the app

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input") # This will call the display error method and will output on the app
                case 401:
                    self.display_error("Unauthorized:\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not Found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;") # This will set the font size to smaller since the error code is big
        self.temperature_label.setText(message)
        self.emoji_label.clear() # This will clear the emoji and the description label to clearly print only the temperature label
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;") # Back the font size to original
        temperature_k = data["main"]["temp"] # This will access the dictionary of main and accessing the temp
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        weather_description = data["weather"][0]["description"] # This will access the list of weather in the index of 0 and the value of description
        weather_id = data["weather"][0]["id"] # Thiw will access the id which is essential for the weather emoji
        self.temperature_label.setText(f"{temperature_c:.0f}°C") # This will display the data in the weather app
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

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
            return "🌥️"
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv) # To access the application
    weather_app = WeatherApp() # To access our class module with is the QWidget of WeatherApp
    weather_app.show() # To show the application on screen
    sys.exit(app.exec_()) # To proper exit the application we created