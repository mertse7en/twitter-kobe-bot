import datetime
import os, sys
import time
# Selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

import logging
logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(name)s - %(funcName)s - %(message)s")

from src.util import get_date


class Scrapper:

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.login_page_url = 'https://twitter.com/login'

        # Chrome options
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument('--no-sandbox') # Bypass OS security model
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu') #  applicable to windows os only
        chrome_options.add_argument('--disable-dev-shm-usage') # overcome limited resource problems
        # chrome_options.add_argument("disable-infobars")
        # chrome_options.add_argument("--disable-extensions");

        self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)


    def tweet_bot(self):
        self.__login()

        time.sleep(3)
        # change url
        self.driver.get('https://twitter.com/compose/tweet')

        message = Scrapper.set_tweet()

        tweet = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'))
        )
        tweet.send_keys(message)
        
        # Click tweet
        self.__click_with_explicit_wait('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')

        time.sleep(5)

    def __login(self):
        self.driver.get(self.login_page_url)

        mail = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input"))
        )
        email = os.environ["mail"]
        mail.send_keys(email)

        # Click login
        self.__click_with_explicit_wait('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div')

        try:
            temp_user_name_location = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'))
            )                                              
            tw_name = os.environ["user_name"]
            temp_user_name_location.send_keys(tw_name)
            self.__click_with_explicit_wait('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')

            # Enter pass
            pass_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input'))
            )
            password = os.environ["password"]
            pass_button.send_keys(password)

            self.__click_with_explicit_wait('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        except:
            # Enter pass
            pass_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input'))
            )
            password = os.environ["password"]
            pass_button.send_keys(password)

            self.__click_with_explicit_wait('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        self.logger.info("Logged in succesfully")



    def __click_with_explicit_wait(self, locator, by="XPATH"):
        if(by == "XPATH"):
            try:
                button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
            except TimeoutException as ex:
                print("Could not find element! " + str(ex))
            except Exception:
                print("Something went wrong")
        elif(by == "NAME"):
            button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, locator)))
        elif(by == "CSS"):
            button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))

        self.driver.execute_script("return arguments[0].scrollIntoView();", button)
        button.click()

        self.logger.info("Clicked locator : {}".format(locator))

    def __change_url(self, url):
        self.logger.warning("old url :" + self.driver.current_url + " has changed to :" + url)
        self.driver.get(url)
        time.sleep(5)


    @staticmethod
    def set_tweet():
        kobe_death = datetime.date(2020, 1, 26)
        today = datetime.date.today()

        delta = today - kobe_death
        message = f"Kobe passed away {delta.days} days ago."
        return message





