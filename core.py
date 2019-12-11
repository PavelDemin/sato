# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import config
#import os

# def init_webriver():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-extensions")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")
#     CHROMEDRIVER_PATH = 'C:\\chromedriver.exe'
#     return webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)


# def load_config_from_printer(type_print: int) -> None:
#     """
#     param: type_print
#     1 - fast mode (Continuous) 
#     0 - dispenser mode

#     """
#     driver = init_webriver()
#     try:
#         driver.implicitly_wait(10)
#         driver.get(config.read_url)
#         configuration = driver.find_element_by_name('WEBDISH').get_attribute("value")
#         if type_print == 0:
#             with open(config.dispenser_conf, mode='w') as f:
#                 f.write(configuration)
#         elif type_print == 1:
#             with open(config.continuous_conf, mode='w') as f:
#                 f.write(configuration)
#     finally:
#         driver.quit()


# def download_config_to_printer(type_print: int) -> None:
#     driver = init_webriver()
#     driver.get(config.write_url)
#     try:
#         element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "PrnConfWriteSelectDisp"))
#         )
#         if type_print == 0:
#             driver.find_element_by_name("PRINTER_CONF").send_keys(os.path.abspath(config.dispenser_conf))
#         elif type_print == 1:
#              driver.find_element_by_name("PRINTER_CONF").send_keys(os.path.abspath(config.continuous_conf))
#         driver.find_element_by_name("PrnConfWriteSubmit").click()
        
#     finally:
#         driver.quit()


# def restart_printer() -> None:
#     driver = init_webriver()
#     driver.get(config.restart_url)
#     try:
#         driver.find_element_by_xpath("//input[1]").click()
#     finally:
#         driver.quit()


def get_type_printer() -> int:
    with requests.Session() as s:
        req = s.get(config.advanced_mode_url)
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'html5lib')
        printer_type = soup.find('select', attrs={'name': 'PrinterType'})
        selected_type = printer_type.find('option', selected=True)
        return int(selected_type.get('value'))
    else:
        raise Exception('Ошибка доступа!')


def get_advanced_config() -> dict:
    with requests.Session() as s:
        r = s.get(config.advanced_mode_url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html5lib')
            upload_data = {}
            for item in config.data_list:
                try:
                    upload_data[item] = soup.find('select', attrs={'name': item}).find('option', selected=True).get('value')
                except:
                    upload_data[item] = soup.find('input', attrs={'name': item}).get('value')
            return upload_data


def change_config(data: dict, param: dict) -> dict:
    data.update(param)
    return data



def send_data(data: dict) -> int:
    with requests.Session() as s:
        r = s.post(config.url_advanced_mode_cgi, data=data, headers=config.headers)
        return r.status_code


def restart_printer() -> int:
    with requests.Session() as s:
        r = s.post(config.url_restart_cgi, data={}, headers=config.headers)
        return r.status_code


if __name__ == "__main__":
    #load_config_from_printer(get_type_printer())
    #download_config_to_printer()
    #restart_printer()
    data = get_advanced_config()
    print(change_config(data, config.param_dispenser_mode))
    #print(config.data.keys())
    pass
