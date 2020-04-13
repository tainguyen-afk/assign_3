import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class blog_test(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_update_post(self):
       user = "instructor"
       pwd = "maverick1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("http://127.0.0.1:8000")
       assert "Logged In"
       time.sleep(5)
       driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/h2/a').click()
       driver.find_element_by_xpath('/html/body/div[2]/div/div/div/a').click()
       time.sleep(5)
       driver.find_element_by_id('id_title').clear()
       driver.find_element_by_id('id_text').clear()
       time.sleep(5)
       elem =driver.find_element_by_id('id_title')
       elem.send_keys('this is an update')
       elem =driver.find_element_by_id('id_text')
       elem.send_keys('this is an update')
       driver.find_element_by_xpath('/html/body/div[2]/div/div/form/button').click()
       assert "post updated"
       time.sleep(5)
       driver.get("http://127.0.0.1:8000")
       time.sleep(5)









   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()

