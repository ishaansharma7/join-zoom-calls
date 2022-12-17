from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback

driver = None
driver = webdriver.Chrome(executable_path='/Users/ishaansharma/Documents/YouTube/code/selenium_zoom/chromedriver')
driver.maximize_window()
sleep(5) 

def login_process(meeting_id, password):

        driver.get(f'https://us04web.zoom.us/wc/join/{meeting_id}?')

        # login code
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "inputpasscode"))).send_keys(password)
            sleep(1)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inputname"]'))).send_keys('PyBot')
            sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="joinBtn"]'))).click()
            sleep(5)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/button'))).click()
        except Exception:
            print('error in logging')
            exit()


def after_login():

    # open participants list
    try:
        wait_for_bar = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'video-avatar__avatar')))
        driver.execute_script('document.getElementById("wc-footer").className = "footer";')
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wc-footer"]/div/div[2]/div[1]/button'))).click()
    except Exception:
        traceback.print_exc()
        print('error occured, not able to open participants list in time')
    
    # read name div
    try:
        sleep(4)
        name_div = driver.find_elements(by=By.CLASS_NAME, value='participants-item-position')
    except Exception:
        traceback.print_exc()
        print('unable to read participants 1')
    
    # loop the div and parse names
    try:
        print('Participants:')
        for idx, participant in enumerate(name_div, 1):
            name = participant.find_element(by=By.TAG_NAME, value='span')
            print(idx, name.text.replace('\n', ' '))
    except Exception:
        traceback.print_exc()
        print('unable to read participants 2')


if __name__ == '__main__':
    login_process('meeting_id_here', 'password_here')
    after_login()
