from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option("detach", True)
options.add_argument("--window-size=1520,800")
options.add_argument("-disable-notifications")

driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options=options)

driver.implicitly_wait(10)

def login(username, passwd):
    try:
        driver.get("https://www.facebook.com/")

        txtUsername = driver.find_element(By.ID, 'email')
        txtUsername.send_keys(username)

        txtPasswd = driver.find_element(By.ID, 'pass')
        txtPasswd.send_keys(passwd)

        btnLogin = driver.find_element(By.NAME, 'login')
        btnLogin.click()

        time.sleep(5)
        # driver.get(f"https://www.facebook.com/{username}")
        # verify login
        # there must be 'Add to story' button after login

    except Exception as e:
        print("Unable to login. Please check your username or password")
        print(e)

        return False
    
login("khanh.tq204881@sis.hust.edu.vn","tqk24232221")