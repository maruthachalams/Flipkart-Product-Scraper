# Flipkart Product Scraper

This Python script scrapes product details from the Flipkart website using Selenium and stores the information in a text file. The information includes the product name, annual power usage, room size, warranty, MRP, offer price, percentage of offer, and product link.

## Features
- Scrapes product details from Flipkart.
- Extracts product name, annual power usage, room size, warranty, MRP, offer price, percentage of offer, and product link.
- Saves the extracted information into a text file (`OutPut.txt`).
- Handles multiple filters and search criteria.

## Requirements
- Python 3.x
- `selenium` library
- `requests` library
- `re` library

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/maruthachalams/Flipkart-Product-Scraper.git
    cd flipkart-product-scraper
    ```
2. Install the required libraries:
    ```sh
    pip install selenium requests
    ```
3. Download the Chrome WebDriver and ensure it is in your PATH or in the same directory as your script.

## Usage
1. Run the script:
    ```sh
    python scraper.py
    ```
2. The output will be saved in a file named `OutPut.txt`.

## Code Explanation
### `data_clean(data)`
Cleans the input data by replacing or removing unwanted characters.

### `single_regex(pattern, target_string)`
Uses regular expressions to find matches in a target string and returns the first match found.

### Main Script
1. Initializes an output string with headers and writes it to `OutPut.txt`.
2. Sets up a Chrome WebDriver to automate browser actions.
3. Opens Flipkart's homepage, closes the login popup, clears the search bar, enters the search keyword, and applies various filters.
4. Retrieves the content of the current URL using the `requests` library.
5. Extracts product information using regular expressions.
6. Formats the extracted information and appends it to `OutPut.txt`.
7. Prints "Completed" when the scraping process is done.

