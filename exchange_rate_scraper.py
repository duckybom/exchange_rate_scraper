import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from tabulate import tabulate

# Store the previous sell prices
previous_sell_prices = {}

# Function to scrape exchange rate data
def scrape_exchange_rates():
    global previous_sell_prices

    # Initialize the WebDriver
    driver = webdriver.Chrome()  # or 'webdriver.Firefox()' if using Firefox

    try:
        # Open the website
        driver.get("https://eximbank.com.vn/bang-ty-gia")

        # Allow time for the page to load
        time.sleep(5)

        # Locate the exchange rate table using the updated XPath
        table = driver.find_element(By.XPATH, "//table[contains(@class, 'w-full overflow-hidden table-auto rounded-2xl')]")

        # Fetch all rows of the table
        rows = table.find_elements(By.TAG_NAME, "tr")

        # Store data for the table
        table_data = []

        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            if columns:
                currency = columns[0].text.strip()
                buy_cash = columns[1].text.strip()
                buy_transfer = columns[2].text.strip()
                sell = columns[3].text.strip()

                # Calculate percentage change in the sell price
                sell_price = float(sell.replace(",", ""))
                if currency in previous_sell_prices:
                    previous_price = previous_sell_prices[currency]
                    change = ((sell_price - previous_price) / previous_price) * 100
                    change_str = f"{change:.2f}%"
                else:
                    change_str = "N/A"  # No previous data available

                # Update the previous sell prices dictionary
                previous_sell_prices[currency] = sell_price

                # Append the row data to the table_data list
                table_data.append([currency, buy_cash, buy_transfer, sell, change_str])

        # Print the table using tabulate
        headers = ["Currency", "Buy (Cash)", "Buy (Transfer)", "Sell", "Change (%)"]
        print(tabulate(table_data, headers, tablefmt="pretty"))

    finally:
        # Close the browser
        driver.quit()

# Function to handle the scan logic
def scan():
    print("Starting a new scan...")
    scrape_exchange_rates()
    print("Scan completed.")

# Loop to run the script every 6 hours or when 'C' is pressed
while True:
    scan()  # Perform the initial scan

    # Time until next scan (6 hours)
    wait_time = 6 * 60 * 60  # 6 hours in seconds

    for remaining in range(wait_time, 0, -1):
        hours, rem = divmod(remaining, 3600)
        minutes, seconds = divmod(rem, 60)
        print(f"Next scan in: {hours:02}:{minutes:02}:{seconds:02} (Press 'C' to scan now)", end='\r')
        
        time.sleep(1)
        
        # Check if 'C' key is pressed
        if keyboard.is_pressed('C'):
            print("\n'C' key pressed. Scanning now...")
            scan()
            break

    print("\n")  # Move to a new line after the countdown or manual scan
