from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure browser options (replace with desired browser)
options = webdriver.ChromeOptions()

# Consider these options (consult documentation for details):
# - User-Agent: Set a realistic human-like UA string.
# - Headless: Run the browser in headless mode (optional).
# - Proxy: Use a residential proxy (ethical considerations apply).
options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0")
# options.add_argument("--headless")
# options.add_argument("--proxy-server=YOUR_PROXY_SERVER")

driver = webdriver.Chrome(options=options)

# ... Your scraping logic here ...


driver.implicitly_wait(1000)

driver.get("https://www.tripadvisor.com/Attraction_Review-g293926-d317599-Reviews-or"+str(0)+"-Hue_Imperial_City_The_Citadel-Hue_Thua_Thien_Hue_Province.html")

time.sleep(1000)