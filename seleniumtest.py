from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://prashannachand.com.np")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Home").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"About").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Skills").click()
time.sleep(5)

#project section
driver.find_element(By.LINK_TEXT,"Projects").click()
time.sleep(5)

#viewing each project(currently viewing only 3)

# library management wala

driver.find_element(By.XPATH,"//*[@id='projects']/div/div/div[2]/a").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='project-detail']/div/div/div/a").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])

#sign language wala
driver.find_element(By.LINK_TEXT,"Projects").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='projects']/div/div/div[3]/a").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='project-detail']/div/div/div/a").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])

#cat dog wala
driver.find_element(By.LINK_TEXT,"Projects").click()
time.sleep(5)

##view project tests
driver.find_element(By.XPATH,"//*[@id='projects']/div/div/div[4]/a[2]").click()
time.sleep(5)

#aba since same page ma khulyo i need to go back 
driver.back()

##heading towards the contact section
driver.find_element(By.LINK_TEXT,"Contact").click()
time.sleep(5)

##scroll until i find get in touch
GIT=driver.find_element(By.XPATH, "//*[@id='contact-form']")
driver.execute_script("arguments[0].scrollIntoView();", GIT)
time.sleep(3)

#testing by sending anything in get in touch 
driver.find_element(By.XPATH,"//*[@id='name']").send_keys("test123")
driver.find_element(By.XPATH,"//*[@id='email']").send_keys("test@gmail.com")
driver.find_element(By.XPATH,"//*[@id='subject']").send_keys("subjectabc")
driver.find_element(By.XPATH,"//*[@id='message']").send_keys("message for automation test")
driver.find_element(By.XPATH,"//*[@id='contact-form']/button").click()
time.sleep(5)
driver.back()

## checking for social medias

#github
driver.find_element(By.XPATH,"/html/body/footer/div/a[1]").click()
time.sleep(3)

#facebook
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,"/html/body/footer/div/a[3]").click()
time.sleep(3)

#instagram
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,"/html/body/footer/div/a[4]").click()
time.sleep(3)

#linkedin
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,"/html/body/footer/div/a[2]").click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[0])

#moving towards the experience section
driver.find_element(By.LINK_TEXT,"Experiences").click()
time.sleep(5)
##scroll until i find get in touch
scrol1=driver.find_element(By.XPATH, "//*[@id='experience']/div/div/div[2]/p")
driver.execute_script("arguments[0].scrollIntoView();", scrol1)
time.sleep(1)
scrol2=driver.find_element(By.XPATH, "/html/body/footer/p")
driver.execute_script("arguments[0].scrollIntoView();", scrol2)

time.sleep(5)

driver.quit()
