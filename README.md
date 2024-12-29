# Zillow Scraper & Google Spreadsheet Automation

This repository contains a Python-based application that automates the process of collecting rental or purchase property data from Zillow.com and organizing it into a Google Spreadsheet. The project streamlines the property search experience by providing users with a structured and easy-to-read format for decision-making.

## Features

- **Automated Data Collection**:
  - Scrapes property data from Zillow.com based on user-provided URL and area.
  - Retrieves details such as rental price, address, and availability date.

- **Google Forms Integration**:
  - Automatically fills a Google Form with scraped data using Selenium WebDriver.
  - Ensures seamless transfer of information to a Google Spreadsheet.

- **Streamlined Property Listing**:
  - Organizes property details into a Google Spreadsheet for user convenience.
  - Enables fast and informed decision-making.

## How It Works

1. **User Input**:
   - The user provides a Zillow URL and specifies the desired area for rental or purchase.
2. **Data Scraping**:
   - Selenium WebDriver navigates Zillow.com to collect property details.
3. **Google Forms Automation**:
   - The scraped data is entered into a Google Form.
4. **Google Spreadsheet Output**:
   - The form responses are automatically saved to a Google Spreadsheet for easy viewing.

## Requirements

To run this project, ensure you have the following:

- Python 3.x
- Libraries: `selenium`, `requests`, `time`
- ChromeDriver installed and configured for Selenium
- Google account access with permission to use Google Forms and Spreadsheets

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/zillow-scraper-automation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd zillow-scraper-automation
   ```
3. Install the required dependencies:
   ```bash
   pip install selenium requests time
   ```
4. Set up your Google API credentials and save them as a JSON file.
5. Update the script with your Google Form URL and Zillow area URL.
6. Run the application:
   ```bash
   python rental_property_research.py
   ```

## Applications

- **Real Estate Search**: Quickly gather property details for renting or buying.
- **Automated Workflows**: Eliminate manual data entry by automating the transfer of data to Google Spreadsheets.
- **Decision Support**: Provides a structured overview of properties to facilitate informed decision-making.

---
Simplify your property search with Zillow Property Automation!

