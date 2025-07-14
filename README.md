<a id="readme-top"></a>

# JWeather

This GUI is a weather application to search and stay updated every 10 minutes of the weather (temperature and condition) of any inputted city through a desktop GUI.

<p align="left">
   <img width="600" alt="image" src="https://gist.github.com/user-attachments/assets/ee8e9eb3-ebc4-41f4-8480-a3f483de1426"/>
</p>

## Description

JWeather contains several weather features including:

- Inputting a city
- Displaying the temperature for that city
- Displaying the weather conditions for that city
- Automatically refreshing the weather, date and time every 10 minutes

## Built With

- [Python 3.13](https://www.python.org/): Programming language for complete functionality
- [PyQt5](https://pypi.org/project/PyPDF2/): Library for creating the GUI
- [OpenWeather](https://pypi.org/project/PyPDF2/): API (free) for retrieving weather data

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

### Setup

To use the demo PDF files, skip the following setup steps. Otherwise, to merge your own files, proceed.

5. Open `main.py`:
   - On Windows:
     ```bash
     notepad main.py
     ```
   - On macOS or Linux
     ```bash
     open main.py
     ```
6. Edit the file's configuration variables to input your own PDF file paths, output PDF name and output PDF file path.
   ```bash
   # ENTER PDF FILE PATHS, OUTPUT PDF NAME, AND OUTPUT PDF PATH HERE.
   pdf_list = ["C:/Users/justi/Downloads/test1.pdf","test2.pdf"] # format with forward slashes and no trailing slash OR use relative file paths by placing the file in the same directory as this script
   output_pdf_name = "merged.pdf"
   output_pdf_path = "" # format with forward slashes and no trailing slash OR leave blank for output file destination to be the same directory as this script
   # ---------------------------------------------------------------
   ```

### Run

6. Run JWeather:
   ```bash
   python main.py
   ```

7. Alternatively, download and run the `jweather.exe` file.

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
│   └── TBD
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
