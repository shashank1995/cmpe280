import unittest
import time
from selenium import webdriver

class SignInFormCheck(unittest.TestCase):
	#Opening browser.
	def setUp(self):
		EXE_PATH = r'/Users/taipham/Documents/selenium/chromedriver'
		self.driver = webdriver.Chrome(executable_path=EXE_PATH)

	# Test click page
	def test_aboutPage(self):
		driver=self.driver
		driver.get('http://taipham.pythonanywhere.com/')
		about_link = driver.find_element_by_xpath("/html/body/nav/ul/li[2]/a")
		about_link.click()

		# check news
		page_heading = driver.find_element_by_class_name('page-heading')
		assert page_heading.text == 'What is SportsChoice?'

	#Testing Single Input Field.   
	def test_signInForm(self):
		driver=self.driver
		driver.get('http://taipham.pythonanywhere.com/')
		# click button
		join_button = driver.find_element_by_class_name('btn-readmore')
		join_button.click()
		time.sleep(3)

		# click sign in
		signin_button = driver.find_element_by_class_name('twitter')
		signin_button.click()

		# sign in
		username = driver.find_element_by_id("id_username")
		password = driver.find_element_by_id("id_password")
		username.send_keys("test1")
		password.send_keys("cmpe280123")
		driver.find_element_by_name("signup-button").click()

		# check news
		page_heading = driver.find_element_by_class_name('page-heading')
		assert page_heading.text == 'Your News Feed'
	
	# Closing the browser.
	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()