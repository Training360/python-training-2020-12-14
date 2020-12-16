from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_search_python_training():
  driver = webdriver.Chrome("C:\\training\\chromedriver.exe")

  driver.get("https://www.training360.com/")
  driver.set_window_size(1296, 1400)
  driver.find_element(By.XPATH, '//*[@id="NewsletterModalCloseButton"]').click()
  driver.find_element(By.CSS_SELECTOR, "#PrimaryNavMainMenu > li:nth-child(4) > a").click()
  driver.find_element(By.ID, "CourseFilterExpression").click()
  driver.find_element(By.ID, "CourseFilterExpression").send_keys("python")
  driver.find_element(By.ID, "CourseFilterExpression").send_keys(Keys.ENTER)
  driver.find_element(By.XPATH, '/html/body/main/div[2]/section[3]/div[4]/div/div[2]/div/div/a').click()
  assert driver.find_element(By.CSS_SELECTOR, ".header__shortid").text == "PR-PYB"
  
