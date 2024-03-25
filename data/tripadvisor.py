import time
import csv
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option("detach", True)
options.add_argument("--window-size=1520,800")
options.add_argument("-disable-notifications")

options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0")
# options.add_argument("--headless")
# options.add_argument("--proxy-server=YOUR_PROXY_SERVER")

driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options=options)

driver.implicitly_wait(1000)

for i in range(0, 7132, 10):
    driver.get("https://www.tripadvisor.com/Attraction_Review-g293926-d317599-Reviews-or"+str(i)+"-Hue_Imperial_City_The_Citadel-Hue_Thua_Thien_Hue_Province.html")
    
    random_float = random.uniform(10, 10)
    time.sleep(random_float)

    # elements cause problem
    elements = driver.find_elements(by='css selector', value='.JguWG .yCeTE')
    
    with open('reviews.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Check if the file is empty (no header row)
        if csvfile.tell() == 0:  # tell() returns the current file position
            csv_writer.writerow(['Text'])  # Write header row only if file is empty

        for element in elements:
            csv_writer.writerow([element.text])
    
    with open("count.txt", "a") as file:
        file.write(str(i) + "\n")