<p align="center">
   <img width="1000" alt="image" src="https://github.com/user-attachments/assets/dac223ea-5b3e-4b80-8282-c6b6cd95671c"/>
</p>

# JWeather App
JWeather App is a weather finder for an inputted city which I created to learn Python APIs and PyQt5 GUIs.

## About This Project
This weather app is a GUI where the user inputs a city and the temperature and weather condition is displayed back to the user. A date and time is displayed of when the weather was last updated which refreshes every 10 minutes automatically.

## Technologies Used
- Python 3.13
- PyQt5 GUI
- OpenWeather API

## Installation
To install the JWeather App, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/jusL98/weather-app.git
   cd weather-app
   ```

2. Ensure that you have python running on your system.

3. Create and activate a virtual environment:
   - On Windows:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

   - On macOS and Linux:
   
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt 
   ```

5. Run the JWeather App.
   ```bash
   python main.py
   ```

5. **Alternatively, download and run the jweatherapp.exe file.**

## Usage
1. Enter a city in the text input.
2. Press enter or the GO button to find the weather of the city.
3. View the temperature and weather condition of the city.
4. The graphic will change corresponding to the weather condition.
5. The weather automatically refreshes every 10 minutes after searching a city.
6. A dialog popup will inform of any errors such as CITY NOT FOUND, CONNECTION ERROR and BAD GATEWAY.

---

Thank you!
