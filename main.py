from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker
import random
import time



class ScammerBot:

    def __init__(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Chrome(
            executable_path="/Users/joshmanik/Downloads/chromedriver 3", options=options)

    def closeBrowser(self):
        self.browser.close()

    def fillOutScams(self):
        browser = self.browser
        browser.get("https://royalmail-arrival.com")
        count = 0

        while True:
            browser.get("https://royalmail-arrival.com")
            UserName, email, PhoneNumber, address, postcode, city, dob, DummyCard, CVV, expiry_date = genDetails()
            nameTextBox = browser.find_element_by_xpath('//*[@id="name"]')
            nameTextBox.send_keys(UserName)
            DOBTextBox = browser.find_element_by_xpath('//*[@id="dob"]')
            DOBTextBox.send_keys(str(dob))
            emailTextBox = browser.find_element_by_xpath('//*[@id="email"]')
            emailTextBox.send_keys(email)
            phoneTextBox = browser.find_element_by_xpath('//*[@id="phone"]')
            phoneTextBox.send_keys(PhoneNumber)
            addressTextBox = browser.find_element_by_xpath('//*[@id="address"]')
            addressTextBox.send_keys(address)
            cityTextBox = browser.find_element_by_xpath('//*[@id="city"]')
            cityTextBox.send_keys(city)
            postcodeTextBox = browser.find_element_by_xpath('//*[@id="postcode"]')
            postcodeTextBox.send_keys(postcode)
            continueButton = browser.find_element_by_xpath('//*[@id="sendMessageButton"]')
            continueButton.click()
            time.sleep(0.5)
            NameOnCardTextBox = browser.find_element_by_xpath('//*[@id="name"]')
            NameOnCardTextBox.send_keys(UserName)
            CardNumberTextBox = browser.find_element_by_xpath('//*[@id="phone"]')
            CardNumberTextBox.send_keys(DummyCard)
            ExpiryDateTextBox = browser.find_element_by_xpath('//*[@id="ccexp"]')
            ExpiryDateTextBox.send_keys(expiry_date)
            CVVTextBox = browser.find_element_by_xpath('/html/body/section/div/div[2]/div/form/div[4]/div/input')
            CVVTextBox.send_keys(CVV)
            Complete = browser.find_element_by_xpath('//*[@id="sendMessageButton"]')
            Complete.click()
            count += 1
            print("Submitted Fake Details under the name " + UserName + " " + str(count) + " Times")

def genDetails():
    fake = Faker('en_UK')
    Phone_1 = random.randint(0, 9)
    Phone_2 = random.randint(0, 9)
    Phone_3 = random.randint(0, 9)
    Phone_4 = random.randint(0, 9)
    Phone_5 = random.randint(0, 9)
    Phone_6 = random.randint(0, 9)
    Phone_7 = random.randint(0, 9)
    Phone_8 = random.randint(0, 9)
    Phone_9 = random.randint(0, 9)
    Phone_10 = random.randint(0, 9)

    UserName = fake.name()
    emailname = UserName.replace(" ", "")
    email = emailname + str(Phone_9) + str(Phone_4) + str(Phone_1) + '@gmail.com'
    PhoneNumber = "+44" + str(Phone_1) + str(Phone_2) + str(Phone_3) + str(Phone_4) + str(Phone_5) + str(Phone_6) \
                  + str(Phone_7) + str(Phone_8) + str(Phone_9) + str(Phone_10)
    address = fake.street_name()
    postcode = fake.postcode()
    city = fake.city()
    dob = fake.date_of_birth(minimum_age=15)
    DummyCard = '4596' + '0' + str(Phone_7) + str(random.randint(0, 9)) + str(random.randint(0, 9)) \
                + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) \
                + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) \
                + str(random.randint(0, 9)) + str(random.randint(0, 9))
    CVV = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    expiry = ['/23', '/24', '/25', '/26', '/27', '/28', '/29']
    decider = random.randint(0, 6)
    first_date = str(random.randint(0, 12))
    if len(first_date) == 2:
        pass
    else:
        first_date = "0" + str(first_date)

    expiry_date = str(first_date) + expiry[decider]

    return UserName, email, PhoneNumber, address, postcode, city, dob, DummyCard, CVV, expiry_date

if __name__ == "__main__":
    Bot = ScammerBot()
    Bot.fillOutScams()
