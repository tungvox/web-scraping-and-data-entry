from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Chrome browser to remain open after script completion
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Fetch and parse the Zillow clone webpage
response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "lxml")
location_tags = soup.find_all('span', class_="StyledTag")
locations = []

# Extract and clean location text from tags
for tag in location_tags:
    text = ''.join(tag.find_all(string=True, recursive=False)).strip()
    text = ' '.join(text.split())
    locations.append(text)

def fill_form_field(selenium_driver, label_text, value):
    try:
        # Locate the form field label
        label = WebDriverWait(selenium_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//div[@role='heading']//span[contains(text(), '{label_text}')]"))
        )
        
        # Find the input field within the same container as the label
        container = label.find_element(By.XPATH, "./ancestor::div[@role='listitem']")
        try:
            input_field = container.find_element(By.XPATH, ".//textarea | .//input[@type='text']")
        except:
            print(f"Could not find input field for {label_text}")
            return False

        # Clear existing text and input new value
        input_field.clear()
        input_field.send_keys(value)
        return True
    except Exception as e:
        print(f"Error filling field {label_text}: {e}")
        return False

# Navigate to the Google Form
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeVyS1AQbwkFwd-SthQSPPRtF0IHzR6U9nM76It8rgqHP6Rfg/viewform")

# Process each property listing and submit form
articles = soup.find_all('article')
for article in articles:
    try:
        # Extract property details from the listing
        price = article.find('span', {'data-test': 'property-card-price'}).get_text(strip=True)
        price = price.split('/')[0]  # Remove '/mo' from price
        address = article.find('address', {'data-test': 'property-card-addr'}).get_text(strip=True)
        url = article.find('a', {'data-test': 'property-card-link'})['href']
        
        # Fill form fields with property details
        address_filled = fill_form_field(driver, "Address", address)
        price_filled = fill_form_field(driver, "Price/Month", price)
        url_filled = fill_form_field(driver, "Link to the property", url)

        # Submit form if all fields were filled successfully
        if address_filled and price_filled and url_filled:
            submit_button = driver.find_element(By.XPATH, "//div[@role='button' and @aria-label='Submit']")
            submit_button.click()
            
            # Allow time for form submission to complete
            time.sleep(2)
            
            # Return to form for next entry
            driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeVyS1AQbwkFwd-SthQSPPRtF0IHzR6U9nM76It8rgqHP6Rfg/viewform")
        else:
            print("Form not submitted due to incomplete fields.")
            
    except Exception as e:
        print(f"Error processing article: {e}")
        continue

# Clean up by closing the browser
driver.quit()
