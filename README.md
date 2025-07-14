<a id="readme-top"></a>

# JWeather

This GUI is a weather application to search and stay updated every 10 minutes of the weather (temperature and condition) of any inputted city through a desktop GUI.

<p align="left">
   <img width="600" alt="image" src="https://github.com/user-attachments/assets/d1ac88ae-ea9e-43b5-81bc-170ada32d296"/>
</p>

## Description

JWeather contains several weather features including:

- Inputting a city
- Displaying the temperature for that city
- Displaying the weather conditions for that city
- Automatically refreshing the weather, date and time every 10 minutes

## Built With

- [Python 3.13](https://www.python.org/): Programming language for complete functionality
- [PyQt5](https://pypi.org/project/PyQt5/): Library for creating the GUI
- [OpenWeather](https://home.openweathermap.org/api_keys): API (free) for retrieving weather data

## Quick Start

### Prerequisites

- OS
- Python 3.13 or higher
- Internet Connection
- Terminal or CLI Access

### Installation

To install JWeather, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/jusL98/jweather.git
   cd jweather
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

5. Copy and edit the .env file:
   ```bash
   cp .env.example .env
   ```


### Setup
6. Open the .env file:

   - On Windows:

      ```bash
      notepad .env
      ```

   - On macOS or Linux

      ```bash
      open .env
      ```

7. Retrieve an API key from https://home.openweathermap.org/api_keys.

8. Use your API key for the variable `API_KEY`.

   | Variable           | Description                            | Example                           |
   | ------------------ | -------------------------------------- | --------------------------------- |
   | API_KEY            | API key from OpenWeather               | `API_KEY=your_actual_api_key_here`|

   Don't add spaces around the = sign in the variables.

   Don't wrap values in quotes unless they contain spaces.

   ex. `.env`

   ```
   API_KEY=your_actual_api_key_here
   ```

### Run

9. Run JWeather:
   ```bash
   python main.py
   ```

10. Alternatively, download and run the `jweather.exe` file.

## Usage

1. Enter a city in the text input.
2. Press enter or the GO button to find the weather of the city.
3. View the temperature and weather condition of the city.
4. The graphic will change corresponding to the weather condition.
5. The weather automatically refreshes every 10 minutes after searching a city.
5. A dialog popup will inform of any errors such as CITY NOT FOUND, CONNECTION ERROR and BAD GATEWAY.

## Contributing

1. Fork & branch off main.
2. Make your changes.
3. PRs welcome!

## Project Structure

```
├── jweather/
│   ├── main.py                        # contains main program code and logic
│   ├── requirements.txt               # list of required dependencies for easy installation
│   ├── jweather.exe                   # .exe file for compiled version of JWeather
│   ├── .env                           # contains environment variables for configuration
│   └── .env.example                   # sample .env file
```

## Acknowledgements

This project was created to learn Python APIs and PyQt5 GUIs.

## License

This project is licensed under the [MIT](LICENSE.txt) License. See LICENSE.txt for more information.

<br>

---

Thank you!

<p align="left">
  <a href="mailto:justin.matthew.lee.18@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
  <a href="https://www.linkedin.com/in/justin-matthew-lee/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
    <a href="https://github.com/jusl98">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

<p align="right">(<a href="#readme-top">BACK TO TOP</a>)</p>
