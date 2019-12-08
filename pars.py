from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import config

chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox")
CHROMEDRIVER_PATH = 'C:\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)


if __name__ == "__main__":
    driver.get(config.url)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "PrnConfWriteSelectDisp"))
        )
        # driver.find_element_by_id("PrnConfWriteSelectDisp").send_keys("file-path")
        # driver.find_element_by_id("submit").click()
    finally:
        driver.quit()
