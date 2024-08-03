# price_exchange_scraper
This Python script is designed to automate the process of scraping exchange rate data from the Eximbank website


# Key Features:
**Automated Web Scraping:** The script navigates to the Eximbank exchange rate page and extracts currency data, including the buying and selling rates. It does so every 6 hours, ensuring that you have up-to-date information without manual intervention.

**Percentage Change Calculation:** After each scan, the script calculates the percentage change in the selling rates compared to the previous scan, providing insight into how the exchange rates are fluctuating over time.

**Manual Trigger with C Key:** Users can manually trigger an immediate scan by pressing the C key, allowing for flexibility in when the data is refreshed, in case an urgent update is needed.

**Real-Time Countdown Display:** The script includes a countdown timer that displays how much time is left until the next automatic scan. This timer updates in real time, and the user is informed that they can press C to initiate an early scan.

**Console Output:** Each scan outputs the current exchange rate data to the console, along with the calculated percentage change in the sell prices, making it easy to monitor trends directly from the terminal.


# Use Cases:

**Exchange Rate Monitoring:** Ideal for financial analysts, traders, or anyone needing regular updates on currency exchange rates.

**Trend Analysis:** The percentage change feature helps track trends in currency fluctuations, providing valuable insights for decision-making.

**Convenient Manual Scans:** The ability to trigger scans on demand makes the script versatile, allowing users to get updates whenever they need them, without waiting for the scheduled interval.