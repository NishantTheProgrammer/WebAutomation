import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):   #function for speaking
    engine.say(audio)
    engine.runAndWait()

#Let's try

name=input("Enter Name of Friend: ")
driver=webdriver.Chrome()

def login(username, password):  #function for login into Facebook
    driver.get("https://mbasic.facebook.com")
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_name("pass").send_keys(Keys.RETURN)
    driver.find_element_by_name("submit[Continue]").click()
    Select(driver.find_element_by_name("verification_method")).select_by_visible_text("Provide your date of birth")
    driver.find_element_by_name("submit[Continue]").click()
    Select(driver.find_element_by_name("birthday_captcha_day")).select_by_value("25")
    Select(driver.find_element_by_name("birthday_captcha_month")).select_by_value("11")
    Select(driver.find_element_by_name("birthday_captcha_year")).select_by_value("1999")
    driver.find_element_by_name("submit[Continue]").click()
    driver.find_element_by_name("submit[Continue]").click()
    driver.get("https://mbasic.facebook.com/buddylist.php")


login("knishant113@gmail.com", "ExperimentsWith{Code}")    #calling login function
driver.get("https://mbasic.facebook.com/buddylist.php")

while(True):
    buddyList=driver.find_elements_by_class_name("bo")
    i=-1
    for buddy in buddyList:
        i=i+1
        #print(buddy.text+" "+str(i))
        if buddy.text==name:
            break
    try:
        online=driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/div[2]/div/table[{i}]/tbody/tr/td[2]/img')
        if online.get_attribute("aria-label")=="Active now":
            speak(f"Nishant Bhai, {buddyList[i].text} online hai")
        time.sleep(4)
        driver.refresh()
    except Exception as e:
        time.sleep(4)
        driver.refresh()