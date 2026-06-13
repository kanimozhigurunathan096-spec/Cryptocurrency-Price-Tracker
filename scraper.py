from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://coinmarketcap.com/")

time.sleep(5)

rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

data = []

for row in rows[:10]:

    try:
        name = row.find_element(
            By.XPATH,
            ".//p[contains(@class,'coin-item-name')]"
        ).text

        price = row.find_element(
            By.XPATH,
            ".//td[4]"
        ).text

        change = row.find_element(
            By.XPATH,
            ".//td[5]"
        ).text

        market_cap = row.find_element(
            By.XPATH,
            ".//td[8]"
        ).text

        data.append([
            name,
            price,
            change,
            market_cap
        ])

    except:
        pass

driver.quit()

df = pd.DataFrame(
    data,
    columns=[
        "Coin Name",
        "Price",
        "24h Change",
        "Market Cap"
    ]
)

df.to_csv(
    "crypto_prices.csv",
    index=False
)

print(df)

print("\nData Saved Successfully!")