# Zillow Property Scraper

A Python automation script that scrapes San Francisco rental property listings from a Zillow clone website ([https://appbrewery.github.io/Zillow-Clone/](https://appbrewery.github.io/Zillow-Clone/)) and automatically submits the data to a Google Form.

## Features

- Scrapes San Francisco rental listings including:
  - Property addresses
  - Monthly rental prices
  - Property URLs
- Handles various property types (apartments, condos, houses)
- Automatically fills and submits Google Forms with the scraped data
- Handles price ranges (e.g., "$2,895+/mo" to "$2,895")
- Uses Selenium WebDriver for reliable form automation
- Implements smart waiting mechanisms and error handling

## Prerequisites

Before running this script, make sure you have the following installed:

- Python 3.x
- Chrome Browser
- ChromeDriver (compatible with your Chrome version)
- PyCharm IDE (Community or Professional)

## Opening with PyCharm

1. Open PyCharm
2. Select `File > Open` or click `Open` from the welcome screen
3. Navigate to the project directory and click `Open`
4. When prompted, select `This Window` to open the project
5. PyCharm will detect it's a Python project and create a virtual environment
6. Open the Terminal in PyCharm (`View > Tool Windows > Terminal`) and install the required packages:

```bash
pip install beautifulsoup4
pip install requests
pip install selenium
pip install lxml
```

## Running in PyCharm

1. Open `main.py` in the editor
2. Right-click anywhere in the editor and select `Run 'main'`
   - Alternatively, click the green play button in the top right
   - Or use the keyboard shortcut (⌃R on macOS, Shift+F10 on Windows/Linux)

## Data Collection

The script collects the following information from each rental listing:
- Complete property address
- Monthly rental price (cleaned from formats like "$2,895+/mo")
- Direct URL link to the property listing

## Error Handling

The script includes comprehensive error handling for:
- Failed web requests
- Missing property information
- Form filling errors
- Network timeouts
- Price format variations (e.g., "+/mo" suffixes)

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
