#/usr/bin/env python3

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from config import EMAIL_OR_PHONE, PASSWORD


class FacebookCrawler:
    LOGIN_URL = 'https://www.facebook.com/login.php?login_attempt=1&lwv=111'

    def __init__(self, login, password, headless):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        
        chrome_options.headless = headless
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.wait = WebDriverWait(self.driver, 5)

        self.login(login, password)

    def login(self, login, password):
        self.driver.get(self.LOGIN_URL)

        # wait for the login page to load
        self.wait.until(EC.visibility_of_element_located((By.ID, "email")))

        self.driver.find_element_by_id('email').send_keys(login)
        self.driver.find_element_by_id('pass').send_keys(password)
        self.driver.find_element_by_id('loginbutton').click()
        
        
        # wait for the main page to load
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#u_0_a > div > div > div > a")))
        
        
    def _get_friends_list(self):
        return self.driver.find_elements_by_css_selector(".uiProfileBlockContent > div > div > div > a")

    def _get_online_friends_list(self):
        return self.driver.find_elements_by_css_selector('div#mobile_buddylist > div > a > div > div.content > div > strong')
    
    def get_friends(self):
        
        # click on the profile icon and go to the profile page
        self.driver.find_element_by_css_selector("div#u_0_a > div > div > div > a").click()
        
        # navigate to "friends" page
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul#u_fetchstream_3_8 > li:nth-child(3)')))
        self.driver.find_element_by_css_selector("ul#u_fetchstream_3_8 > li:nth-child(3) > a").click()
        
        # continuous scroll until no more new friends loaded
        num_of_loaded_friends = len(self._get_friends_list())
        while True:
                
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                self.wait.until(lambda driver: len(self._get_friends_list()) > num_of_loaded_friends)
                num_of_loaded_friends = len(self._get_friends_list())
            except TimeoutException:
                break  # no more friends loaded
                
        return [friend.text for friend in self._get_friends_list()]
    
    def get_online_friends(self):
        
        # go to mobile version messages page (done so that it is simple and easy to scrape)
        self.driver.get('https://m.facebook.com/buddylist.php')
        
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#mobile_buddylist > div > a > div > div.content > div > strong')))
        
        # continuous scroll until no more new friends loaded
        num_of_loaded_online_friends = len(self._get_online_friends_list())
        
        while True:
                
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                self.wait.until(lambda driver: len(self._get_online_friends_list()) > num_of_loaded_online_friends)
                num_of_loaded_online_friends = len(self._get_online_friends_list())
            except TimeoutException:
                break  # no more friends loaded
                
        return [online_friend.text for online_friend in self._get_online_friends_list()]
        
    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    crawler = FacebookCrawler(login=EMAIL_OR_PHONE, password=PASSWORD, headless=False)
    
    # get list of all friends and online friends
    friends = crawler.get_friends()
    online_friends = crawler.get_online_friends()
    
    # write the lists into txt files
    with open('exports/all_friends.txt', 'w') as f:
        f.write("\n".join(friends))

    with open('exports/online_friends.txt', 'w') as f:
        f.write("\n".join(online_friends))
    
    # quit the crawler
    crawler.quit()