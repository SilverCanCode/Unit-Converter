Length Unit Converter

This is a Python application for converting lengths using an API from RapidAPI. It allows users to convert between various length units such as nanometers, meters, inches, miles, etc.
Features

    Conversion between different length units.
    User-friendly graphical interface built with custom tkinter widgets.
    Error handling for invalid input.

Requirements

    Python 3.x
    requests library
    PIL library
    customtkinter library

Installation

    Clone this repository to your local machine:

    bash

git clone https://github.com/SilverCanCode/Unit-Converter.git

Navigate to the project directory:

bash

cd unit-converter

Install the required libraries using pip:

pip install -r requirements.txt

Obtain an API key from RapidAPI by signing up and subscribing to the length conversion API.
Open the unit_converter.py file and replace "YOUR_API_KEY" in the headers dictionary with your actual API key.
Run the unit_converter.py file:

    python unit_converter.py

Usage

    Enter the value you want to convert in the provided entry box.
    Select the unit you want to convert from in the first dropdown menu.
    Select the unit you want to convert to in the second dropdown menu.
    Click the "Convert" button to get the conversion result displayed.

API

The length conversion functionality is achieved using the RapidAPI length conversion API. You need to sign up for RapidAPI and obtain an API key to use this service.
Notes

    Ensure an active internet connection to access the API.
    This application currently supports only length-based conversions.
    Background image path may need to be adjusted based on your file structure.

Go Check out the API:

    https://rapidapi.com/foxello-foxello-default/api/measurement-unit-converter

Feel free to contribute to this project by forking and submitting pull requests!

🛠️ Happy coding!