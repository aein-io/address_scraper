# Address Scraper
![Alt text](address_scraper_banner.png)

## A Python project that scrapes US addresses!

This project scrapes US addresses from the Realty in US API in RapidApi and returns it as a CSV file. The user also has the option to display the scraped addresses to a map.

It includes the following features:
- Customizable API request calls
- Map display of the scraped addresses

## Dependencies
- python 3.10+
- poetry
- pydantic
- requests
- pandas
- geopy
- folium

## Installation instructions
1. Clone this project.
2. Install poetry.  ``` pip install poetry ```

## Usage instructions
1. Run ``` poetry install ``` in the directory of the project.
2. Run the project using ``` python address_scraper/scraper.py ``` to see the usage.

```python
  usage: scraper.py [-h] -s STATE [-t TOTAL] [-l LIMIT] [-v] [-m]
```
```
-s: State or state code of desired US state | [-s NY]
-t total number of addresses to scrape (max 10000) must be greather than limit | [-t 50]
-l how many addresses to scrape per API call (max 200) must be less than total | [-l 10]
-v if provided, debug logging is enabled
-m if provided, output is mapped to a browser

```
