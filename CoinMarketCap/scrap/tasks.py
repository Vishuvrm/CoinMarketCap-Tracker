# Creating the web scrapper
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
import time
import requests
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

def get_data(url):

    # If you want to fetch all the data on screen, just uncomment below code

    # screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    # i = 1
    #  # scroll one screen height each time
    # while True:
    #     # scroll one screen height each time
    #     driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    #     i += 1
    #     # time.sleep(scroll_pause_time)
    #     # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    #     scroll_height = driver.execute_script("return document.documentElement.scrollHeight;")  

    #     # Break the loop when the height we need to scroll to is larger than the total scroll height
    #     if (screen_height) * i > scroll_height:
    #         break 

    table = driver.find_element(by=By.XPATH, value=r"""//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[5]/table""")

    table_rows = table.find_element(by=By.TAG_NAME, value="tbody").find_elements(by=By.TAG_NAME, value="tr")
    TABLE_DATA = []
    for row in table_rows[:5]:
        ROW_DATA = {}
        row_data = row.find_elements(by=By.TAG_NAME, value="td")[2:-2]
        for point, column in zip(row_data, HEADER):
            data_lst = point.find_elements(by=By.TAG_NAME, value="span")
            # data_lst1 = point.find_elements(by=By.TAG_NAME, value="span")
            # data_lst = data_lst if len(data_lst)==1 else data_lst[:-1]
            
            if data_lst:
                try:
                    text = sign = ""
                    for d in data_lst:
                        text += d.text
                        sign += ""
                        if d.find_elements(by=By.CLASS_NAME, value="icon-Caret-down"):
                            sign = "-"
                        elif d.find_elements(by=By.CLASS_NAME, value="icon-Caret-up"):
                            sign = "+"
                        record = sign + text
                except  Exception as e:
                    print(e)
            else:
                data_lst = [r.text for r in point.find_elements(by=By.TAG_NAME, value="p")]
                record = " ".join(data_lst)
            ROW_DATA[column] = record
        
        TABLE_DATA.append(ROW_DATA)
    
    return TABLE_DATA

def get_driver_connectivity():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    return webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)



if __name__ == "__main__":
    url = env("SCRAP_URL")
    driver = get_driver_connectivity()
    driver.get(url)
    HEADER = ["name", "price", "perc_1h", "perc_24h", "perc_7d", "market_cap", "volume_24h", "circulating_supply"]
    BASE_URL = env("BACKEND_BASE_URL")
    while True:
        full_data = get_data(url)
        for data in full_data:
            try:
                response = requests.post(BASE_URL + "scrap/put-data", data=data)
                print(response)
            except Exception as e:
                print(e)
                break
        time.sleep(5)