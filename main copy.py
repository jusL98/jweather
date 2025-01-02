import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt
import datetime

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        # Initialize Widgets
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("✔️", self)
        self.temperature_label = QLabel("0°C",self)
        self.emoji_label = QLabel("⛈️",self)
        self.description_label = QLabel("Stormy", self)

        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Weather App")

        # Layout Manager
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.city_input)
        hbox.addWidget(self.get_weather_button)
        vbox.addItem(hbox)

        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        # Align Widgets In Center
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Set Stylesheet
        self.city_label.setObjectName("city_label")
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
                font-family: Segoe UI Emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "d63fc3d821befae4fd586ad520fe81f3"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status() # Raises an exception if there are any HTTP errors.
            data = response.json()
            
            if data["cod"] == 200:
                self.display_weather(data)
                print(data["dt"])
                #print(datetime.datetime.fromtimestamp(data["dt"]).strftime("%b %d, %Y"))
                #print(datetime.datetime.fromtimestamp(data["dt"]).strftime("%I:%M %p"))
        
        except requests.exceptions.HTTPError as http_error: # Handles HTTP not found.
            match response.status_code :
                case 400:
                    self.display_error("Bad request\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response form the server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connect Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error: # Handles network problems and invalid urls.
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        # Temperature
        temperature_k = data["main"]["temp"] # Access temperature in Kelvin.
        temperature_c = temperature_k - 273.15 # Convert temperature to Celsius.
        temperature_f = (temperature_k * 9/5) - 459.67 # Convert temperature to Fahrenheit.
        
        self.temperature_label.setStyleSheet("font-size: 75px;")
        self.temperature_label.setText(f"{temperature_c:.0f}°C")

        #  Weather Emoji
        weather_id = data["weather"][0]["id"]
        self.emoji_label.setText(self.get_weather_emoji(weather_id))

        # Weather Description
        description = data["weather"][0]["description"]
        self.description_label.setText(description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if  200 <= weather_id <= 232:
            return "⛈️"
        elif  300 <= weather_id <= 321:
            return "🌦️"
        elif  500 <= weather_id <= 531:
            return "🌧️"
        elif  600 <= weather_id <= 622:
            return "❄️"
        elif  701 <= weather_id <= 741:
            return "🌫️"
        elif  weather_id == 762:
            return "🌋"
        elif  weather_id == 771:
            return "💨"
        elif  weather_id == 781:
            return "🌪️"
        elif  weather_id == 800:
            return "☀️"
        elif  801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""

# Run Code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
