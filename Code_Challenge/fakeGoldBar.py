######################################################################
# Author   : Bharath Kumar Galla.
# Date     : July 06, 2024.
# Project  : Fetch Coding Exercise - SDET.
# Test     : Finding the fake gold bar.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Function to check if the bar is faulty.
def faulty_check(driver, num1, num2, num3):
    # weighing for the second time
    driver.find_element(by=By.CSS_SELECTOR, value="#left_0").send_keys(num1)
    driver.find_element(by=By.CSS_SELECTOR, value="#right_0").send_keys(num2)
    driver.find_element(by=By.ID, value="weigh").click()

    # Fetching the final weighing result
    final_result = driver.find_element(by=By.XPATH, value="//ol/li[2]").text
    weighings_output = driver.find_element(by=By.XPATH, value="//ol").text.split("\n")
    final_result = final_result.split()[1]

    # Clicking the button with the number based on the result.
    if final_result == "=":
        driver.find_element(by=By.ID, value="coin_" + str(num3)).click()
    elif final_result == ">":
        driver.find_element(by=By.ID, value="coin_" + str(num2)).click()
    else:
        driver.find_element(by=By.ID, value="coin_" + str(num1)).click()

    # Fetching the alert message.
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_message = driver.switch_to.alert.text

    # Printing the output.
    print("Alert Message is: " + alert_message)
    print(f"Weighings are: {weighings_output}")
    driver.quit()


def fakeGoldBar():
    # Initializing the WebDriver.
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    # Navigating to the provided URL.
    driver.get("http://sdetchallenge.fetch.com/")

    # Providing input to the left and right bowls.
    for i in range(3):
        driver.find_element(by=By.CSS_SELECTOR, value=f"#left_{i}").send_keys(i)
        driver.find_element(by=By.CSS_SELECTOR, value=f"#right_{i}").send_keys(i + 3)

    # Checking the weight of the bars.
    driver.find_element(by=By.ID, value="weigh").click()

    # Result of the weighing and resetting.
    weighings = driver.find_element(by=By.XPATH, value="//ol/li").text
    initial_result = weighings.split()[1]
    driver.find_element(by=By.XPATH, value="//div/div[4]/button[1]").click()

    # Validating the result and calling the faulty check to find the bar
    if initial_result == "=":
        faulty_check(driver, 6, 7, 8)
    elif initial_result == ">":
        faulty_check(driver, 3, 4, 5)
    else:
        faulty_check(driver, 0, 1, 2)


# Calling the function to start the execution.
fakeGoldBar()
