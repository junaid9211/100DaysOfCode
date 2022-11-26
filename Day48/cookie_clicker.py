from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time, sleep
from random import choice
from save_data import save_id

class CookieClicker(webdriver.Chrome):

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-site-isolation-trials")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("detach", True)
        super(CookieClicker, self).__init__(options=options)
        self.implicitly_wait(5)
        self.maximize_window()
        self.get('https://orteil.dashnet.org/cookieclicker/')

        WebDriverWait(self, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#langSelect-EN'))
        )
        self.find_element(By.CSS_SELECTOR, '#langSelect-EN').click()

        WebDriverWait(self, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button#bigCookie"))
        )

        # close cookies notice
        self.find_element(By.CSS_SELECTOR, ".cc_btn.cc_btn_accept_all").click()
        sleep(1)
        self.find_element(By.XPATH, "//div[contains(text(), 'Options')]").click()
        self.find_element(By.XPATH, "//a[contains(text(), 'Import save')]").click()
        self.find_element(By.CSS_SELECTOR, "textarea#textareaPrompt").send_keys(save_id)
        sleep(1)
        self.find_element(By.CSS_SELECTOR, "a#promptOption0").click()
        self.find_element(By.CSS_SELECTOR, "div.close.menuClose").click()

        self.wait_time = 0
        self.minute_count = 1


    # TODO: test close notifications
    def close_achievements(self):
        try:
            self.find_element(By.CSS_SELECTOR, ".framed.close.sidenote").click()
        except:
            pass
        else:
            print("Closed achievements")



    # TODO: test buy upgrades
    def buy_upgrades(self):
        print("Trying to buy all available upgrades...")

        while True:
            try:
                # click each item until an element not found exception is raised?
                self.find_element(By.CSS_SELECTOR, '.crate.upgrade.enabled').click()
            except Exception:
                break



    # TODO: test click cookies
    def click_cookie(self):
        cookie = self.find_element(By.CSS_SELECTOR, "button#bigCookie")
        cookie.click()


    def click_cookies(self, click_count):
        for _ in range(click_count):
            self.click_cookie()


    # TODO logic for buying items, problem, no exception for clicking disabled
    # solution, check if disabled
    def buy_items(self):
        if time() > self.wait_time:
            print("Trying to click last item...")
            last_item = self.get_items_list()[-1]
            if 'enabled' in last_item.get_attribute('class'):
                last_item.click()
                self.wait_time = time()
            else:
                print("Couldn't click, clicking other items...")
                for _ in range(10):
                    try:
                        choice(self.get_items_list(choice='enabled')).click()
                    except:
                        pass


                print("Will try again to click last item after a minute")
                self.wait_time = 60*self.minute_count + time()
                self.minute_count += 1




    # TODO close backup save reminder


    # enabled items
    def get_items_list(self, choice='all'):
        if choice == 'all':
            return self.find_elements(By.CSS_SELECTOR, '.product.unlocked')
        elif choice == 'enabled':
            return self.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')




c = CookieClicker()

while True:
    c.click_cookies(50)
    c.buy_items()
    c.buy_upgrades()
    c.close_achievements()